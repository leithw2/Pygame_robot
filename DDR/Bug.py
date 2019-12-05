#!/usr/bin/env python3
import numpy as np
import pygame
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from mate_funcs import *

class controlBug1():
    def __init__(self, ddr, qGoal, lidar):
        self.ddr = ddr
        self.qGoal = qGoal
        self.lidar = lidar
        self.configs = []
        self.initConfig = self.ddr.config
        self.firstConfig = []
        self.closestConf = dis_Between(self.ddr.get_posxy(), qGoal.get_posxy())
        self.distToGoal = dis_Between(self.ddr.get_posxy(), qGoal.get_posxy())
        self.circumnavigating = False
        self.movingToGoal = False
        self.rotating = False
        self.dispacing = False
        self.rotatingStep = 19
        self.step = 1
        self.sensor1 = False
        self.sensor2 = False
        self.sensor3 = False
        self.sensor1C = False
        self.sensor2C = False
        self.sensor3C = False
        self.stateMachine = 0
        self.WAITING = 0
        self.ROT_IZQ = 1
        self.ROT_DER = 2
        self.FRW = 3
        self.snapShots = [self.ddr.config[0]]
        self.stateMachine2 = 0
        self. minDistance = 0




    def folloWall(self):
        self.sensor1 = False
        self.sensor2 = False
        self.sensor3 = False
        self.sensor1C = False
        self.sensor2C = False
        self.sensor3C = False
        self.stateMachine = 0

        #print (self.ddr.getAngle())

        if not self.ddr.updating or self.dispacing:
            self.dispacing = False

            if self.lidar.getBoundary()[0].distValue < self.lidar.getBoundary()[0].distance -0:
                self.sensor1 = True
                self.lidar.getBoundary()[0].setColor([255,255,0])

            else:
                self.lidar.getBoundary()[0].setColor([0,255,0])

            if self.lidar.getBoundary()[1].distValue < self.lidar.getBoundary()[1].distance -10:
                self.sensor2 = True
                self.lidar.getBoundary()[1].setColor([255,255,0])
            else:
                self.lidar.getBoundary()[1].setColor([0,255,0])

            if self.lidar.getBoundary()[2].distValue < self.lidar.getBoundary()[2].distance -00:
                self.sensor3 = True
                self.lidar.getBoundary()[2].setColor([255,255,0])
            else:
                self.lidar.getBoundary()[2].setColor([0,255,0])

            if self.lidar.getBoundary()[0].distValue <= self.lidar.getBoundary()[0].distance -25:
                self.sensor1C = True
                self.lidar.getBoundary()[0].setColor([255,0,0])

            if self.lidar.getBoundary()[1].distValue <= self.lidar.getBoundary()[1].distance -25:
                self.sensor2C = True
                self.lidar.getBoundary()[1].setColor([255,0,0])

            if self.lidar.getBoundary()[2].distValue <= self.lidar.getBoundary()[2].distance -25:
                self.sensor3C = True
                self.lidar.getBoundary()[2].setColor([255,0,0])

            if self.sensor1 or self.sensor2:
                self.stateMachine = self.ROT_IZQ

            if self.sensor1 and self.sensor2:
                self.stateMachine = self.FRW

            if self.sensor2 and self.sensor3C:
                self.stateMachine = self.FRW

            if not self.sensor1 and not self.sensor2 and not self.sensor3:
                self.stateMachine = self.ROT_DER

            if (not self.sensor1 and not self.sensor2) and self.sensor3:
                self.stateMachine = self.FRW

            if (not self.sensor1 and not self.sensor2) and not self.sensor3:
                self.stateMachine = self.ROT_DER

            if not self.sensor1 and self.sensor2 and not self.sensor3:
                self.stateMachine = self.FRW

            if not self.sensor1 and not self.sensor2 and not self.sensor3:
                self.stateMachine = self.FRW

            if (not self.sensor1 and not self.sensor2) and not self.sensor3:
                self.stateMachine = self.ROT_DER

            if self.sensor1 and not self.sensor2 and not self.sensor3:
                self.stateMachine = self.FRW

            if not self.sensor1 and not self.sensor2C and not self.sensor3C and self.sensor2 and self.sensor3:
                self.stateMachine = self.FRW

            if not self.sensor1 and self.sensor2C and self.sensor3C:
                self.stateMachine = self.ROT_IZQ

            if not self.sensor1 and  not self.sensor2 and self.sensor3C:
                self.stateMachine = self.FRW

            if self.sensor1 and self.sensor3 and not self.sensor2 and not self.sensor2C  :
                self.stateMachine = self.FRW

            if self.sensor1C :
                self.stateMachine = self.ROT_IZQ

            if self.sensor2 and self.sensor3 and (not self.sensor2C and not self.sensor3C):
                self.stateMachine = self.FRW

        if self.stateMachine == self.ROT_IZQ:
            self.angleTarget = self.ddr.getAngle() - self.rotatingStep * np.pi/180
            self.ddr.moveto(self.ddr.getPos(), self.angleTarget)

        if self.stateMachine == self.ROT_DER:
            self.angleTarget = self.ddr.getAngle() + self.rotatingStep * np.pi/180
            self.ddr.moveto(self.ddr.getPos(), self.angleTarget)

        if self.stateMachine == self.FRW:

            self.dispacing = True
            self.ddr.forward(.5)


        if self.stateMachine2 == 0:
            if self.ddr.getBoundary().collidepoint(self.getfirstConfig()[0]):
                pass
                #print ("vuelta completa!!!")
            else:
                #print ("Deja el primero")
                self.stateMachine2 = 1

        if self.stateMachine2 == 1:
            if self.ddr.getBoundary().collidepoint(self.getfirstConfig()[0]):
                #print ("Regreso")
                self.minDistance = dis_Between(self.getfirstConfig()[0], self.qGoal.get_posxy())

                for snap in self.snapShots:
                    dis = dis_Between(snap, self.qGoal.get_posxy())
                    if dis < self.minDistance:
                        self.minDistance =  dis
                        #print (dis)
                        self.closestConf = snap

                self.stateMachine2 = 2

        if self.stateMachine2 == 2:

            if self.ddr.getBoundary().collidepoint(self.closestConf):
                self.circumnavigating = False
                #self.movingToGoal = True
                #print("closestReach")
                self.stateMachine2 == 0

    def moveToGoal(self):
        if not self.isMovingToGoal():
            self.movingToGoal = True
            self.ddr.moveto(self.qGoal.getPos(),0)
            self.ddr.setStop(False)
            #print("movingToGoal")

    def setfirstConfig(self,firstConfig):
        self.firstConfig = firstConfig

    def getfirstConfig(self):
        return self.firstConfig

    def setClosestConf(self, closestConf):
        self.closestConf = closestConf

    def getCosestConf(self):
        return self.closestConf

    # def distanceToGoal():
    #     self.distToGoal = dis_Between(self.ddr.get_posxy(), qGoal.get_posxy())

    def update(self):
        self.ddr.update()
        self.lidar.update()
        if self.ddr.getBoundary().collidepoint(self.qGoal.get_posxy()):
            #print("Fin")
            return
        if self.ddr.distanceTravel > 10 * self.step:
            self.step += 1
            self.snapShots.append(self.ddr.config[0])
            #print(dis_Between(self.ddr.config[0], self.qGoal.get_posxy()))

        if not self.isCircumnavigating():
            self.moveToGoal()

            if self.lidar.getCloseSensorDist() < 20:

                self.ddr.setStop(True)
                self.setfirstConfig(self.ddr.config)
                self.circumnavigating = True
                self.movingToGoal = False
        else:
            self.folloWall()

    def isCircumnavigating(self):
        return self.circumnavigating

    def isMovingToGoal(self):
        return self.movingToGoal

    def drawSteps(self, surface):
        for point in self.snapShots:
            center = [int(surface.get_width()/2 + point[0]), int(surface.get_height()/2 + point[1])]
            pygame.draw.circle(surface, [0,0,255], center, 2)
            drawInit = [int(surface.get_width()/2 + self.ddr.getBoundary().x), int(surface.get_height()/2 + self.ddr.getBoundary().y)]
            pygame.draw.rect(surface,[255,0,0], pygame.Rect(drawInit, [self.ddr.getBoundary().width,self.ddr.getBoundary().height]), 1)

            #pygame.draw.circle(surface, [255,0,0], center, 2)
        if self.getfirstConfig() != []:

            center = [int(surface.get_width()/2 +self.getfirstConfig()[0][0]), int(surface.get_height()/2 + self.getfirstConfig()[0][1])]
            pygame.draw.circle(surface, [0,255,255], center, 3)





#############################################################################################


class controlBug2():
    def __init__(self, ddr, qGoal, lidar):
        self.ddr = ddr
        self.qGoal = qGoal
        self.lidar = lidar
        self.configs = []
        self.initConfig = self.ddr.config
        self.firstConfig = []
        self.firstSlope = line_slop2(self.initConfig[0], self.qGoal.get_posxy())
        self.firstSlopeConfig = []
        self.closestConf = self.ddr.config
        self.distToGoal = dis_Between(self.ddr.get_posxy(), qGoal.get_posxy())
        self.circumnavigating = False
        self.movingToGoal = False
        self.rotating = False
        self.dispacing = False
        self.rotatingStep = 16
        self.step = 1
        self.sensor1 = False
        self.sensor2 = False
        self.sensor3 = False
        self.sensor1C = False
        self.sensor2C = False
        self.sensor3C = False
        self.stateMachine = 0
        self.WAITING = 0
        self.ROT_IZQ = 1
        self.ROT_DER = 2
        self.FRW = 3
        self.snapShots = [self.ddr.config[0]]
        self.stateMachine2 = 0
        self. minDistance = 0




    def folloWall(self):
        self.sensor1 = False
        self.sensor2 = False
        self.sensor3 = False
        self.sensor1C = False
        self.sensor2C = False
        self.sensor3C = False
        self.stateMachine = 0

        #print (self.ddr.getAngle())

        if not self.ddr.updating or self.dispacing:
            self.dispacing = False

            if self.lidar.getBoundary()[0].distValue < self.lidar.getBoundary()[0].distance -0:
                self.sensor1 = True
                self.lidar.getBoundary()[0].setColor([255,255,0])

            else:
                self.lidar.getBoundary()[0].setColor([0,255,0])

            if self.lidar.getBoundary()[1].distValue < self.lidar.getBoundary()[1].distance -0:
                self.sensor2 = True
                self.lidar.getBoundary()[1].setColor([255,255,0])
            else:
                self.lidar.getBoundary()[1].setColor([0,255,0])

            if self.lidar.getBoundary()[2].distValue < self.lidar.getBoundary()[2].distance -10:
                self.sensor3 = True
                self.lidar.getBoundary()[2].setColor([255,255,0])
            else:
                self.lidar.getBoundary()[2].setColor([0,255,0])

            if self.lidar.getBoundary()[0].distValue <= self.lidar.getBoundary()[0].distance -25:
                self.sensor1C = True
                self.lidar.getBoundary()[0].setColor([255,0,0])

            if self.lidar.getBoundary()[1].distValue <= self.lidar.getBoundary()[1].distance -25:
                self.sensor2C = True
                self.lidar.getBoundary()[1].setColor([255,0,0])

            if self.lidar.getBoundary()[2].distValue <= self.lidar.getBoundary()[2].distance -25:
                self.sensor3C = True
                self.lidar.getBoundary()[2].setColor([255,0,0])

            if self.sensor1 or self.sensor2:
                self.stateMachine = self.ROT_IZQ

            if self.sensor1 and self.sensor2:
                self.stateMachine = self.FRW

            if self.sensor2 and self.sensor3C:
                self.stateMachine = self.FRW

            if not self.sensor1 and not self.sensor2 and not self.sensor3:
                self.stateMachine = self.ROT_DER

            if (not self.sensor1 and not self.sensor2) and self.sensor3:
                self.stateMachine = self.FRW

            if (not self.sensor1 and not self.sensor2) and not self.sensor3:
                self.stateMachine = self.ROT_DER

            if not self.sensor1 and self.sensor2 and not self.sensor3:
                self.stateMachine = self.FRW

            if not self.sensor1 and not self.sensor2 and not self.sensor3:
                self.stateMachine = self.FRW

            if (not self.sensor1 and not self.sensor2) and not self.sensor3:
                self.stateMachine = self.ROT_DER

            if self.sensor1 and not self.sensor2 and not self.sensor3:
                self.stateMachine = self.FRW

            if not self.sensor1 and not self.sensor2C and not self.sensor3C and self.sensor2 and self.sensor3:
                self.stateMachine = self.FRW

            if not self.sensor1 and self.sensor2C and self.sensor3C:
                self.stateMachine = self.ROT_IZQ

            if not self.sensor1 and  not self.sensor2 and self.sensor3C:
                self.stateMachine = self.FRW

            if self.sensor1 and self.sensor3 and not self.sensor2 and not self.sensor2C  :
                self.stateMachine = self.FRW

            if self.sensor1C :
                self.stateMachine = self.ROT_IZQ

            if self.sensor2 and self.sensor3 and (not self.sensor2C and not self.sensor3C):
                self.stateMachine = self.FRW

        if self.stateMachine == self.ROT_IZQ:
            self.angleTarget = self.ddr.getAngle() - self.rotatingStep * np.pi/180
            self.ddr.moveto(self.ddr.getPos(), self.angleTarget)

        if self.stateMachine == self.ROT_DER:
            self.angleTarget = self.ddr.getAngle() + self.rotatingStep * np.pi/180
            self.ddr.moveto(self.ddr.getPos(), self.angleTarget)

        if self.stateMachine == self.FRW:

            self.dispacing = True
            self.ddr.forward(.5)


        if self.stateMachine2 == 0:
            slope = line_slop2(self.ddr.get_posxy(), self.qGoal.get_posxy())
            if abs(self.firstSlope - slope) <= .1:

                #print ("First slope Found")
                #print ("Actual: ", slope, "First: ", self.firstSlope, "diference: ", self.firstSlope - slope )
                self.firstSlopeConfig = self.ddr.config

                pass
            else:
                #print ("Left first slope")
                self.stateMachine2 = 1
            pass

        if self.stateMachine2 == 1:
            slope = line_slop2(self.ddr.get_posxy(), self.qGoal.get_posxy())
            #print (abs(self.firstSlope - slope))

            if abs(self.firstSlope - slope) <= 0.1 :
                #print ("New slope found ",self.firstSlopeConfig)
                firstDistToGoal = dis_Between(self.firstSlopeConfig[0], self.qGoal.get_posxy())
                actualDistance = dis_Between(self.ddr.get_posxy(), self.qGoal.get_posxy())

                if firstDistToGoal > actualDistance:
                    self.minDistance =  actualDistance
                    #print (actualDistance)
                    self.closestConf = self.ddr.config
                    self.stateMachine2 = 0
                    self.circumnavigating = False
                    print("closestReach")


    def moveToGoal(self):
        if not self.isMovingToGoal():
            self.movingToGoal = True
            self.ddr.moveto(self.qGoal.getPos(),0)
            self.ddr.setStop(False)
            print("movingToGoal")

    def setfirstConfig(self,firstConfig):
        self.firstConfig = firstConfig

    def getfirstConfig(self):
        return self.firstConfig

    def setClosestConf(self, closestConf):
        self.closestConf = closestConf

    def getCosestConf(self):
        return self.closestConf

    # def distanceToGoal():
    #     self.distToGoal = dis_Between(self.ddr.get_posxy(), qGoal.get_posxy())

    def update(self):
        self.ddr.update()
        self.lidar.update()
        if self.ddr.getBoundary().collidepoint(self.qGoal.get_posxy()):
            print("Fin")
            return
        if self.ddr.distanceTravel > 50 * self.step:
            self.step += 1
            self.snapShots.append(self.ddr.config[0])
            #print(dis_Between(self.ddr.config[0], self.qGoal.get_posxy()))

        if not self.isCircumnavigating():
            self.moveToGoal()


            if self.lidar.getCloseSensorDist() < 20 and dis_Between(self.closestConf[0], self.ddr.get_posxy()) > 30:

                self.ddr.setStop(True)
                self.setfirstConfig(self.ddr.config)
                self.circumnavigating = True
                self.movingToGoal = False
        else:
            self.folloWall()

    def isCircumnavigating(self):
        return self.circumnavigating

    def isMovingToGoal(self):
        return self.movingToGoal

    def drawSteps(self, surface):
        point1 = [int(surface.get_width()/2 + self.initConfig[0][0]), int(surface.get_height()/2 + self.initConfig[0][1])]
        point2 = [int(surface.get_width()/2 + self.qGoal.get_posxy()[0]), int(surface.get_height()/2 + self.qGoal.get_posxy()[1])]

        pygame.draw.line(surface, [255,255,0], point1, point2, 2)
        for point in self.snapShots:
            center = [int(surface.get_width()/2 + point[0]), int(surface.get_height()/2 + point[1])]
            pygame.draw.circle(surface, [0,0,255], center, 2)
            drawInit = [int(surface.get_width()/2 + self.ddr.getBoundary().x), int(surface.get_height()/2 + self.ddr.getBoundary().y)]
            pygame.draw.rect(surface,[255,0,0], pygame.Rect(drawInit, [self.ddr.getBoundary().width,self.ddr.getBoundary().height]), 1)

            #pygame.draw.circle(surface, [255,0,0], center, 2)
        if self.getfirstConfig() != []:

            center = [int(surface.get_width()/2 +self.getfirstConfig()[0][0]), int(surface.get_height()/2 + self.getfirstConfig()[0][1])]
            pygame.draw.circle(surface, [0,255,255], center, 3)
