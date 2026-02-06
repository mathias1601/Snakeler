""" 
vegger som hindrer firkanten i å gå utenfor skjermem
"""

import pygame
import sys

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Første pygame")

clock = pygame.time.Clock()
FPS = 60

WHITE = (255,255,255)
BLUE = (60,60,255)

x, y = 100, 100
speed = 5
size = 50

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        if not x <= 0:
            x -= speed
    if keys[pygame.K_RIGHT]:
        if not x >= WIDTH - size:
            x += speed
    if keys[pygame.K_UP]:
        if not y <= 0:
            y -= speed
    if keys[pygame.K_DOWN]:
        if not y >= HEIGHT - size:
            y += speed

    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, (x, y, size, size))
    pygame.display.flip()

pygame.quit()
sys.exit()