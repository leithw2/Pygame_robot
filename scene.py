#!/usr/bin/env python3
import pygame
import numpy as np
from mate_funcs import *

from pygame import *
from mate_funcs import *
from robot import *
import os.path

def main():
    pygame.init()

    # create a surface on screen that has the size of
    #screen_width = 1280
    #screen_height = 720
    screen_width = 600
    screen_height = 400

    surface = pygame.display.set_mode((screen_width,screen_height))
    running = True
    center1 = screen_width/2
    center2 = screen_height/2
    robot1 = DDR(surface,'Robo1',[0 ,0 ,0 ],30,0        ,[0  ,255,255])
    robot2 = DDR(surface,'Robo2',[50,50,0 ],30,(np.pi/2),[0  ,155,155])

    dir  = 0
    dir2 = 0
    dir3 = 0
    dir4 = 0

    while running:

        keystate = pygame.key.get_pressed()

        dir  += keystate[K_RIGHT] - keystate[K_LEFT]
        dir2 += keystate[K_DOWN]  - keystate[K_UP]
        dir3 += keystate[K_a]     - keystate[K_d]
        dir4 += keystate[K_w]     - keystate[K_s]

        if dir != 0 or dir2 != 0 or dir3 != 0 or dir4 != 0:

            robot1.move([dir,dir2,0])
            robot1.rotate(dir3*.08 )
            robot2.move([dir,dir2,0])
            robot2.rotate(dir3*.08 )
            robot1.forward(dir4)
            robot2.forward(dir4)

            dir  = 0
            dir2 = 0
            dir3 = 0
            dir4 = 0

        surface.fill((200,200,200))
        robot1.draw()
        robot2.draw()
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
