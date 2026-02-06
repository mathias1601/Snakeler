""" Hovedprogrammet som skal kjøres """
import pygame
from .options import *

# Init
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # needed here by assets.py

import sys, random, time, os

from .assets import *
from .Player import Player
from .Boulder import Boulder
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
    boulders = []

    score = 0

    def draw_frame():
        screen.blit(BACKGROUND_IMAGE, (0, 0))
        pygame.draw.rect(screen, BLACK, (0, 690, WIDTH, 30))  # Ground
        p1.draw(screen)
        for projectile in projectiles:
            projectile.update(dt)
            projectile.draw(screen)
        for boulder in boulders:
            boulder.draw(screen)
            
        # Draw score and lives
        score_text = FONT_TYPE.render(f'Score: {score}', False, FONT_COLOR)
        lives_text = FONT_TYPE.render(f"♥"*p1.lives, True, FONT_COLOR)
        screen.blit(score_text, (10, 10))
        screen.blit(lives_text, (WIDTH - 120, 10))

        pygame.display.flip()

    # Game loop
    running = True
    while running:
        clock.tick(FRAMERATE)  # Limit frame rate
        current_time = pygame.time.get_ticks()

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get key presses
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            p1.x -= p1.speed * dt
        if keys[pygame.K_d]:
            p1.x += p1.speed * dt
        if keys[pygame.K_SPACE]:
            if current_time - p1.last_shot_time >= BULLET_COOLDOWN_MS:
                p1.last_shot_time = current_time
                projectile = p1.shoot()
                projectiles.append(projectile)

        if current_time - last_boulder_spawn_time >= BOULDER_SPAWN_INTERVAL_MS:
            boulder = Boulder()
            boulders.append(boulder)
            last_boulder_spawn_time = current_time

        for projectile in projectiles:
            if projectile.y <= 0:
                projectiles.remove(projectile)
            projectile.update(dt)
            # collision w boulder
            for boulder in boulders:
                if projectile.collides_with(boulder.get_rect()):
                    projectiles.remove(projectile)
                    boulders.remove(boulder)
                    score += 100
                    break

        for boulder in boulders:
            boulder.y += boulder.speed * dt
            if boulder.y >= HEIGHT + boulder.size[1]:
                boulders.remove(boulder)
                p1.lives -= 1
                if p1.lives <= 0:
                    # Game over sequence
                    boulders.clear()
                    projectiles.clear()
                    draw_frame()
                    game_over_text = FONT_TYPE.render("GAME OVER", True, RED)
                    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2 - game_over_text.get_height() // 2))
                    pygame.display.flip()
                    time.sleep(2)
                    running = False

        # Update display
        draw_frame()

        dt = clock.tick(60) / 1000

    # Clean up
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    run()
