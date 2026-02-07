""" Hovedprogrammet som skal kjøres """
import pygame
from .options import *

# Init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # needed here by assets.py

import sys, random, time, os

from .assets import *
from .Player import Player
from .Projectile import Projectile


def run():
    pygame.display.set_caption("Boulder Game")

    # Clock and timing
    clock = pygame.time.Clock()
    dt = 0
    last_boulder_spawn_time = 0

    # Game objects
    p1 = Player()
    projectiles = []
    cut_grass = set()

    score = 0

    def draw_frame():
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        pygame.draw.rect(screen, GREEN, (0, 0, WIDTH, HEIGHT))  # Ground
        for projectile in projectiles:
            projectile.update(dt)
            projectile.draw(screen)

        # Update grass
        for cut_grass_position in cut_grass:
            pygame.draw.rect(screen, DARK_GREEN, pygame.Rect(cut_grass_position[0], cut_grass_position[1], 64, 64))
            
        p1.draw(screen)
        
        
        # Draw score and lives
        score_text = FONT_TYPE.render(f'Score: {score}', False, FONT_COLOR)
        lives_text = FONT_TYPE.render(f"♥"*p1.lives, True, FONT_COLOR)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 120, 10))

        pygame.display.flip()

    # Game loop
    running = True

    direction = pygame.Vector2(0, -1)
    last_move_pos = (p1.x, p1.y)

    while running:
        dt = clock.tick(FRAMERATE) / 1000
        current_time = pygame.time.get_ticks()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        lastX = p1.x
        lastY = p1.y
            
        # Get key presses
        keys = pygame.key.get_pressed()
        input_dir = pygame.Vector2(0, 0)
        if keys[pygame.K_a]:
            input_dir.x -= 1
        if keys[pygame.K_d]:
            input_dir.x += 1
        if keys[pygame.K_w]:
            input_dir.y -= 1
        if keys[pygame.K_s]:
            input_dir.y += 1

        if input_dir.length_squared() > 0:
            input_dir = input_dir.normalize()
            direction = input_dir

        p1.x += direction.x * p1.speed * dt
        p1.y += direction.y * p1.speed * dt

        p1.x = max(0, min(WIDTH - p1.size[0], p1.x))
        p1.y = max(0, min(HEIGHT - p1.size[1], p1.y))

        if (p1.x, p1.y) != last_move_pos:
            cut_grass.add((lastX, lastY))
            last_move_pos = (p1.x, p1.y)
        if keys[pygame.K_SPACE]:
            if current_time - p1.last_shot_time >= BULLET_COOLDOWN_MS:
                p1.last_shot_time = current_time
                projectile = p1.shoot()
                projectiles.append(projectile)

        # Update display
        draw_frame()

    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run()
