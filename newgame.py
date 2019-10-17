#!/usr/bin/env python3
import pygame

from pygame import *
import os.path

class robot(pygame.sprite.Sprite):

    def __init__(self, color, width, height):
         pygame.sprite.Sprite.__init__(self)
         self.image = pygame.Surface([width, height])
         self.image.fill(color)
         self.rect = self.image.get_rect()



def main():
    # initialize the pygame module
    print (os.getcwd())
    if not pygame.image.get_extended():
        raise SystemExit("Sorry, extended image module required")

    turtlebot = robot([0,0,0],200,200)


    print (turtlebot)
    pygame.init()
    # load and set the logo

    # create a surface on screen that has the size of 240 x 180
    screen_width = 240
    screen_height = 180
    screen = pygame.display.set_mode((240,180))

    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    bgd_image = pygame.image.load("background.png")
    image = pygame.image.load("01_image.png")

    bgd_image = bgd_image.convert()

    bgd_image.set_alpha(255)
    image.set_alpha(255)
    logo.set_alpha(255)

    # blit image(s) to screen
    screen.fill((255,0,0))
    screen.blit(bgd_image,(50,50))

    screen.blit(logo, (50,50))

    xpos =110
    ypos = 50
    screen.blit(image, (xpos,ypos))
    # define a variable to control the main loop
    running = True

    step_x =1
    step_y =1

    pygame.display.flip()

    # main loop
    while running:

        # check if the smiley is still on screen, if not change direction
        if xpos>screen_width-64 or xpos<0:
            step_x = -step_x
        if ypos>screen_height-64 or ypos<0:
            step_y = -step_y
        # update the position of the smiley
        xpos += step_x # move it to the right
        ypos += step_y # move it down

        # first erase the screen
        #(just blit the background over anything on screen)
        screen.blit(bgd_image, (0,0))
        # now blit the smiley on screen
        screen.blit(image, (xpos, ypos))

        turtlebot.update(screen)
        # and update the screen (don't forget that!)
        pygame.display.flip()

        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.MOUSEBUTTONDOWN:
                print (event)

            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False

        pygame.time.delay(10)


#call the "main" function if running this script
if __name__ == '__main__': main()
