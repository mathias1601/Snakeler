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

        self.last_enemy = []
        self.hurdles = self._generate_hurdles()
        self.field = self._fill() #hvert element tilsvarer 60x60 blokker
        self._fill_in_hurdles()
    
    def _generate_hurdles(self): #adjust difficulty by hurdles
        hurdles = []
        for _ in range(self.diff):
            posx = random.randint(0, WIDTH//self.grid  - 1)
            posy = random.randint(0, HEIGHT//self.grid  - 1)
            hurdle = pygame.Rect(posx, posy, 1, 1) #Projectile klassen hjalp :^)

            if hurdle.collidelist(hurdles) == -1: #søkte opp
                hurdles.append(hurdle)
        return hurdles
        
    def generate_enemies(self): #should have its own class, adjust difficulty by number/strength of enemies; max 3 levels
        update = 0
        while(not update):
            posx = random.randint(0, WIDTH//self.grid  - 1)
            posy = random.randint(0, HEIGHT//self.grid  - 1)
            lil_enemy = pygame.Rect(posx, posy, 1, 1)
            if (lil_enemy.collidelist(self.last_enemy) == -1 and lil_enemy.collidelist(self.hurdles) == -1):
                update = 1
                if len(self.last_enemy) == 0: 
                    self.last_enemy.append(lil_enemy)
                    continue
                self.last_enemy[0] = lil_enemy
        return True
    
    def add_enemy(self): #button press to avoid enemy attack? ... don't use before enemy is made
        x, y = self.last_enemy[0].left, self.last_enemy[0].top 
        if self.field[y][x] == 1: 
                self.field[y][x] = 2 #enemy = 2

    def remove_enemy(self): # ... don't use before enemy is made
        x, y = self.last_enemy[0].left, self.last_enemy[0].top 
        if self.field[y][x] == 2: 
                self.field[y][x] = 1
    
    def collide(self, lawn_mower): 
        return lawn_mower.collidelist(self.hurdles) #Projectile klassen hjalp :^) 
                                                    #must use Rect, also should be in grid units
    
    def _fill(self):
        field = []
        for _ in range(self.colgrid):
            temp = [1]*self.rowgrid
            field.append(temp)
        return field

    def _fill_in_hurdles(self): 
        for elem in self.hurdles: 
            x, y = elem.left, elem.top
            if self.field[y][x] == 1: 
                self.field[y][x] = 0 #stein = 0

    def transform(self, rect): #transform grid positions to screen
        return pygame.Rect(rect.left*self.grid, rect.top*self.grid, 
                           rect.width*self.grid, rect.height*self.grid)
    
    def advance_lvl(self):
        self.field[5][-1] = 1
        self.field[5][-1] = 1

    def draw(self, screen):
        for y, row in enumerate(self.field): 
            for x, elem in enumerate(row):
                cell = pygame.Rect(x,y,1,1)
                proj = self.transform(cell)
                pygame.draw.rect(screen, GREEN, proj)

# 60x60                


        
