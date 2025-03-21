import os
import pygame
from save_load import load_game_state

WIDTH, HEIGHT = 1600, 900
WHITE = (255, 255, 255)

background_image = pygame.image.load(os.path.join("assets", "start", "start_panorama.png"))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

def start_screen(screen):
    """
    Wyświetla ekran startowy z dwoma przyciskami:
    "Nowa gra" oraz "Załaduj grę". Zwraca "new" w przypadku nowej gry,
    lub wczytany stan gry (jako dict) przy wyborze "Załaduj grę".
    """
    running = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 50)

    # Definiujemy prostokąty przycisków
    new_game_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 70, 300, 60)
    load_game_button = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 10, 300, 60)

    while running:
        screen.blit(background_image, (0, 0))
        title_text = font.render("Math RPG", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        # Rysujemy przycisk "Nowa gra"
        pygame.draw.rect(screen, (0, 200, 0), new_game_button)
        new_game_text = font.render("Nowa gra", True, (0, 0, 0))
        screen.blit(new_game_text, (new_game_button.centerx - new_game_text.get_width() // 2,
                                    new_game_button.centery - new_game_text.get_height() // 2))

        # Rysujemy przycisk "Załaduj grę"
        pygame.draw.rect(screen, (0, 200, 0), load_game_button)
        load_game_text = font.render("Załaduj grę", True, (0, 0, 0))
        screen.blit(load_game_text, (load_game_button.centerx - load_game_text.get_width() // 2,
                                     load_game_button.centery - load_game_text.get_height() // 2))

        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_button.collidepoint(event.pos):
                    return "new"
                elif load_game_button.collidepoint(event.pos):
                    state = load_game_state()
                    if state is not None:
                        return state
                    else:
                        return "new"