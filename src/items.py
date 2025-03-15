import os
from constants import *
from utils import get_asset_path

berry_image = pygame.image.load(get_asset_path(os.path.join("items", "berries.png")))
berry_image = pygame.transform.smoothscale(berry_image, (grid_size, grid_size))

class Berry:
    """Represents a berry on the map that restores health when collected."""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(berry_image, (grid_size, grid_size))
        self.rect = pygame.Rect(self.x, self.y, grid_size, grid_size)

    def draw(self, screen):
        """Draws the berry on the screen."""
        screen.blit(self.image, (self.x, self.y))

    def check_collision(self, player):
        """Checks if the player has collected the berry."""
        return self.rect.colliderect(pygame.Rect(player.x, player.y, grid_size, grid_size))
