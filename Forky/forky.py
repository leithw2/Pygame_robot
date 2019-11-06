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

    def __init__(self,screen , color, init, end):
        self.screen = screen
        self.init = [init[0],-init[1],0,1]
        self.end = [end[0],-end[1],0,1]
        self.color = color

        self.endRelative = [end[0]+init[0],end[1]+init[1]]

    def set_center(self,vec):
        self.center

    def get_center(self):
        return self.center

    def draw(self):
        init2 = [self.init[0] + self.screen.get_width()/2,self.screen.get_height()/2 - self.init[1]]
        end2 = [self.end[0] + self.screen.get_width()/2, self.screen.get_height()/2 - self.end[1]]
        pygame.draw.line(self.screen,self.color ,init2,end2 ,5)

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

def main():
    # initialize the pygame module
    global l1
    global l2

    dir  = 45
    dir2 = 0
    dir3 = -45
    dir4 = 0
    dir5 = 0
    dir6 = 0
    dir7 = 0

    if not pygame.image.get_extended():
        raise SystemExit("Sorry, extended image module required")

    #option = int(input("option 0 = demo; option 1 = manual "))
    option = 0
    pygame.init()

    # create a surface on screen that has the size of 240 x 180
    screen_width = 640
    screen_height = 480

    screen = pygame.display.set_mode((screen_width,screen_height))

    base     = vector_coordinate(screen, [0,0,255], [0,0], [0,50])
    body     = vector_coordinate(screen, [0,255,255], [0,50], [0,100])
    forearmR = vector_coordinate(screen, [0,0,255], [0,50], [0,100])
    armR     = vector_coordinate(screen, [0,255,0], [0,50], [0,100])
    forearmL = vector_coordinate(screen, [0,0,255], [0,50], [0,100])
    armL     = vector_coordinate(screen, [0,255,0], [0,50], [0,100])
    handL    = vector_coordinate(screen, [255,0,0], [0,50], [0,100])
    handR    = vector_coordinate(screen, [255,0,0], [0,50], [0,100])
    head     = vector_coordinate(screen, [255,0,0], [0,50], [0,100])


    pygame.display.set_caption("Forky Robot")

    xpos = 0
    ypos = 0
    running = True

    step_x =1
    step_y =1
    x=4
    y=4

    font = pygame.font.Font('freesansbold.ttf', 14)

    pygame.display.flip()
    speed1 = 0
    speed2 = 0
    actualAng1 =0
    actualAng2 =0

    # main loop
    while running:

        screen.fill((0,0,0))
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (event)

            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        keystate = pygame.key.get_pressed()

        #handle player input
        dir  += keystate[K_RIGHT] - keystate[K_LEFT]
        dir2 += keystate[K_DOWN]  - keystate[K_UP]
        dir3 += keystate[K_a]     - keystate[K_d]
        dir4 += keystate[K_w]     - keystate[K_s]
        dir5 += keystate[K_q]     - keystate[K_e]
        dir6 += keystate[K_i]     - keystate[K_k]
        dir7 += keystate[K_j]     - keystate[K_l]

        #vec.set_end(deg_to_Rect([l1,dir*.01]))

        mat  = MatRotZ((-90*np.pi)/180).dot(MatTra([50,0,0,1]))
        mat1 = MatRotZ((dir5*np.pi)/180).dot(MatTra([50,0,0,1]))

        mat1_1 = MatRotZ((dir*np.pi)/180).dot(MatTra([50,0,0,1]))
        mat1_1_1 = MatRotZ((dir2*np.pi)/180).dot(MatTra([50,0,0,1]))
        mat1_1_1_1 = MatRotZ((dir6*np.pi)/180).dot(MatTra([30,0,0,1]))

        mat1_2 = MatRotZ((dir3*np.pi)/180).dot(MatTra([50,0,0,1]))
        mat1_2_1 = MatRotZ((dir4*np.pi)/180).dot(MatTra([50,0,0,1]))
        mat1_2_1_1 = MatRotZ((dir7*np.pi)/180).dot(MatTra([30,0,0,1]))

        mat1_3 = MatRotZ((0*np.pi)/180).dot(MatTra([50,0,0,1]))

        vectest = np.matrix([0,0,0,1])

        endpos = mat.dot(np.transpose(vectest))
        endpos2 = mat.dot(mat1).dot(np.transpose(vectest))

        forearm_R_end = mat.dot(mat1).dot(mat1_1).dot(np.transpose(vectest))
        arm_R_end = mat.dot(mat1).dot(mat1_1).dot(mat1_1_1).dot(np.transpose(vectest))
        hand_R_end = mat.dot(mat1).dot(mat1_1).dot(mat1_1_1).dot(mat1_1_1_1).dot(np.transpose(vectest))

        forearm_L_end = mat.dot(mat1).dot(mat1_2).dot(np.transpose(vectest))
        arm_L_end = mat.dot(mat1).dot(mat1_2).dot(mat1_2_1).dot(np.transpose(vectest))
        hand_L_end = mat.dot(mat1).dot(mat1_2).dot(mat1_2_1).dot(mat1_2_1_1).dot(np.transpose(vectest))

        head_end = mat.dot(mat1).dot(mat1_3).dot(np.transpose(vectest))

        base.set_init(np.transpose(vectest))
        base.set_end(endpos)
        body.set_init(endpos)
        body.set_end(endpos2)

        forearmR.set_init(endpos2)
        forearmR.set_end(forearm_R_end)
        armR.set_init(forearm_R_end)
        armR.set_end(arm_R_end)
        handR.set_init(arm_R_end)
        handR.set_end(hand_R_end)

        forearmL.set_init(endpos2)
        forearmL.set_end(forearm_L_end)
        armL.set_init(forearm_L_end)
        armL.set_end(arm_L_end)
        handL.set_init(arm_L_end)
        handL.set_end(hand_L_end)

        head.set_init(endpos2)
        head.set_end(head_end)


        coord = 100
        pygame.draw.line(screen,[255,255,255] ,[screen_width/2,screen_height/2-coord],[screen_width/2,screen_height/2+coord] ,2)
        pygame.draw.line(screen,[255,255,255] ,[screen_width/2-coord,screen_height/2],[screen_width/2+coord,screen_height/2] ,2)


        base.draw()
        body.draw()

        forearmR.draw()
        armR.draw()
        handR.draw()

        forearmL.draw()
        armL.draw()
        handL.draw()

        head.draw()

        # and update the screen (don't forget that!)
        pygame.display.flip()
        pygame.time.delay(10)

#call the "main" function if running this script
if __name__ == '__main__': main()
