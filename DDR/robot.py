#!/usr/bin/env python3
import numpy as np
from mate_funcs import *
from Model import *
import numpy as np
#from pygame import *
import pygame

class Robot(Collider):

    def __init__(self,surface ,name, pos, boundary):
        visible = True
        self.visible = visible
        Collider.__init__(self,surface ,name ,pos, boundary)

    def rotate(self,ang):
        pass

    def move(self, vector):
        if vector[0] == 0 and vector[1] == 0:
            pass

        else:
            self.pos = translation(self.getPos(), np.matrix([vector[0],vector[1],0,1]))

class LidarL(Robot):
    def __init__(self, surface, name, colliders, parent, step = 8):
        self.parent = parent
        self.pos = parent.getPos()
        self.radious = parent.getRadious()
        self.offsetAngle = 0
        self.step = step
        self.boundary = []
        self.colliders = colliders
        self.closeSensorDist = 99999
        for x in range(self.offsetAngle , 360, self.step):
            print(x)
            self.boundary.append(LaserLine(surface, np.matrix([0 ,0,0,1]), (x*np.pi/180) + parent.getAngle(), self.radious))

        Robot.__init__(self, surface, name, self.pos, self.boundary)

    def update(self):
        #if self.getParent().updating:
        if True:
            self.closeSensorDist = 99999
            for laser in  self.boundary:
                laser.update(self.getParent().getAngle(), self.getParent().getPos())
                #print (laser.distValue)
                laser.check_Collision(self.colliders)
                dist = laser.distValue
                #dist = -self.radious +  dis_Between([self.getParent().getPos().item(0),self.getParent().getPos().item(1)], laser.check_Collision(self.colliders))
                if dist < self.closeSensorDist:
                    self.closeSensorDist = dist

    def getCloseSensorDist(self):
        return self.closeSensorDist

    def setParent(self, parent):
        self.parent = parent

    def getParent(self):
        return self.parent


class DDR(Robot):

    def __init__(self,surface , name, pos ,radious = 100.0,angle = 0 ,color = [0,0,0] ):

        self.boundary = pygame.Rect(pos[0],pos[1], radious*2,radious*2)
        pos = np.matrix([pos[0],pos[1], 0, 1])
        Robot.__init__(self,surface ,name ,pos, self.boundary)
        self.color = color
        self.radious = radious
        self.end_line = np.matrix([self.getRadious(),0,0,1])
        self.angle = 0
        self.rotate(angle)
        print (self.getName(), self.getAngle(), self.getPos())
        self.dir_ang = 1
        self.dir = 1
        self.tarAng = self.angle
        self.target_pos = self.pos
        self.target_point = np.matrix([0,0,0,1])
        self.end_angle = 0
        self.setPos(pos)
        self.first_step = False
        self.second_step = False
        self.third_step = False
        self.updating = True
        self.stop = True
        self.AngleSpeed = .5 * np.pi/180
        self.config = [self.get_posxy(),self.getAngle()]
        self.distanceTravel = 0


    def getBoundary(self):
        self.boundary = pygame.Rect(self.get_posxy()[0]-self.getRadious(),self.get_posxy()[1]-self.getRadious(), self.getRadious()*2, self.getRadious()*2)
        return self.boundary


    def set_first_step(self, bool):
        self.first_step = bool

    def set_second_step(self, bool):
        self.second_step = bool

    def set_third_step(self, bool):
        self.third_step = bool

    def get_first_step(self):
        return self.first_step

    def get_second_step(self):
        return self.second_step

    def get_third_step(self):
        return self.third_step

    def getEnd_line(self):
        return self.end_line

    def getRadious(self):
        return self.radious

    def setRadious(self, radious):
        self.radious = radious

    def getAngle(self):
        return self.angle

    def setAngle(self, ang):
        self.angle = ang

    def get_target_Angle(self):
        return self.tarAng

    def set_target_Angle(self, tarAng):
        self.tarAng = tarAng

    def get_dir_ang(self):
        return self.dir_ang

    def set_dir_ang(self, dir_ang):
        self.dir_ang = dir_ang

    def get_dir(self):
        return self.dir

    def set_dir(self, dir):
        self.dir = dir

    def rotate(self,ang):
        if ang != 0:
            self.end_line = Rotz(self.end_line, ang )
            self.setAngle(self.getAngle() + ang)

    def rotateq(self,ang):
        if ang != 0:
            q = np.matrix([np.cos(ang/2), 0, 0, np.sin(ang/2)])
            p = np.matrix([1,self.end_line.item(0), self.end_line.item(1), 0])
            self.end_line = R_quaternion(q, p)
            self.setAngle(self.getAngle() + ang)

    def forward(self, speed):

        if speed != 0:
            self.updating = True
            vector = Rotz([speed,0,0,1], self.getAngle())

            self.pos = translation(self.getPos(), vector)
            self.config = [self.get_posxy(),self.getAngle()]
            self.distanceTravel += speed




    def draw(self):
        position = translation(self.pos,np.matrix([int(self.surface.get_width()/2),int(self.surface.get_height()/2),0]))

        end_line_draw = translation(self.end_line,position)
        end_line_draw = [end_line_draw.item(0), end_line_draw.item(1)]

        pygame.draw.circle(self.surface, self.color,[int(position.item(0)), int(position.item(1)) ], self.radious)
        pygame.draw.line(self.surface,[0,0,0] , [position.item(0), position.item(1) ], end_line_draw ,3)
        return True

    def get_target_pos(self):
        return self.target_pos

    def set_target_pos(self, target_pos):
        self.target_pos = target_pos

    def set_target_point(self, target_point):
        self.target_point = target_point

    def get_target_point(self):
        return self.target_point

    def set_end_angle(self, end_angle):
        self.end_angle = end_angle

    def do_first_step(self):

        if not self.get_first_step():
            self.updating = True

            if self.get_target_Angle() >= self.getAngle():

                self.set_dir_ang(1)

                if self.getAngle() < self.get_target_Angle() * self.get_dir_ang():
                    #self.rotateq(.5*self.get_dir_ang() * np.pi/180)

                    if self.get_target_Angle() - self.getAngle() < 0.01:
                        self.set_first_step(True)
                    else:
                        self.rotateq(.5*self.get_dir_ang() * np.pi/180)
                        #print (self.getAngle(), self.get_target_Angle())

            else:
                self.set_dir_ang(-1)

                if self.getAngle() > -self.get_target_Angle() * self.get_dir_ang():
                    #self.rotateq(.5*self.get_dir_ang() * np.pi/180)

                    if  self.get_target_Angle() - self.getAngle() - np.pi > 0.01:
                        self.set_first_step(True)
                    else:
                        self.rotateq(.5*self.get_dir_ang() * np.pi/180)

        # if self.getAngle() >=  np.pi:
        #     print (self.getAngle())
        #     self.setAngle(self.getAngle() - 2 * np.pi)
        #     print (self.getAngle())
        #
        # if self.getAngle() <= -1 * np.pi:
        #     self.setAngle(self.getAngle() + 2 * np.pi)

    def do_second_step(self):
        if self.get_first_step() and not self.get_second_step():

            targetx = self.get_target_pos().item(0,0)
            targety = self.get_target_pos().item(0,1)

            posx = self.getPos().item(0,0)
            posy = self.getPos().item(0,1)

            #self.forward(self.get_dir()*.1)
            if  dis_Between([posx,posy],[targetx,targety]) < 5:
                self.set_second_step(True)
            else:
                #self.forward(self.get_dir()*.1)
                if not self.get_second_step():
                    self.forward(self.get_dir())



    def do_third_step(self):
        if self.get_first_step() and self.get_second_step() and not self.get_third_step():

            if (self.getAngle() <= -np.pi ):
                self.setAngle(self.getAngle() + 2*np.pi)

            if (self.getAngle() >= np.pi ):
                self.setAngle(self.getAngle() - 2*np.pi)

            if (self.end_angle <= -np.pi ):
                self.end_angle =self.end_angle + 2*np.pi

            if (self.end_angle >= np.pi ):
                self.end_angle = self.end_angle - 2*np.pi

            if self.end_angle >= self.getAngle() :
                self.set_dir_ang(1)

                if self.getAngle() < self.end_angle * self.get_dir_ang():
                    #self.rotateq(.5*self.get_dir_ang() * np.pi/180)

                    if self.end_angle - self.getAngle() < 0.01:
                        self.set_third_step(True)
                        self.updating = False
                    else:
                        self.rotateq(.5*self.get_dir_ang() * np.pi/180)

            else:

                self.set_dir_ang(-1)
                if self.getAngle() > -self.end_angle * self.get_dir_ang():
                    if  self.end_angle - self.getAngle()-np.pi > 0.01:

                        self.set_third_step(True)
                        self.updating = False
                    else:
                        self.rotateq(.5*self.get_dir_ang() * np.pi/180)

        # if self.getAngle() >=  np.pi:
        #     print (self.getAngle())
        #     self.setAngle(self.getAngle() - 2 * np.pi)
        #     print (self.getAngle())
        #
        # if self.getAngle() <= -1 * np.pi:
        #     self.setAngle(self.getAngle() + 2 * np.pi)


    def moveto(self,targetPos, targetAngel):

        self.setStop(False)
        self.set_target_point(targetPos)
        self.set_end_angle(targetAngel)
        self.set_first_step(False)
        self.set_second_step(False)
        self.set_third_step(False)

        if self.target_point.item(0) > self.getPos().item(0):
            slope = line_slop(self.getPos(),self.get_target_point())
            angle = np.arctan(slope)
        else:
            slope = + line_slop(self.getPos(),self.get_target_point())
            angle = - np.pi + np.arctan(slope)

        if self.target_point.item(0) == self.getPos().item(0):
            angle = targetAngel

        self.set_target_Angle(angle)
        self.set_target_pos(self.get_target_point())
        #print("angulo objetivo: ",self.end_angle)

    def update(self):

        if not self.getStop():
            self.do_first_step()

            self.do_second_step()

            self.do_third_step()
        else:
            self.set_third_step(True)
            self.updating = False
        self.config = [self.get_posxy(),self.getAngle()]


    def getStop(self):
        return self.stop

    def setStop(self, stop):
        self.stop = stop
