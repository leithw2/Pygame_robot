#!/usr/bin/env python3
import pygame

from pygame import *
import os.path

SCREENRECT     = Rect(0, 0, 640, 480)

class robot(pygame.sprite.Sprite):
    speed = 1
    posx=0
    posy=0

    def __init__(self, color, width, height, posx = 0, posy = 0):
         pygame.sprite.Sprite.__init__(self)
         self.image = pygame.Surface([width, height])
         self.image.fill(color)
         self.image = pygame.image.load("01_image.png")
         self.rect = self.image.get_rect()
         self.set_posx(posx)
         self.set_posy(posy)

    def move(self, dir,dir2):
        if dir: self.facing = dir
        self.rect.move_ip(dir*self.speed, dir2*self.speed)
        self.rect = self.rect.clamp(SCREENRECT)

    def set_posx(self,posx):
        self.rect.x = posx

    def set_posy(self,posy):
        self.rect.y = posy

    def get_posx(self):
        return self.rect.x

    def get_posy(self):
        return self.rect.y

def main():
    # initialize the pygame module
    print (os.getcwd())
    if not pygame.image.get_extended():
        raise SystemExit("Sorry, extended image module required")

    turtlebot  = robot([255,0,0], 20 ,20)
    turtlebot2 = robot([255,0,0] ,20 ,20 ,50 ,50 )

    enemy = robot([255,0,0] ,20 ,20 ,50 ,50 )

    # Initialize Game Groups
    robots = pygame.sprite.Group()

    enemys = pygame.sprite.Group()

    for carita in range(10):
        robot([255,0,0] ,20 ,20 ,carita*50 ,carita*50 ).add(robots)

    #robots.add(turtlebot)
    turtlebot.add(robots)
    turtlebot2.add(robots)

    enemy.add(enemys)

    pygame.init()

    # create a surface on screen that has the size of 240 x 180
    screen_width = 640
    screen_height = 480

    screen = pygame.display.set_mode((screen_width,screen_height))

    logo = pygame.image.load("logo32x32.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("minimal program")
    bgd_image = pygame.image.load("background.png")
    image = pygame.image.load("01_image.png")

    bgd_image = bgd_image.convert()

    bgd_image.set_alpha(255)
    image.set_alpha(255)

    logo.set_alpha(255)

    xpos =110
    ypos = 50
    screen.blit(image, (xpos,ypos))
    # define a variable to control the main loop
    running = True

    step_x =3
    step_y =3

    x=4
    y=4

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


        print (enemy.get_posx())
        print (screen_width)

        if enemy.get_posx()>screen_width-65 or enemy.get_posx()<1:
            print (enemy.get_posx())
            x = -x
        if enemy.get_posy()>screen_height-65 or enemy.get_posy()<1:
            print (enemy.get_posy())
            y = -y

        enemy.move(x,y)

        # first erase the screen
        #(just blit the background over anything on screen)
        screen.fill((xpos/640*255,ypos/480*255,0))
        image.set_alpha(xpos/640*255)

        screen.blit(bgd_image, (0,0))
        # now blit the smiley on screen

        screen.blit(image, (xpos, ypos))
        robots.update(screen)
        robots.draw(screen)

        enemys.update(screen)
        enemys.draw(screen)

        pygame.draw.line(screen,(255,0,0),(60,80),(130,100))
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

        keystate = pygame.key.get_pressed()

        #handle player input
        dir = keystate[K_RIGHT] - keystate[K_LEFT]
        dir2 = keystate[K_DOWN] - keystate[K_UP]

        for rob in pygame.sprite.spritecollide(enemy, robots, 1):
            rob.kill()

        for allrobots in robots:
            allrobots.move(dir,dir2)


        pygame.time.delay(10)





#call the "main" function if running this script
if __name__ == '__main__': main()
