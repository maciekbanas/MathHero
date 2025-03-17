from constants import *
from assets import enemy_sprites, enemy_fig_sprites

class Enemy:
    def __init__(self, x, y, enemy_type):
        self.x = x
        self.y = y
        self.type = enemy_type
        self.size = 160 if enemy_type in ["Troll", "Golem"] else grid_size
        self.sprite = pygame.transform.smoothscale(enemy_fig_sprites[enemy_type], (self.size, self.size))

    def draw(self, surface):
        surface.blit(self.sprite, (self.x, self.y))

    def check_collision(self, player):
        return pygame.Rect(self.x, self.y, grid_size, grid_size).colliderect(pygame.Rect(player.x, player.y, grid_size, grid_size))
