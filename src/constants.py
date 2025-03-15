import pygame
from pathlib import Path

# Base dirs
BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "../assets"

# Ustawienia ekranu (pełny ekran)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
GREY = (192, 192, 192)
# Lista dostępnych postaci
characters = ["Rycerz", "Czarodziejka", "Wilczas", "Mag"]

grid_size = 80