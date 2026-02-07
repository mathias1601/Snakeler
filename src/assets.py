import pygame
from os import path

from .options import *


BACKGROUND_IMAGE = pygame.image.load(path.join('assets', 'stars.jpg')).convert()
ROCKET_IMAGE = pygame.image.load(path.join('assets', 'rocket.png')).convert_alpha()
BOULDER_IMAGE = pygame.image.load(path.join('assets', 'boulder.png')).convert_alpha()
SOUNDTRACK = path.join('assets', 'soundtrack.mp3')

# Font
FONT_TYPE = pygame.font.Font(path.join('assets', 'dpcomic.ttf'), FONT_SIZE)