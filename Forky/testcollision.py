import pygame
import pygame.freetype
from pygame.math import Vector2

pygame.init()
clock = pygame.time.Clock()

WIDTH = 900
HEIGHT = 550
screen = pygame.display.set_mode((WIDTH, HEIGHT))

track_image = pygame.image.load("trackimagelinkinthepost.png").convert_alpha()

REDCAR_ORIGINAL = pygame.Surface((50, 30), pygame.SRCALPHA)
redangle = 0
redspeed = 2
pos_red = Vector2(200, 200)
vel_red = Vector2(redspeed, 0)

redcar = REDCAR_ORIGINAL
pygame.draw.polygon(REDCAR_ORIGINAL, pygame.Color('dodgerblue'), [(0, 30), (50, 20), (50, 10), (0, 0)])

mask_red = pygame.mask.from_surface(redcar)
off_mask = pygame.mask.from_surface(track_image)
off_mask.invert()

font = pygame.freetype.SysFont(None, 42, True, True)
s=False
run = True
while run:
  for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

  keys = pygame.key.get_pressed()
  if keys[pygame.K_LEFT]:
      redangle += 3
      vel_red.rotate_ip(-3)
      redcar = pygame.transform.rotate(REDCAR_ORIGINAL, redangle)
      mask_red = pygame.mask.from_surface(redcar)

  elif keys[pygame.K_RIGHT]:
      redangle -= 3
      vel_red.rotate_ip(3)
      redcar = pygame.transform.rotate(REDCAR_ORIGINAL, redangle)
      mask_red = pygame.mask.from_surface(redcar)

  pos_red += vel_red
  redcar_pos = list(int(v) for v in pos_red)

  offtrack = off_mask.overlap(mask_red, redcar_pos)

  screen.fill(pygame.Color('grey12'))
  screen.blit(track_image, (0, 0))

  if offtrack:
    font.render_to(screen, (250, 20), '!!! OFFTRACK !!!', pygame.Color('orange'))

  screen.blit(redcar, redcar_pos)
  pygame.display.flip()
  clock.tick(60)

pygame.quit()
