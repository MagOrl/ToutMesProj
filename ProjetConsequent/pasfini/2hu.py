import pygame
from sys import exit 
from pygame.locals import *

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
class projectile(object): 
    def __init__(self,x,y,width,height,vel):
        self.x = x 
        self.y = y 
        self.width = width
        self.height = height
        self.vel = vel 
    


carac = girl(400,200,7,3,3,0,0,4)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clef = pygame.key.get_pressed()
     
        
    if clef[pygame.K_LEFT] and carac.x > carac.hitbox:
        if clef[pygame.K_LSHIFT]:
            carac.x-= carac.vel // 2
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
    pygame.draw.rect(screen,'blue',(carac.x,projectile()))
    #pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()
    clock.tick(60)
