#!/usr/bin/env python3
import numpy as np
import pygame

class Model():

    def __init__(self,surface ,name='' ,pos=[0.0 ,0.0, 0.0 ]):
        pos = np.matrix([pos[0], pos[1], pos[2], 1])
        self.name = name
        self.pos = pos
        self.surface = surface

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

class Collider(Model):

    def __init__(self,surface ,name="" ,pos=[0.0 ,0.0, 0.0 ], boundary = pygame.Rect(0, 0, 0, 0)):
        self.boundary = boundary
        Model.__init__(self,surface ,name ,pos)

    def check_Collision(self, collider):
        return False
