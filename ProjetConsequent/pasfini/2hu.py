import pygame
from sys import exit 
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode(((1020,720)))
background = 'dark gray'
clock = pygame.time.Clock()

class monjoueur:
    def __init__(spell,xp):
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill(background)
    pygame.display.update()
    clock.tick(60)
