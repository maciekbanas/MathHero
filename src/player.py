import pygame
from assets import player_sprites, player_minifig_sprites
from PIL import Image

def load_gif_frames(filename, new_size=None):
    frames = []
    pil_image = Image.open(filename)
    try:
        while True:
            frame = pil_image.copy().convert('RGBA')
            pygame_frame = pygame.image.fromstring(frame.tobytes(), frame.size, 'RGBA')
            if new_size is not None:
                pygame_frame = pygame.transform.scale(pygame_frame, new_size)
            frames.append(pygame_frame)
            pil_image.seek(pil_image.tell() + 1)
    except EOFError:
        pass
    return frames

class AnimatedSprite:
    def __init__(self, frames, frame_duration):
        self.frames = frames
        self.frame_duration = frame_duration
        self.current_time = 0
        self.current_frame = 0

    def update(self, dt):
        self.current_time += dt
        if self.current_time >= self.frame_duration:
            self.current_time = 0
            self.current_frame = (self.current_frame + 1) % len(self.frames)

    def get_image(self):
        return self.frames[self.current_frame]

class Player:
    def __init__(self, x, y, character):
        self.x = x
        self.y = y
        self.speed = 5
        self.health = 100
        self.character = character
        self.battle_sprite = pygame.transform.scale(player_sprites[character], (200, 200))
        self.sprite = load_gif_frames(player_minifig_sprites[character], new_size=(50, 50))
        self.animation = AnimatedSprite(self.sprite, frame_duration=100)

        self.grid_size = 50
        self.target_x = self.x
        self.target_y = self.y
        self.is_moving = False

    def move(self, keys):
        """ Obsługuje wejście gracza, jeśli nie jest w trakcie ruchu """
        if self.is_moving:
            return

        if keys[pygame.K_LEFT]:
            self.target_x = self.x - self.grid_size
        elif keys[pygame.K_RIGHT]:
            self.target_x = self.x + self.grid_size
        elif keys[pygame.K_UP]:
            self.target_y = self.y - self.grid_size
        elif keys[pygame.K_DOWN]:
            self.target_y = self.y + self.grid_size

        if self.x != self.target_x or self.y != self.target_y:
            self.is_moving = True

    def update_position(self):
        """ Stopniowe przesuwanie postaci do docelowego pola """
        if self.is_moving:
            if abs(self.x - self.target_x) > self.speed:
                self.x += self.speed if self.x < self.target_x else -self.speed
            else:
                self.x = self.target_x

            if abs(self.y - self.target_y) > self.speed:
                self.y += self.speed if self.y < self.target_y else -self.speed
            else:
                self.y = self.target_y

            if self.x == self.target_x and self.y == self.target_y:
                self.is_moving = False  # Ruch zakończony
