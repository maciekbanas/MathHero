from constants import *
from assets import player_sprites
from assets import player_minifig_sprites

from PIL import Image
import pygame

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
        self.frame_duration = frame_duration  # czas trwania jednej klatki (w milisekundach)
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

    def move(self, keys):
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed


