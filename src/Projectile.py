from .options import *

class Projectile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = (4, 30)
        self.speed = BULLET_SPEED
        self.color = GREEN
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def update(self, dt):
        self.y -= self.speed * dt
        if self.y < 0:
            self.y = 0  # Prevent going off-screen
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size[0], self.size[1]))

    def collides_with(self, boulder_rect):
        return self.rect.colliderect(boulder_rect)