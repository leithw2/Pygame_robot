#!/usr/bin/env python3
import numpy as np
import pygame
from mate_funcs import *

class Model():

    def __init__(self,surface ,name='' ,pos=np.matrix([0,0,0,1])):
        self.pos = np.matrix([pos.item(0), pos.item(1), pos.item(2), pos.item(3)])
        self.name = name
        self.surface = surface

    def getPos(self):
        return self.pos

    def get_posxy(self):
        return [self.getPos().item(0), self.getPos().item(1)]

    def setPos(self, pos):
        self.pos = pos

    def getName(self):
        return self.name

    def setName(self, name='robot'):
        self.name = name

    def setSurface(self, surface):
        self.surface = surface

    def getSurface(self):
        return self.surface

    def draw(self):
        pass

class Point(Model):
    def __init__(self, surface, pos):
        name=""
        Model.__init__(self,surface ,name ,pos)
        self.color = [0,255,0]

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def draw(self):
        center = [int(self.surface.get_width()/2 + self.getPos().item(0)), int(self.surface.get_height()/2 + self.getPos().item(1))]
        pygame.draw.circle(self.getSurface(), self.getColor(), center, 2)

class LaserLine(Model):
    def __init__(self, surface, pos, angle, radious, distance = 200 , step = 10):
        name=("sensor a ",angle * 180/np.pi, " grados")
        Model.__init__(self,surface ,name ,pos)
        self.color = [0,255,0]
        self.angle = angle
        self.distance = distance
        self.step = step
        self.radious = radious
        self.distValue =  distance
        self.collidePoint = [distance,distance]

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setPos(self, pos):
        self.pos = pos

    def getAngle(self):
        return self.angle

    def setAngle(self, ang):
        self.angle = ang

    def setDir(self, dir):
        self.dir = dir

    def getDir(self):
        return self.dir

    def check_Collision(self, colliders):
        for trace in range(self.radious, self.distance + self.radious, self.step):
            #print (self.radious, self.distance + self.radious, self.step)
            for collider in colliders:
                self.collidePoint = [self.getPos().item(0) + (self.getDir()[0] * trace)   , self.getPos().item(1) + (self.getDir()[1] * trace) ]
                if collider.collidepoint(self.collidePoint):
                    self.distValue = -self.radious + dis_Between([self.getPos().item(0),self.getPos().item(1)], self.collidePoint)
                    pygame.draw.circle(self.getSurface(), [255,0,0], [int(self.collidePoint[0] + self.getSurface().get_width()/2 ),int(self.collidePoint[1] + self.getSurface().get_height()/2)], 2)
                    return self.collidePoint
                else:
                    self.distValue = 1000
                    pygame.draw.circle(self.getSurface(), self.getColor(), [int(self.collidePoint[0] + self.getSurface().get_width()/2 ),int(self.collidePoint[1] + self.getSurface().get_height()/2)], 2)

        return [1000, 1000]

    def update(self,ParentAngle,ParentPos ):
        self.setDir( [np.cos(ParentAngle + self.getAngle()), np.sin(ParentAngle + self.getAngle())] )
        self.setPos(ParentPos)

        #print (self.getDir())

class Collider(Model):

    def __init__(self,surface,name, pos, boundary):
        Model.__init__(self,surface ,name ,pos)
        self.boundary = boundary

    def check_Collision(self, collider):
        return False

    def getBoundary(self):
        return self.boundary

    def setBoundary(self, boundary):
        self.boundary = boundary
