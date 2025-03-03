from src.constants import *
from assets import enemy_sprites

class Enemy:
    def __init__(self, x, y, enemy_type):
        self.x = x
        self.y = y
        self.type = enemy_type
        self.sprite = pygame.transform.scale(enemy_sprites[enemy_type], (50, 50))

    def draw(self, surface):  # FIX: Added 'surface' parameter
        surface.blit(self.sprite, (self.x, self.y))

    def check_collision(self, player):
        return pygame.Rect(self.x, self.y, 50, 50).colliderect(pygame.Rect(player.x, player.y, 50, 50))
