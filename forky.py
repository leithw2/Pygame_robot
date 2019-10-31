#!/usr/bin/env python3
import pygame
import numpy as np

from pygame import *
from mate_funcs import *
import os.path

SCREENRECT     = Rect(0, 0, 640, 480)
l1= 150
l2= 100

class vector_coordinate():

    def __init__(self,screen , color, init, end):
        self.screen = screen
        self.init = init
        self.end = end
        self.color = color

        self.endRelative = [end[0]+init[0],end[1]+init[1]]

    def set_center(self,vec):
        self.center

    def get_center(self):
        return self.center

    def draw(self):
        init2 = [self.init[0] + self.screen.get_width()/2, self.init[1] + self.screen.get_height()/2]
        end2 = [self.end[0] + self.screen.get_width()/2, self.screen.get_height()/2+ self.end[1]]
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

    dir = 0
    dir2 = 0
    dir3 = 0

    if not pygame.image.get_extended():
        raise SystemExit("Sorry, extended image module required")

    #option = int(input("option 0 = demo; option 1 = manual "))
    option = 0
    pygame.init()

    # create a surface on screen that has the size of 240 x 180
    screen_width = 640
    screen_height = 480

    screen = pygame.display.set_mode((screen_width,screen_height))

    vec  = vector_coordinate(screen, [0,0,255], [0,0], [0,0])
    base = vector_coordinate(screen, [0,0,255], [0,0], [0,50])
    body = vector_coordinate(screen, [0,0,255], [0,0], [0,50])
    

    vec2 = vector_coordinate(screen, [0,255,0], [0,0], [0,0])

    vec3 = vector_coordinate(screen, [255,0,0], [0,0], [0,0])

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
        dir += keystate[K_RIGHT] - keystate[K_LEFT]
        dir2 += keystate[K_DOWN] - keystate[K_UP]
        dir3 += keystate[K_a]     - keystate[K_d]

        #vec.set_end(deg_to_Rect([l1,dir*.01]))

        mat = MatRotZ((dir*np.pi)/180).dot(MatTra([100,0,0,1]))
        mat2 = MatRotZ((dir2*np.pi)/180).dot(MatTra([100,0,0,1]))
        mat3 = MatRotZ((dir3*np.pi)/180).dot(MatTra([100,0,0,1]))

        vectest = np.matrix([0,0,0,1])
        endpos = mat.dot(np.transpose(vectest))
        endpos2 = mat.dot(mat2).dot(np.transpose(vectest))
        endpos3 = mat.dot(mat2).dot(mat3).dot(np.transpose(vectest))
        print (endpos)

        vec.set_end(endpos)
        vec2.set_init(endpos)
        vec2.set_end(endpos2)
        vec3.set_init(endpos2)
        vec3.set_end(endpos3)

        coord = 100
        pygame.draw.line(screen,[255,255,255] ,[screen_width/2,screen_height/2-coord],[screen_width/2,screen_height/2+coord] ,2)
        pygame.draw.line(screen,[255,255,255] ,[screen_width/2-coord,screen_height/2],[screen_width/2+coord,screen_height/2] ,2)

        vec.draw()
        vec2.draw()
        vec3.draw()


        vec1Init = font.render("Init:" +str(vec.get_init()), True, [0,0,255])
        vec1End = font.render("End: "+ str(vec.get_end()), True, [0,0,255])
        vec1Mag = font.render("Magnitude: " + str(vec.get_mag()), True, [0,0,255])
        #vec1Angle = font.render("angle: " + str(vec.get_angle()), True, [0,0,255])

        textRect1 = vec1Init.get_rect()
        textRect2 = vec1End.get_rect().move([0,20])
        textRect3 = vec1Mag.get_rect().move([0,40])
        #textRect4 = vec1Angle.get_rect().move([0,60])


        screen.blit(vec1Init, textRect1)
        screen.blit(vec1End, textRect2)
        screen.blit(vec1Mag, textRect3)
        #screen.blit(vec1Angle, textRect4)



        vec2Init = font.render("Init:" +str(vec2.get_init()), True, [0,255,0])
        #vec2End = font.render("End: " +str(vec2.get_endRelative()), True, [0,255,0])
        vec2Mag = font.render("Magnitude: " +str(vec2.get_mag()), True, [0,255,0])
        #vec2Angle = font.render("angle: " + str(vec2.get_angRelative()), True, [0,255,0])

        textRect21 = vec2Init.get_rect().move([0,100])
        #textRect22 = vec2End.get_rect().move([0,120])
        textRect23 = vec2Mag.get_rect().move([0,140])
        #textRect24 = vec2Angle.get_rect().move([0,160])


        screen.blit(vec2Init, textRect21)
        #screen.blit(vec2End, textRect22)
        screen.blit(vec2Mag, textRect23)
        #screen.blit(vec2Angle, textRect24)

        #print (str(vec2.get_end()))
        # and update the screen (don't forget that!)
        pygame.display.flip()
        pygame.time.delay(10)

#call the "main" function if running this script
if __name__ == '__main__': main()
