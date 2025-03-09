from src.constants import *
from src.assets import player_sprites

def choose_character():
    """
    Funkcja wyświetlająca ekran wyboru postaci w Pygame.
    Zwraca nazwę wybranej postaci (string).
    """
    total_width = int(0.9 * WIDTH)

    single_width = total_width // 4

    # Lista, w której będziemy przechowywać (nazwa_postaci, sprite, rect)
    char_data = []

    # Przygotowujemy pozycje i skalujemy grafiki
    for i, char_name in enumerate(characters):
        # Oryginalny sprite
        original_sprite = player_sprites[char_name]
        # Proporcja skalowania
        # Najpierw obliczamy współczynnik, żeby obrazek miał szerokość single_width
        w = original_sprite.get_width()
        h = original_sprite.get_height()
        scale_factor = single_width / w

        new_w = single_width
        new_h = int(h * scale_factor)

        # Skalowanie obrazka
        scaled_sprite = pygame.transform.scale(original_sprite, (new_w, new_h))

        # Pozycjonowanie tak, aby wszystkie były w jednym rzędzie, wyśrodkowane w pionie
        # Start X (dla i=0) możemy obliczyć tak, by łącznie 4 obrazki zajmowały 90% i były wycentrowane
        start_x = (WIDTH - total_width) // 2  # lewy brzeg całego bloku 90%
        pos_x = start_x + i * single_width    # pozycja X dla danego obrazka

        # Y ustawiamy, by obrazek był mniej więcej wycentrowany na ekranie
        pos_y = (HEIGHT - new_h) // 2

        # Tworzymy prostokąt kliknięcia
        rect = pygame.Rect(pos_x, pos_y, new_w, new_h)

        char_data.append((char_name, scaled_sprite, rect))

    chosen_character = None
    clock = pygame.time.Clock()

    while True:
        clock.tick(30)  # 30 FPS

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.KEYDOWN:
                # Opcjonalnie obsługa wyjścia klawiszem ESC
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                # Sprawdzamy, czy kliknięto w którąś z postaci
                for char_name, sprite, rect in char_data:
                    if rect.collidepoint(mouse_pos):
                        chosen_character = char_name
                        break

                if chosen_character is not None:
                    break

        if chosen_character is not None:
            break

        # Rysowanie ekranu wyboru
        screen.fill(WHITE)
        # Możesz dodać jakiś tytuł, np. "Wybierz postać"
        # np. narysować napis:
        font = pygame.font.SysFont(None, 60)
        text_surface = font.render("Wybierz postać", True, BLACK)
        text_rect = text_surface.get_rect(center=(WIDTH//2, HEIGHT//6))
        screen.blit(text_surface, text_rect)

        # Rysujemy każdą postać
        for char_name, sprite, rect in char_data:
            screen.blit(sprite, (rect.x, rect.y))

        pygame.display.flip()

    return chosen_character