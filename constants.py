import pygame

# Ustawienia ekranu (pełny ekran)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Lista dostępnych postaci
characters = ["Rycerz", "Mag", "Wróżka", "Wojowniczka"]
