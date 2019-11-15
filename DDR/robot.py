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
        self.dir_ang = 1
        self.dir = 1
        self.tarAng = self.angle
        self.target_pos = self.pos
        self.target_point = [0,0]


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
            vector = Rotz([speed,0,0,1], self.getAngle())

            self.pos = translation(self.getPos(), vector)

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
