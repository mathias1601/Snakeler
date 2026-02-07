import pygame
import random
from .options import *

#gjerder, generer steiner, generer gress, gjerdet er ødelagt der man kan gå til neste bane

class Garden():
    def __init__(self):
        self.size = (WIDTH, HEIGHT)
        self.grid = 60
        self.diff = 30
        self.rowgrid = WIDTH // self.grid
        self.colgrid = HEIGHT // self.grid
        self.image = pygame.transform.scale(IMG, self.size)

        self.hurdles = self._generate_hurdles(30)
        self.field = self._fill() #hvert element tilsvarer 60x60 blokker
        self._fill_in_hurdles()
    
    def _generate_hurdles(self): #adjust difficulty by hurdles
        hurdles = []
        for _ in range(self.diff):
            posx = random.randint(WIDTH//self.grid  - 1)*self.grid 
            posy = random.randint(HEIGHT//self.grid  - 1)*self.grid 
            hurdle = pygame.Rect(posx, posy, self.grid , self.grid) #Projectile klassen hjalp :^)

            if hurdle.collidelist(hurdles) == -1: #søkte opp
                hurdles.append(hurdle)
            return hurdles
    
    def collide(self, lawn_mower): 
        return lawn_mower.colliderect(self.hurdles) #Projectile klassen hjalp :^)
    
    def _fill(self):
        temp = []
        field = []
        for _ in range(self.rowgrid):
            temp.append(1) # grass = 1
        for _ in range(self.colgrid):
            field.append(temp)
        return field

    def _fill_in_hurdles(self): 
        for elem in self.hurdles: 
            x, y = elem.left, elem.top
            if self.field[y][x] == 1: 
                self.field[y][x] = 0 #stein = 0

    def transform(self, posx, posy): #transform grid positions to screen
        return (posx*self.grid, posy*self.grid)
    
    def draw(self):
        pass

    def make_garden(self): 
        pass
# 60x60                
    def generate_enemies(self): #should have its own class, adjust difficulty by number/strength of enemies; max 3 levels
        pass

        
