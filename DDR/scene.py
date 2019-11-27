#!/usr/bin/env python3
import pygame
import numpy as np
from pygame import *
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from mate_funcs import *
from robot import *
from Bug1 import *

def main():
    pygame.init()

    screen_width = 700
    screen_height = 600

    surface = pygame.display.set_mode((screen_width,screen_height))
    running = True
    center1 = screen_width/2
    center2 = screen_height/2

    #optionx = int(input("x init = "))
    #optiony = int(input("y init = "))
    #optionA = int(input("y angle = "))
    optionx = -0
    optiony = -280
    optionA = -0 * np.pi / 180


    robot1 = DDR(surface,'Robo1',[optionx ,-optiony],15,optionA ,[0  ,255,255])

    qGoal = Point(surface,np.matrix([200,-150,0,1]))

    rect00 = pygame.Rect(00/2,-250/2,100,50)
    rect01 = pygame.Rect(200/2,-450/2,50,150)

    rect02 = pygame.Rect(-200/2,150/2,250,50)

    colliders =[]
    colliders.append(rect00)
    colliders.append(rect01)
    colliders.append(rect02)
    #colliders.append(rect03)
    #colliders.append(rect04)
    #colliders.append(rect05)

    Lidar = LidarL(surface, "sensor", colliders, robot1, 45)
    LidarGroup = []

    bugControl = controlBug2(robot1, qGoal, Lidar)


    #print(robot1.getPos())
    #robot2 = DDR(surface,'Robo2',[50,50,0 ],30,(np.pi/2),[0  ,155,155])
    dir  = 0
    dir2 = 0
    dir3 = 0
    dir4 = 0

    #optionx = int(input("x target = "))
    #optiony = int(input("y target = "))
    #optionA = int(input("y target_angle = "))

    option2x = 101
    option2y = 150
    option2A = 170

    #robot1.moveto(np.matrix([option2x,-option2y,0,1]),option2A * np.pi / 180)
    #robot1.setStop(False)
    while running:

        keystate = pygame.key.get_pressed()

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:

                newtarget = np.matrix([-screen_width/2 + event.pos[0],-(screen_height/2 - event.pos[1]),0,1])
                robot1.moveto(newtarget,0)
                print (newtarget)

            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            #print(event.type)

        '''
        dir  += keystate[K_RIGHT] - keystate[K_LEFT]
        dir2 += keystate[K_DOWN]  - keystate[K_UP]
        dir3 += keystate[K_a]     - keystate[K_d]
        dir4 += keystate[K_w]     - keystate[K_s]
        '''

        #robot1.update()

        surface.fill((0,0,0))
        #Lidar.update()
        robot1.draw()
        qGoal.draw()

        for collider in colliders:
            pygame.draw.rect(surface, [255,255,255],  Rect(collider.left + center1, collider.top + center2, collider.width, collider.height),2)
        bugControl.update()

        bugControl.drawSteps(surface)

        pygame.display.flip()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of etype QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (event)

            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.time.delay(0)
    return 1
#call the "main" function if running this script
if __name__ == '__main__': main()
