from constants import *
from assets import player_sprites

class Player:
    def __init__(self, x, y, character):
        self.x = x
        self.y = y
        self.speed = 5
        self.health = 100
        self.character = character
        self.battle_sprite = pygame.transform.scale(player_sprites[character], (200, 200))
        self.sprite = pygame.transform.scale(player_sprites[character], (50, 50))

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed

    def draw(self, surface):  # FIX: Added 'surface' parameter
        surface.blit(self.sprite, (self.x, self.y))
