#!/usr/bin/env python3
import pygame
import numpy as np
from pygame import *
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from mate_funcs import *
from robot import *
from Bug import *
from BugTan import *

def main():
    pygame.init()

    screen_width = 700
    screen_height = 600

    surface = pygame.display.set_mode((screen_width,screen_height))
    running = True
    center1 = screen_width/2
    center2 = screen_height/2

    mousePoint = []
    optionx = -0
    optiony = -280
    optionA = -0 * np.pi / 180


    robot1 = []

    qGoal = Point(surface,np.matrix([-50,-150,0,1]))

    rect00 = pygame.Rect(00/2,-250/2,100,50)
    rect01 = pygame.Rect(200/2,-450/2,50,150)
    rect02 = pygame.Rect(-300/2,150/2,300,50)

    outOfBounds1 = pygame.Rect(-screen_width/2 ,-screen_height/2,screen_width,10)
    outOfBounds2 = pygame.Rect(-screen_width/2 ,screen_height/2-10,screen_width,10)
    outOfBounds3 = pygame.Rect(-screen_width/2 ,-screen_height/2,10 ,screen_height)
    outOfBounds4 = pygame.Rect(screen_width/2 -10 ,-screen_height/2,10 ,screen_height)

    colliders =[]
    colliders.append(rect00)
    colliders.append(rect01)
    colliders.append(rect02)
    #colliders.append(outOfBounds1)
    #colliders.append(outOfBounds2)
    #colliders.append(outOfBounds3)
    #colliders.append(outOfBounds4)

    Lidar = []
    LidarGroup = []

    bugControl = []

    while running:

        keystate = pygame.key.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                newtarget = np.matrix([-screen_width/2 + event.pos[0],-(screen_height/2 - event.pos[1]),0,1])

                # if robot1 !=[]:
                #     qGoal.setPos(newtarget)
                #     bugControl = controlBug2(robot1, qGoal, Lidar)
                #
                # else:
                #     robot1 = DDR(surface,'Robo1',[newtarget.item(0),newtarget.item(1) ],15,optionA ,[0  ,255,255])
                #     Lidar = LidarL(surface, "sensor", colliders, robot1, 45)

                if robot1 !=[]:
                    qGoal.setPos(newtarget)
                    bugControl = controlBugTan(robot1, qGoal, Lidar)

                else:
                    robot1 = DDR(surface,'Robo1',[newtarget.item(0),newtarget.item(1) ],15,optionA ,[0  ,255,255])
                    Lidar = LidarL(surface, "sensor", colliders, robot1, 9)

            if event.type == pygame.QUIT:
                running = False

        surface.fill((0,0,0))

        if robot1 != []:
            robot1.draw()

        for collider in colliders:
            pygame.draw.rect(surface, [255,255,255],  Rect(collider.left + center1, collider.top + center2, collider.width, collider.height),2)

        if bugControl != []:
            robot1.draw()
            qGoal.draw()
            bugControl.update()
            bugControl.drawSteps(surface)

        pygame.display.flip()
        pygame.time.delay(0)
    return 1
#call the "main" function if running this script
if __name__ == '__main__': main()
