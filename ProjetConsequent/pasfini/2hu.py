import pygame
from sys import exit 
from pygame.locals import *

caca = None 
pygame.init()
screen = pygame.display.set_mode(((1020,720)))
imgtest = pygame.image.load('ProjetConsequent/pasfini/flandre.png')
background = 'dark gray'
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill(background)
    pygame.display.update()
    clock.tick(60)
