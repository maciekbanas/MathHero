import os
import pygame
from save_load import create_user, get_users, has_saved_game

WIDTH, HEIGHT = 1600, 900
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
RED = (200, 60, 60)

background_image = pygame.image.load(os.path.join("assets", "start", "start_panorama.png"))
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


def user_selection_screen(screen):
    """Ekran wyboru lub tworzenia użytkownika."""
    running = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 44)
    small_font = pygame.font.SysFont(None, 34)

    create_button = pygame.Rect(WIDTH // 2 - 220, HEIGHT - 190, 440, 60)
    close_game_button = pygame.Rect(WIDTH // 2 - 220, HEIGHT - 110, 440, 60)
    input_box = pygame.Rect(WIDTH // 2 - 220, HEIGHT - 220, 440, 55)

    selected_user = None
    input_mode = False
    typed_name = ""
    message = ""

    while running:
        users = get_users()
        screen.blit(background_image, (0, 0))

        title_text = font.render("Wybór użytkownika", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, 80))

        y_start = 180
        user_buttons = []
        for idx, user in enumerate(users):
            btn = pygame.Rect(WIDTH // 2 - 220, y_start + idx * 65, 440, 52)
            user_buttons.append((btn, user))
            color = GREEN if user == selected_user else (210, 210, 210)
            pygame.draw.rect(screen, color, btn, border_radius=8)
            pygame.draw.rect(screen, BLACK, btn, 2, border_radius=8)
            user_text = small_font.render(user, True, BLACK)
            screen.blit(user_text, (btn.centerx - user_text.get_width() // 2,
                                    btn.centery - user_text.get_height() // 2))

        pygame.draw.rect(screen, (255, 255, 255), input_box, border_radius=8)
        pygame.draw.rect(screen, BLACK, input_box, 2, border_radius=8)
        placeholder = typed_name if input_mode else "Wpisz nazwę nowego użytkownika"
        text_color = BLACK if input_mode else (120, 120, 120)
        input_text = small_font.render(placeholder, True, text_color)
        screen.blit(input_text, (input_box.x + 12, input_box.y + 12))

        pygame.draw.rect(screen, GREEN, create_button, border_radius=8)
        pygame.draw.rect(screen, BLACK, create_button, 2, border_radius=8)
        create_text = small_font.render("Stwórz użytkownika (Enter)", True, BLACK)
        screen.blit(create_text, (create_button.centerx - create_text.get_width() // 2,
                                  create_button.centery - create_text.get_height() // 2))

        pygame.draw.rect(screen, RED, close_game_button, border_radius=8)
        pygame.draw.rect(screen, BLACK, close_game_button, 2, border_radius=8)
        close_text = small_font.render("Zamknij grę", True, BLACK)
        screen.blit(close_text, (close_game_button.centerx - close_text.get_width() // 2,
                                 close_game_button.centery - close_text.get_height() // 2))

        if message:
            info_text = small_font.render(message, True, WHITE)
            screen.blit(info_text, (WIDTH // 2 - info_text.get_width() // 2, HEIGHT - 40))

        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    input_mode = True
                elif create_button.collidepoint(event.pos):
                    ok, msg = create_user(typed_name)
                    message = msg
                    if ok:
                        selected_user = typed_name.strip()
                        typed_name = ""
                        input_mode = False
                elif close_game_button.collidepoint(event.pos):
                    pygame.quit()
                    exit()
                else:
                    for btn, user in user_buttons:
                        if btn.collidepoint(event.pos):
                            selected_user = user
                            return selected_user
            elif event.type == pygame.KEYDOWN:
                if input_mode:
                    if event.key == pygame.K_RETURN:
                        ok, msg = create_user(typed_name)
                        message = msg
                        if ok:
                            selected_user = typed_name.strip()
                            typed_name = ""
                            input_mode = False
                    elif event.key == pygame.K_BACKSPACE:
                        typed_name = typed_name[:-1]
                    else:
                        if len(typed_name) < 24:
                            typed_name += event.unicode


def start_screen(screen, user_name):
    """Ekran startowy po wyborze użytkownika."""
    running = True
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 50)
    small_font = pygame.font.SysFont(None, 35)

    new_game_button = pygame.Rect(WIDTH // 2 - 170, HEIGHT // 2 - 70, 340, 60)
    load_game_button = pygame.Rect(WIDTH // 2 - 170, HEIGHT // 2 + 10, 340, 60)
    back_button = pygame.Rect(WIDTH // 2 - 170, HEIGHT // 2 + 90, 340, 60)

    while running:
        screen.blit(background_image, (0, 0))
        title_text = font.render(f"Math RPG - {user_name}", True, WHITE)
        screen.blit(title_text, (WIDTH // 2 - title_text.get_width() // 2, HEIGHT // 4))

        pygame.draw.rect(screen, GREEN, new_game_button)
        new_game_text = font.render("Nowa gra", True, BLACK)
        screen.blit(new_game_text, (new_game_button.centerx - new_game_text.get_width() // 2,
                                    new_game_button.centery - new_game_text.get_height() // 2))

        load_enabled = has_saved_game(user_name)
        load_color = GREEN if load_enabled else RED
        pygame.draw.rect(screen, load_color, load_game_button)
        load_game_text = font.render("Załaduj grę", True, BLACK)
        screen.blit(load_game_text, (load_game_button.centerx - load_game_text.get_width() // 2,
                                     load_game_button.centery - load_game_text.get_height() // 2))

        pygame.draw.rect(screen, RED, back_button)
        back_text = font.render("Wróć", True, BLACK)
        screen.blit(back_text, (back_button.centerx - back_text.get_width() // 2,
                                back_button.centery - back_text.get_height() // 2))

        if not load_enabled:
            no_save_text = small_font.render("Brak zapisu dla wybranego użytkownika", True, WHITE)
            screen.blit(no_save_text, (WIDTH // 2 - no_save_text.get_width() // 2, HEIGHT // 2 + 90))

        pygame.display.flip()
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if new_game_button.collidepoint(event.pos):
                    return "new"
                elif load_game_button.collidepoint(event.pos) and load_enabled:
                    return "load"
                elif back_button.collidepoint(event.pos):
                    return "back"
