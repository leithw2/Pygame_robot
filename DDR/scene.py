#!/usr/bin/env python3
import pygame
import numpy as np
from pygame import *
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )
from mate_funcs import *
from robot import *

def main():
    pygame.init()

    screen_width = 1000
    screen_height = 800

    surface = pygame.display.set_mode((screen_width,screen_height))
    running = True
    center1 = screen_width/2
    center2 = screen_height/2

    optionx = int(input("x init = "))
    optiony = int(input("y init = "))

    robot1 = DDR(surface,'Robo1',[optionx ,optiony ,0 ],30,0        ,[0  ,255,255])
    #robot2 = DDR(surface,'Robo2',[50,50,0 ],30,(np.pi/2),[0  ,155,155])

    dir  = 0
    dir2 = 0
    dir3 = 0
    dir4 = 0

    optionx = int(input("x target = "))
    optiony = int(input("y target = "))

    robot1.set_target_point([optionx,-optiony])

    if robot1.target_point[0] >= robot1.getPos().item(0,0):
        slope = line_slop([robot1.getPos().item(0,0),robot1.getPos().item(0,1)],robot1.target_point)
        angle = np.arctan(slope)
    else:
        slope = + line_slop([robot1.getPos().item(0,0),robot1.getPos().item(0,1)],robot1.target_point)
        angle = - np.pi + np.arctan(slope)


    robot1.set_target_Angle(angle)
    robot1.set_target_pos(np.matrix([[robot1.target_point[0],robot1.target_point[1],0,1]]))
    done = False
    done2 = False

    while running:

        keystate = pygame.key.get_pressed()

        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:

                newtarget = [-screen_width/2 + event.pos[0],-(screen_height/2 - event.pos[1])]
                robot1.set_target_point(newtarget)
                if robot1.target_point[0] >= robot1.getPos().item(0,0):
                    slope = line_slop([robot1.getPos().item(0,0),robot1.getPos().item(0,1)],robot1.target_point)
                    angle = np.arctan(slope)
                else:
                    slope = + line_slop([robot1.getPos().item(0,0),robot1.getPos().item(0,1)],robot1.target_point)
                    angle = - np.pi + np.arctan(slope)

                robot1.set_target_Angle(angle)
                robot1.set_target_pos(np.matrix([[robot1.target_point[0],robot1.target_point[1],0,1]]))
                done = False
                done2 = False

                print (newtarget)
            if event.type == pygame.K_RIGHT:
                print(aaaaaaaaaa)

            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                self.running = False
            #print(event.type)


        if not done:

            if robot1.get_target_Angle() >= robot1.getAngle() :

                robot1.set_dir_ang(1)

                if robot1.getAngle() < robot1.get_target_Angle() * robot1.get_dir_ang():
                    robot1.rotateq(.5*robot1.get_dir_ang() * np.pi/180)
            else:

                robot1.set_dir_ang(-1)

                if robot1.getAngle() > -robot1.get_target_Angle() * robot1.get_dir_ang():
                    robot1.rotateq(.5*robot1.get_dir_ang() * np.pi/180)

            if abs(robot1.get_target_Angle()) - abs(robot1.getAngle()) < 0.001:

                done = True

        #print (robot1.get_target_pos())
        #print (robot1.getPos())
        #print (done, done2)


        if done and not done2:

            targetx = robot1.get_target_pos().item(0,0)
            targety = robot1.get_target_pos().item(0,1)

            posx = robot1.getPos().item(0,0)
            posy = robot1.getPos().item(0,1)

            robot1.forward(robot1.get_dir()*.1)
            print (dis_Between([posx,posy],[targetx,targety]))
            if  dis_Between([posx,posy],[targetx,targety]) < 5:

                done2 = True
            if not done2:
                robot1.forward(robot1.get_dir())



        '''
        dir  += keystate[K_RIGHT] - keystate[K_LEFT]
        dir2 += keystate[K_DOWN]  - keystate[K_UP]
        dir3 += keystate[K_a]     - keystate[K_d]
        dir4 += keystate[K_w]     - keystate[K_s]
        '''
        surface.fill((200,200,200))
        robot1.draw()
        #robot2.draw()
        pygame.display.flip()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of etype QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (event)

            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
        pygame.time.delay(10)
    return 1
#call the "main" function if running this script
if __name__ == '__main__': main()
