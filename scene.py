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
    screen_width = 640
    screen_height = 480

    surface = pygame.display.set_mode((screen_width,screen_height))
    running = True
    center1 = screen_width/2
    center2 = screen_height/2
    robot1 = DDR(surface,'popo',[0,0,0],20,[0,255,255])
    robot2 = DDR(surface,'popo',[50,20,0],20,[0,155,155])

    while running:

        print (robot1.getPos())
        robot1.draw()
        robot2.draw()
        pygame.display.flip()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (event)

            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

    return 1
#call the "main" function if running this script
if __name__ == '__main__': main()
