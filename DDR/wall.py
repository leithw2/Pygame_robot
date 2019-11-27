#!/usr/bin/env python3
from Model import *
#from pygame import *
import pygame

class Wall(Collider):

    def __init__(self,surface ,name, pos, boundary):
        visible = True
        self.visible = visible
        self.width = boundary.width
        self.height = boundary.height
        Collider.__init__(self,surface ,name ,pos, boundary)

    def draw(self):
        #position = translation(self.pos,np.matrix([int(self.surface.get_width()/2),int(self.surface.get_height()/2),0]))
        #pygame.draw.line(self.surface,[0,0,0] , [position.item(0), position.item(1) ], end_line_draw ,3)
        rect(self.surface, color, rect)
        return True
