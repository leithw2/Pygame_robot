#!/usr/bin/env python3
import numpy as np
from mate_funcs import *
from Model import *
#from pygame import *
import pygame

class Robot(Collider):

    def __init__(self,surface ,name='robot' ,pos=[0.0 ,0.0, 0.0 ],boundary = pygame.Rect(0,0,0,0), visible = True  ):
        self.visible = visible
        Collider.__init__(self,surface ,name ,pos, boundary)

    def rotate(self,ang):
        pass

    def move(self, vector):
        if vector[0] == 0 and vector[1] == 0:
            pass

        else:
            self.pos = translation(self.getPos(), np.matrix([vector[0],vector[1],0]))


class DDR(Robot):

    def __init__(self,surface , name='robot', pos=[0.0, 0.0, 0.0],radious = 100.0,angle = 0 ,color = [0,0,0] ):

        Robot.__init__(self,surface ,name ,pos)
        self.color = color
        self.radious = radious
        self.end_line = np.matrix([self.getRadious(),0,0,1])
        self.angle = 0
        self.rotate(angle)
        print (self.getName(), self.getAngle())
        self.pastAngle = 0

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

    def rotate(self,ang):
        if ang != 0:
            self.end_line = Rotz(self.end_line, ang )
            self.setAngle(self.getAngle() + ang)

    def forward(self, speed):
        if speed != 0:
            vector = Rotz([speed,0,0,1], self.getAngle())
            #print (self.getName(),  self.getAngle())
            self.pos = translation(self.getPos(), vector)

    def draw(self):
        position = translation(self.pos,np.matrix([int(self.surface.get_width()/2),int(self.surface.get_height()/2),0]))

        end_line_draw = translation(self.end_line,position)
        end_line_draw = [end_line_draw.item(0), end_line_draw.item(1)]

        pygame.draw.circle(self.surface, self.color,[int(position.item(0)), int(position.item(1)) ], self.radious)
        pygame.draw.line(self.surface,[0,0,0] , [position.item(0), position.item(1) ], end_line_draw ,3)
        return True
