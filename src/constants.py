import pygame
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "../assets"

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BROWN = (150, 100, 50)
RED = (255, 0, 0)
GREEN = (50, 200, 50)
GREY = (192, 192, 192)

characters = ["Rabbit", "Czarodziejka", "Wilczas", "Kocias"]

grid_size = 80