import pygame

from .options import *


BACKGROUND_IMAGE = pygame.image.load('./assets/stars.jpg').convert()
ROCKET_IMAGE = pygame.image.load('./assets/rocket.png').convert_alpha()
BOULDER_IMAGE = pygame.image.load('./assets/boulder.png').convert_alpha()

# Font
FONT_TYPE = pygame.font.Font('./assets/dpcomic.ttf', FONT_SIZE)