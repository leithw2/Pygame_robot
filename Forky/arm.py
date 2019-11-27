#!/usr/bin/env python3

import pygame
import numpy as np
from pygame import *
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from mate_funcs import *

SCREENRECT     = Rect(0, 0, 640, 480)
l1= 150
l2= 100

class vector_coordinate():

    def __init__(self,screen , color, init, end, name):

        self.screen = screen
        self.init = [init[0],-init[1],0,1]
        self.end = [end[0],-end[1],0,1]
        self.color = color
        self.name = name

        self.target = 0
        self.direction = 1
        self.ang = 0
        self.range = [0,0]

        self.ouch = False

        self.surface_mask = pygame.Surface((self.screen.get_width(),self.screen.get_height()))
        self.surface_mask.set_colorkey((255,255,255))
        self.surface_mask.fill((255,255,255))
        self.mask = pygame.mask.from_surface(self.surface_mask)

        self.endRelative = [end[0]+init[0],end[1]+init[1]]


    def get_ang(self):
        return self.ang

    def set_ang(self, ang):
        self.ang = ang

    def get_target(self):
        return self.target

    def set_target(self, target):
        self.target = target

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction

    def set_center(self,vec):
        self.center

    def get_center(self):
        return self.center

    def draw(self):
        init2 = [self.init[0] + self.screen.get_width()/2,self.screen.get_height()/2 - self.init[1]]
        end2 = [self.end[0] + self.screen.get_width()/2, self.screen.get_height()/2 - self.end[1]]
        pygame.draw.line(self.screen,self.color ,init2,end2 ,5)

        self.surface_mask.fill((255,255,255))
        pygame.draw.line(self.surface_mask,self.color ,init2,end2 ,5)
        self.mask = pygame.mask.from_surface(self.surface_mask)

    def set_init(self, vec):
        self.init = vec

    def get_init(self):
        return self.init

    def set_end(self, vec):
        self.end = vec

    def get_end(self):
        return self.end

    def get_mag(self):
        return magVec(self.get_end())

    def set_ouch(self, ouch):
        self.ouch = ouch

    def get_ouch(self):
        return self.ouch

    def get_range(self):
        return self.range

    def set_range(self,vec):
        self.range = [vec[0], vec[1]]

    def get_name(self):
        return self.name

class scene():
    def __init__(self):
        # initialize the pygame module
        global l1
        global l2
        self.running = True

        self.dir = 0

        #option = int(input("option 0 = demo; option 1 = manual "))
        option = 0
        pygame.init()

        # create a surface on screen that has the size of 240 x 180
        self.screen_width = 640
        self.screen_height = 480

        self.screen = pygame.display.set_mode((self.screen_width,self.screen_height))
        #self.screen = pygame.display.set_mode()
        self.screen.fill((255,255,255))
        self.screen.set_colorkey((255,255,255))

        self.base     = vector_coordinate(self.screen, [0,0,255], [0,0], [0,50],"base")
        self.body     = vector_coordinate(self.screen, [0,255,255], [0,50], [0,100], "body")
        self.neck     = vector_coordinate(self.screen, [255,0,0], [0, 0], [0,30],"head")

        self.vectors = []
        self.vectors.append(self.base)

        self.vectors.append(self.body)

        self.vectors.append(self.neck)

        #self.rect = pygame.rect()
        self.vectors = []

        self.base.set_ang(0)
        self.base.set_target(0)

        self.body.set_ang(0)
        self.body.set_target(0)

        self.neck.set_ang(0)


######################################
        ####
        self.base.set_range([-170,170])
        self.body.set_range([-170,170])
        self.neck.set_range([-170,170])

#######################################
        self.vectors.append(self.base)

        self.vectors.append(self.body)

        self.vectors.append(self.neck)

        pygame.display.set_caption("Forky Robot")

        option1 = int(input("Angulo 1 : "))
        option2 = int(input("Angulo 2 : "))
        option3 = int(input("Angulo 3 : "))

        self.base.set_target(-option1)
        self.body.set_target(-option2)
        self.neck.set_target(-option3)

        self.font = pygame.font.Font('freesansbold.ttf', 14)
        # main loop

    def draw(self):

        #pygame.display.flip()
        self.screen.fill((0,0,0))
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (event)

            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                self.running = False
            #print(event.type)

        for vec in self.vectors:

            if True:

                if vec.get_target() >= vec.get_ang():

                    vec.set_direction(1)

                    if vec.get_ang() < vec.get_target() * vec.get_direction():
                        vec.set_ang(vec.get_ang() + vec.get_direction())
                else:

                    vec.set_direction(-1)

                    if vec.get_ang() > -vec.get_target() * vec.get_direction():
                        vec.set_ang(vec.get_ang() + vec.get_direction())


        self.keystate = pygame.key.get_pressed()

        #self.base.set_ang(self.base.get_ang()           + self.keystate[K_RIGHT] - self.keystate[K_LEFT])
        #self.body.set_ang(self.body.get_ang()           + self.keystate[K_UP] - self.keystate[K_DOWN])
        #self.neck.set_ang(self.neck.get_ang()           + self.keystate[K_a] - self.keystate[K_d])

        mat  = MatRotZ((self.base.get_ang()*np.pi)/180).dot(MatTra([50,0,0,1]))
        mat1 = MatRotZ((self.body.get_ang()*np.pi)/180).dot(MatTra([50,0,0,1]))


        mat1_3 = MatRotZ((self.neck.get_ang()*np.pi)/180).dot(MatTra([50,0,0,1]))

        vectest = np.matrix([0,0,0,1])

        endpos = mat.dot(np.transpose(vectest))
        endpos2 = mat.dot(mat1).dot(np.transpose(vectest))

        neck_end = mat.dot(mat1).dot(mat1_3).dot(np.transpose(vectest))

        self.base.set_init(np.transpose(vectest))
        self.base.set_end(endpos)
        self.body.set_init(endpos)
        self.body.set_end(endpos2)

        self.neck.set_init(endpos2)
        self.neck.set_end(neck_end)

        coord = 100
        pygame.draw.line(self.screen,[255,255,255] ,[self.screen_width/2,self.screen_height/2-coord],[self.screen_width/2,self.screen_height/2+coord] ,2)
        pygame.draw.line(self.screen,[255,255,255] ,[self.screen_width/2-coord,self.screen_height/2],[self.screen_width/2+coord,self.screen_height/2] ,2)

        for vec in self.vectors:
            vec.draw()

        fonts = self.font.render("End point : " + str(vec.get_end().item(0)) + " " +str(vec.get_end().item(1)), True, [0,255,0])

        rectangle = fonts.get_rect().move([0,100])

        self.screen.blit(fonts, rectangle)

        pygame.display.flip()
        pygame.time.delay(5)
        #self.dir += 1
        #print(self.dir)

    def get_width(self):
        return self.screen_width

    def get_height(self):
        return self.screen_height

    def get_surface(self):
        return self.screen

    #call the "main" function if running this script
if __name__ == '__main__':
    sc=scene()
    while sc.running:
        sc.draw()
        pass
