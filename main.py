import random
from constants import *
from assets import *
from player import Player
from enemy import Enemy

# Inicjalizacja Pygame
pygame.init()
pygame.display.set_caption("Math RPG")

player = Player(WIDTH // 2, HEIGHT // 2, "Wilczas")
enemies = [
    Enemy(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), random.choice(["Goblin", "Golem", "Troll", "Ogr"]))
    for _ in range(5)
]

def show_start_screen():
    title_image = pygame.image.load("math_hero_enter_screen.png")
    title_image = pygame.transform.scale(title_image, (WIDTH, HEIGHT))  # Dopasowanie do ekranu

    screen.blit(title_image, (0, 0))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                waiting = False  # Rozpoczęcie gry

show_start_screen()



# Funkcja wyboru postaci
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

    # Po wybraniu postaci zwracamy jej nazwę
    return chosen_character

# Wybór postaci
player_character = choose_character()

# Tworzenie gracza i wrogów
player = Player(WIDTH // 2, HEIGHT // 2, player_character)
enemies = [
    Enemy(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), random.choice(list(enemy_sprites.keys())))
    for _ in range(5)]


def show_message(message):
    message_font = pygame.font.SysFont(None, 60)
    message_surface = message_font.render(message, True, BLACK)
    message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.fill(WHITE)
    screen.blit(message_surface, message_rect)
    pygame.display.flip()

    pygame.time.delay(1000)


def math_battle(enemy_type, hero_sprite):
    """
    Wyświetla ekran walki z pytaniem matematycznym.
    W przypadku błędnej odpowiedzi zmniejsza zdrowie gracza o 1 punkt.
    Zwraca True, gdy gracz odpowie poprawnie.
    """
    import random

    # Generowanie pytania i poprawnej odpowiedzi
    if enemy_type in ["Troll", "Ogr"]:
        a, b = random.randint(2, 10), random.randint(2, 10)
        question = f"Ile to {a} x {b}?"
        correct_answer = a * b
    else:
        a, b = random.randint(1, 10), random.randint(1, 10)
        question = f"Ile to {a} + {b}?"
        correct_answer = a + b

    # Skalowanie sprite'ów
    enemy_sprite = enemy_sprites[enemy_type]
    enemy_sprite = pygame.transform.scale(enemy_sprite, (200, 200))

    input_text = ""
    clock = pygame.time.Clock()
    battle_active = True

    font_large = pygame.font.SysFont(None, 48)
    font_small = pygame.font.SysFont(None, 36)

    while battle_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    try:
                        user_answer = int(input_text)
                        if user_answer == correct_answer:
                            return True
                        else:
                            player.health -= 20
                    except ValueError:
                        player.health = player.health
                    input_text = ""
                    if player.health == 0:
                        show_message("Koniec gry!")
                        pygame.quit()

                else:
                    if event.unicode.isdigit():
                        input_text += event.unicode

        # Rysowanie tła i elementów ekranu walki
        screen.fill((200, 200, 200))
        hero_rect = hero_sprite.get_rect(center=(WIDTH // 4, HEIGHT // 2))
        enemy_rect = enemy_sprite.get_rect(center=(3 * WIDTH // 4, HEIGHT // 2))
        screen.blit(hero_sprite, hero_rect)
        screen.blit(enemy_sprite, enemy_rect)

        # Rysowanie paska życia nad bohaterem
        health_bar_width = hero_sprite.get_width()  # 100 pikseli
        health_bar_height = 10
        health_ratio = player.health / 100.0  # Zakładamy maksymalne zdrowie = 100
        bar_x = hero_rect.x
        bar_y = hero_rect.y - 15  # Pasek nad sprite'm bohatera
        pygame.draw.rect(screen, RED, (bar_x, bar_y, health_bar_width, health_bar_height))
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, health_bar_width * health_ratio, health_bar_height))

        # Wyświetlenie pytania
        question_surface = font_large.render(question, True, BLACK)
        question_rect = question_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(question_surface, question_rect)

        # Wyświetlenie wpisanego tekstu
        input_prompt = "Odpowiedź: " + input_text
        input_surface = font_small.render(input_prompt, True, BLACK)
        input_rect = input_surface.get_rect(center=(WIDTH // 2, 3 * HEIGHT // 4))
        screen.blit(input_surface, input_rect)

        pygame.display.flip()
        clock.tick(30)



clock = pygame.time.Clock()
running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)
    player.animation.update(dt)

    # Czyścimy ekran (tylko raz)
    screen.fill(BLACK)

    # Rysujemy animowany sprite gracza
    current_image = player.animation.get_image()
    screen.blit(current_image, (player.x, player.y))

    # Rysujemy pasek życia (możesz dostosować pozycję i rozmiar)
    pygame.draw.rect(screen, RED, (player.x, player.y - 15, 50, 5))
    pygame.draw.rect(screen, GREEN, (player.x, player.y - 15, 50 * (player.health / 100), 5))

    # Rysujemy wrogów
    for enemy in enemies[:]:
        enemy.draw(screen)
        if enemy.check_collision(player):
            if math_battle(enemy.type, player.battle_sprite):
                enemies.remove(enemy)
                show_message("Pokonałeś wroga!")

    # Wywołujemy flip() tylko raz, po narysowaniu wszystkiego
    pygame.display.flip()

    pygame.time.delay(30)

pygame.quit()
