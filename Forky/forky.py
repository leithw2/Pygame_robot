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
        self.forearmR = vector_coordinate(self.screen, [0,0,255], [0,50], [0,100],"forearmR")
        self.armR     = vector_coordinate(self.screen, [0,255,0], [0,50], [0,100],"armR")
        self.forearmL = vector_coordinate(self.screen, [0,0,255], [0,50], [0,100],"forearmL")
        self.armL     = vector_coordinate(self.screen, [0,255,0], [0,50], [0,100],"armL")
        #handL    = vector_coordinate(screen, [255,0,0], [0,50], [0,100])
        #handR    = vector_coordinate(screen, [255,0,0], [0,50], [0,100])
        self.neck     = vector_coordinate(self.screen, [255,0,0], [0, 0], [0,30],"head")

        self.headR1   = vector_coordinate(self.screen, [255,0,0], [0, 0], [0,30],"head")
        self.headR2   = vector_coordinate(self.screen, [255,0,0], [0, 0], [0,30],"head")
        self.headL1   = vector_coordinate(self.screen, [255,0,0], [0, 0], [0,30],"head")
        self.headL2   = vector_coordinate(self.screen, [255,0,0], [0, 0], [0,30],"head")

        self.head   = vector_coordinate(self.screen, [255,0,0], [0, 0], [0,30],"head")

        #self.rect = pygame.rect()
        self.vectors = []


        self.base.set_ang(0)
        self.base.set_target(0)

        self.body.set_ang(0)
        self.body.set_target(0)

        self.forearmR.set_ang(90)
        self.forearmR.set_target(80)
        self.armR.set_ang(-90)
        self.armR.set_target(-90)

        self.forearmL.set_ang(-90)
        self.forearmL.set_target(-90)
        self.armL.set_ang(90)
        self.armL.set_target(90)

        self.neck.set_ang(-90)

        self.headR1.set_ang(-90)
        self.headR2.set_ang(-90)
        self.headL1.set_ang(-90)
        self.headL2.set_ang(-90)

        self.head.set_ang(-90)

######################################
        ####
        self.base.set_range([-170,170])
        self.body.set_range([-170,170])

        self.forearmR.set_range([-170,170])
        self.armR.set_range([-170,170])

        self.forearmL.set_range([-170,170])
        self.armL.set_range([-170,170])

        self.neck.set_range([-170,170])

        self.headR1.set_range([-170,170])
        self.headR2.set_range([-170,170])
        self.headL1.set_range([-170,170])
        self.headL2.set_range([-170,170])

        self.head.set_range([-170,170])
#######################################
        self.vectors.append(self.base)

        self.vectors.append(self.body)

        self.vectors.append(self.forearmR)
        self.vectors.append(self.armR)
        self.vectors.append(self.forearmL)
        self.vectors.append(self.armL)


        self.vectors.append(self.neck)

        self.vectors.append(self.headR1)
        self.vectors.append(self.headR2)
        self.vectors.append(self.headL1)
        self.vectors.append(self.headL2)

        self.vectors.append(self.head)


        pygame.display.set_caption("Forky Robot")

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

        self.keystate = pygame.key.get_pressed()

        #self.dir  += self.keystate[K_RIGHT] - self.keystate[K_LEFT]

        #handle player input
        '''
        self.dir  += self.keystate[K_RIGHT] - self.keystate[K_LEFT]
        self.dir2 += self.keystate[K_DOWN]  - self.keystate[K_UP]
        self.dir3 += self.keystate[K_a]     - self.keystate[K_d]
        self.dir4 += self.keystate[K_w]     - self.keystate[K_s]
        self.dir5 += self.keystate[K_q]     - self.keystate[K_e]
        self.dir6 += self.keystate[K_i]     - self.keystate[K_k]
        self.dir7 += self.keystate[K_j]     - self.keystate[K_l]
        '''

        for vec in self.vectors:

            if not vec.get_ouch():

                if vec.get_target() >= vec.get_ang():
                    vec.set_direction(1)
                else:
                    vec.set_direction(-1)

                if vec.get_ang() < vec.get_target() * vec.get_direction():
                    vec.set_ang(vec.get_ang() + vec.get_direction())




        mat  = MatRotZ((-90*np.pi)/180).dot(MatTra([50,0,0,1]))
        mat1 = MatRotZ((self.body.get_ang()*np.pi)/180).dot(MatTra([50,0,0,1]))

        mat1_1     = MatRotZ((self.forearmR.get_ang()*np.pi)/180).dot(MatTra([50,0,0,1]))
        mat1_1_1   = MatRotZ((self.armR.get_ang()*np.pi)/180).dot(MatTra([50,0,0,1]))
       #mat1_1_1_1 = MatRotZ((dir6*np.pi)/180).dot(MatTra([30,0,0,1]))

        mat1_2     = MatRotZ((self.forearmL.get_ang()*np.pi)/180).dot(MatTra([50,0,0,1]))
        mat1_2_1   = MatRotZ((self.armL.get_ang()*np.pi)/180).dot(MatTra([50,0,0,1]))
       #mat1_2_1_1 = MatRotZ((dir7*np.pi)/180).dot(MatTra([30,0,0,1]))

        mat1_3 = MatRotZ((0*np.pi)/180).dot(MatTra([50,0,0,1]))
        mat1_3_R1 = MatRotZ((-90*np.pi)/180).dot(MatTra([30,0,0,1]))
        mat1_3_R2 = MatRotZ((90*np.pi)/180).dot(MatTra([30,0,0,1]))
        mat1_3_L1 = MatRotZ((90*np.pi)/180).dot(MatTra([30,0,0,1]))
        mat1_3_L2 = MatRotZ((-90*np.pi)/180).dot(MatTra([30,0,0,1]))
        mat1_3_H = MatRotZ((np.pi)/180).dot(MatTra([30,0,0,1]))

        vectest = np.matrix([0,0,0,1])

        endpos = mat.dot(np.transpose(vectest))
        endpos2 = mat.dot(mat1).dot(np.transpose(vectest))

        forearm_R_end = mat.dot(mat1).dot(mat1_1).dot(np.transpose(vectest))
        arm_R_end = mat.dot(mat1).dot(mat1_1).dot(mat1_1_1).dot(np.transpose(vectest))
        #hand_R_end = mat.dot(mat1).dot(mat1_1).dot(mat1_1_1).dot(mat1_1_1_1).dot(np.transpose(vectest))

        forearm_L_end = mat.dot(mat1).dot(mat1_2).dot(np.transpose(vectest))
        arm_L_end = mat.dot(mat1).dot(mat1_2).dot(mat1_2_1).dot(np.transpose(vectest))
        #hand_L_end = mat.dot(mat1).dot(mat1_2).dot(mat1_2_1).dot(mat1_2_1_1).dot(np.transpose(vectest))

        neck_end = mat.dot(mat1).dot(mat1_3).dot(np.transpose(vectest))
        headR1_end = mat.dot(mat1).dot(mat1_3).dot(mat1_3_R1).dot(np.transpose(vectest))
        headR2_end = mat.dot(mat1).dot(mat1_3).dot(mat1_3_R1).dot(mat1_3_R2).dot(np.transpose(vectest))
        headL1_end = mat.dot(mat1).dot(mat1_3).dot(mat1_3_L1).dot(np.transpose(vectest))
        headL2_end = mat.dot(mat1).dot(mat1_3).dot(mat1_3_L1).dot(mat1_3_L2).dot(np.transpose(vectest))

        head_end = mat.dot(mat1).dot(mat1_3).dot(mat1_3_H).dot(np.transpose(vectest))

        self.base.set_init(np.transpose(vectest))
        self.base.set_end(endpos)
        self.body.set_init(endpos)
        self.body.set_end(endpos2)

        self.forearmR.set_init(endpos2)
        self.forearmR.set_end(forearm_R_end)
        self.armR.set_init(forearm_R_end)
        self.armR.set_end(arm_R_end)
        #handR.set_init(arm_R_end)
        #handR.set_end(hand_R_end)

        self.forearmL.set_init(endpos2)
        self.forearmL.set_end(forearm_L_end)
        self.armL.set_init(forearm_L_end)
        self.armL.set_end(arm_L_end)
        #handL.set_init(arm_L_end)
        #handL.set_end(hand_L_end)

        self.neck.set_init(endpos2)
        self.neck.set_end(neck_end)

        self.headR1.set_init(neck_end)
        self.headR1.set_end(headR1_end)

        self.headR2.set_init(headR1_end)
        self.headR2.set_end(headR2_end)

        self.headL1.set_init(neck_end)
        self.headL1.set_end(headL1_end)

        self.headL2.set_init(headL1_end)
        self.headL2.set_end(headL2_end)

        self.head.set_init(neck_end)
        self.head.set_end(head_end)

        coord = 100
        pygame.draw.line(self.screen,[255,255,255] ,[self.screen_width/2,self.screen_height/2-coord],[self.screen_width/2,self.screen_height/2+coord] ,2)
        pygame.draw.line(self.screen,[255,255,255] ,[self.screen_width/2-coord,self.screen_height/2],[self.screen_width/2+coord,self.screen_height/2] ,2)


        for vec in self.vectors:
            if vec.get_end()[1] <= 0:
                for vec2 in self.vectors:
                    vec2.set_ouch(True)
                print ("ouch!")
                print (vec.get_ouch())

            if vec.get_range()[0] >= vec.get_ang() or vec.get_range()[1] <= vec.get_ang():
                for vec2 in self.vectors:
                    vec2.set_ouch(True)
                print ("ouch! mi articulacion " + vec.get_name())
                print (vec.get_ouch())
                print (vec.get_ang())
                print (vec.get_range())

                #vec.set_target(vec.get_ang())



        for vec in self.vectors:
            vec.draw()

        x=0
        #for vec in self.vectors:
        #    print (vec.mask.overlap(vec.mask,(0,0)))

        if self.armR.mask.overlap(self.armL.mask,(0,0)) != None:
            x+=1

        if self.armR.mask.overlap(self.forearmL.mask,(0,0)) != None:
            x+=1

        if self.armR.mask.overlap(self.head.mask,(0,0)) != None:
            x+=1

        if self.armR.mask.overlap(self.headL1.mask,(0,0)) != None:
            x+=1

        if self.armR.mask.overlap(self.headL2.mask,(0,0)) != None:
            x+=1

        if self.armR.mask.overlap(self.headR2.mask,(0,0)) != None:
            x+=1

        if self.armR.mask.overlap(self.headR2.mask,(0,0)) != None:
            x+=1

        if x > 0:
            print ("ouch!")




        # and update the screen (don't forget that!)
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
