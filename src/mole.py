import pygame
import random
from Projectile import Projectile
from garden import Garden

#SNEILESKOOOOOOO
class Mole():
    def __init__(self, garden):
        self.garden = garden
        self.size = (60,60)
        self.rect = garden.generate_enemy()
        self.counter = 0
        self.pause = 5 #seconds
        self.amount = 3
        self.peekabo = pygame.transform.scale(pygame.image.load("src/mole.png").convert_alpha(),
                                                  self.size)
        self.throw = pygame.transform.scale(pygame.image.load("src/mole_throw.png").convert_alpha(),
                                                  self.size)
        self.death = pygame.transform.scale(pygame.image.load("src/mole_dead.png").convert_alpha(),
                                                  self.size)
        self.projectile = []

    def _throw_projectile(self):
        x = self.rect.centerx
        y = self.rect.top
        snailshoe = Projectile(x,y)
        self.projectile.append(snailshoe)

    def _throw_and_wait(self):
        self.throw_projectile()
        while(self.counter <= self.pause):
            self.counter+=1
        return True

    def collision_w_lawnmower(self, lawnmower):
        return self.rect.colliderect(lawnmower)
    
    def update(self): 
        status = self._throw_and_wait()
        
        
    def draw(self, screen):
        pass
