import pygame
from sys import exit 
from pygame.locals import *
import time 
pygame.init()
screen = pygame.display.set_mode(((1020,720)))
background = 'gray'
clock = pygame.time.Clock()

class girl(object):
    def __init__(info,x,y,vel,nb_life,nb_bomb,xp,lvl,hitbox):
         info.nb_life = nb_life 
         info.nb_bomb = nb_bomb
         info.xp = xp 
         info.lvl = lvl
         info.x = x 
         info.y = y 
         info.hitbox = hitbox
         info.vel = vel
    def __str__(info):
        return f"Life : {info.nb_life}\n Bomb : {nb_bomb} \n Power :{info.xp}"


    

carac = girl(400,200,7,3,3,0,0,4)
kek = carac.y

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clef = pygame.key.get_pressed()
    
    

    if clef[pygame.K_LEFT] and carac.x > carac.hitbox:
        if clef[pygame.K_LSHIFT]:
            carac.x -= carac.vel // 2
        else:
            carac.x -= carac.vel 
    if clef[pygame.K_RIGHT] and carac.x < 1020 - carac.hitbox: 
        if clef[pygame.K_LSHIFT]:
            carac.x += carac.vel // 2
        else:
            carac.x += carac.vel 
    if clef[pygame.K_UP] and carac.y > carac.hitbox:           
        if clef[pygame.K_LSHIFT]:
            carac.y -= carac.vel // 2
        else:
            carac.y -= carac.vel 
    if clef[pygame.K_DOWN] and carac.y < 720 - carac.hitbox: 
        if clef[pygame.K_LSHIFT]:
            carac.y += carac.vel // 2
        else:
            carac.y += carac.vel 
    screen.fill(background)
    pygame.draw.circle(screen, 'red', [carac.x,carac.y], carac.hitbox) 
    if clef[pygame.K_w]:
        while kek > 0:
            pygame.draw.circle(screen,'blue',[carac.x, kek], 5)
            kek -= 4
            pygame.display.update()        
    else:
        kek = carac.y    
    pygame.display.update()
    clock.tick(60)
