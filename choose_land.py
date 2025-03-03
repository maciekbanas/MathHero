import os
import pygame
from constants import *
def choose_land():
    """
    Funkcja wyświetlająca ekran wyboru krainy za pomocą ilustracji zamiast przycisków.
    """

    assets_path = os.path.join("assets", "lands")

    lands = ["Dodatnie Lasy", "Mnożeniowe Wyżyny"]
    land_images = {
        "Dodatnie Lasy": pygame.image.load(os.path.join(assets_path, "forest.png")),
        "Mnożeniowe Wyżyny": pygame.image.load(os.path.join(assets_path, "hills.png"))
    }

    font = pygame.font.SysFont(None, 60)
    button_width = WIDTH // 3
    button_height = HEIGHT // 2
    start_x = (WIDTH - (2 * button_width + 50)) // 2
    start_y = HEIGHT // 4

    land_buttons = []
    for i, land_name in enumerate(lands):
        rect = pygame.Rect(start_x + i * (button_width + 50), start_y, button_width, button_height)
        land_buttons.append((land_name, rect))

    chosen_land = None

    while chosen_land is None:
        screen.fill(WHITE)
        title_text = font.render("Wybierz krainę", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 8))
        screen.blit(title_text, title_rect)

        for land_name, rect in land_buttons:
            image = pygame.transform.scale(land_images[land_name], (button_width, button_height))
            screen.blit(image, rect.topleft)
            text_surface = font.render(land_name, True, WHITE)
            text_rect = text_surface.get_rect(center=(rect.centerx, rect.bottom + 30))
            screen.blit(text_surface, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                for land_name, rect in land_buttons:
                    if rect.collidepoint(mouse_pos):
                        chosen_land = land_name
                        break

    return chosen_land