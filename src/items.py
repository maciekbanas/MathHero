import pygame
import random
import os
from constants import *
from utils import get_asset_path

# Ładowanie grafiki jagód
berry_image = pygame.image.load(get_asset_path(os.path.join("items", "berries.png")))
berry_image = pygame.transform.scale(berry_image, (50, 50))

# Funkcja generująca jagódki na planszy
def generate_berries():
    return [pygame.Rect(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), 30, 30) for _ in range(2, 4)]
