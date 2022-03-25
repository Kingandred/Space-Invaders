import pygame
from pygame.locals import *

#define frames per second
clock = pygame.time.Clock()
fps = 60

screen_width = 600
screen_height = 800

screen = pygame.display.set_mode((screen_wdith, screen_height))
pygame.display.set_caption("Space Invaders")

#load image
bg = pygame.image.load("")

def draw_bg():
  screen.blit(bg, (0, 0))

run = True
while run:
  
  clock.tick(fps)
  
  #draw bacjground
  draw_bg()
  
  #event handlers
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
      
      
  pygame.display.update()
      
pygame.quit()
