#!/usr/bin/env python3
import numpy as np
from mate_funcs import *
#from pygame import *
import pygame

class Robot():

    def __init__(self,surface ,name='robot' ,pos=[0.0 ,0.0, 0.0 ], visible = True ):
        pos = np.matrix([pos[0], pos[1], pos[2], 1])
        self.name = name
        self.pos = translation(pos, [int(surface.get_width()/2),int(surface.get_height()/2),0])
        self.surface = surface
        self.visible = visible

    def translation(self, vector):
        pass

    def getPos(self):
        return self.pos

    def setPos(self, pos=[0.0,0.0]):
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


class DDR(Robot):

    def __init__(self,surface , name='robot', pos=[0, 0],radious = 100.0,color = [0,0,0] ):

        Robot.__init__(self,surface ,name ,pos)
        self.color = color
        self.radious = radious


    def getRadious(self):
        return self.radious

    def setRadious(self, radious = 100.0):
        self.radious = radious

    def draw(self):
        position = [self.pos.item(0),self.pos.item(1)]
        end_line = [self.pos.item(0) + self.radious,self.pos.item(1)]
        pygame.draw.circle(self.surface, self.color, position, self.radious)
        pygame.draw.line(self.surface,[0,0,0] , position ,end_line ,3)
        return True
