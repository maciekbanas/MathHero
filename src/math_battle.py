from assets import enemy_sprites
from constants import *
from utils import show_message
import os

def math_battle(player, enemy_type, selected_land):
    """
    Displays the battle screen and awards coins for winning.
    """
    import random

    coin_rewards = {
        "Goblin": 5, "Grzybolud": 5, "Wilk": 5,
        "Gnom": 5, "Spider": 10,
        "Troll": 20, "Golem": 20
    }

    if selected_land == "Mglista Puszcza":
        if enemy_type == "Troll":
            a, b = random.randint(6, 15), random.randint(6, 15)
        elif enemy_type == "Spider":
            a, b = random.randint(0, 20), random.randint(0, 20)
        else:
            a, b = random.randint(1, 10), random.randint(1, 10)
        question = f"Ile to {a} + {b}?"
        correct_answer = a + b
    elif selected_land == "Zamek":
        if enemy_type == "Gnom":
            a, b = random.randint(0, 10), random.randint(0, 10)
        question = f"Ile to {a} + {b}?"
        correct_answer = a + b
    elif selected_land == "Grzybowe Bagna":
        if enemy_type == "Troll":
            a, b = random.randint(6, 15), random.randint(6, 15)
        elif enemy_type == "Spider":
            a, b = random.randint(0, 20), random.randint(0, 20)
        else:
            a, b = random.randint(1, 10), random.randint(1, 10)

        if a < b:
            a, b = b, a
        question = f"Ile to {a} - {b}?"
        correct_answer = a - b
    elif selected_land == "Zimowe Królestwo":
        if enemy_type == "Wilk":
            while True:
                a = random.randint(2, 10)
                b = random.randint(2, 10)
                if a * b <= 15:
                    break
            question = f"Ile to {a} x {b}?"
            correct_answer = a * b
        elif enemy_type == "Golem":
            a = random.randint(2, 10)
            b = random.randint(2, min(30 // a, 10))
            question = f"Ile to {a} x {b}?"
            correct_answer = a * b
    else:
        a = random.randint(2, 10)
        b = random.randint(2, min(30 // a, 10))
        question = f"Ile to {a} x {b}?"
        correct_answer = a * b

    enemy_size = (300, 300) if enemy_type == "Troll" else (200, 200)
    enemy_sprite = enemy_sprites[enemy_type]
    enemy_sprite = pygame.transform.smoothscale(enemy_sprite, enemy_size)
    input_text = ""
    clock = pygame.time.Clock()
    battle_active = True
    font_large = pygame.font.SysFont(None, 48)
    font_small = pygame.font.SysFont(None, 36)

    def load_elixirs():
        elixir_buttons = []
        for idx, item in enumerate(player.inventory):
            if item == "Eliksir rozwiązania":
                elixir_path = "assets/items/elixir_solution.png"
            else:
                continue

            if os.path.exists(elixir_path):
                elixir_img = pygame.image.load(elixir_path)
                elixir_img = pygame.transform.scale(elixir_img, (50, 50))
                rect = pygame.Rect(50 + idx * 80, HEIGHT - 100, 50, 50)
                elixir_buttons.append((rect, item, elixir_img))
        return elixir_buttons

    elixir_buttons = load_elixirs()

    while battle_active:
        screen.fill((200, 200, 200))

        hero_sprite = player.battle_sprite
        hero_rect = hero_sprite.get_rect(center=(WIDTH // 4, HEIGHT // 2))
        enemy_rect = enemy_sprite.get_rect(center=(3 * WIDTH // 4, HEIGHT // 2))

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
                            player.coins += coin_rewards.get(enemy_type, 0)
                            show_message(f"Pokonałeś {enemy_type} i zdobyłeś {coin_rewards[enemy_type]} monet!")
                            return True
                        else:
                            player.health -= 20
                    except ValueError:
                        pass
                    input_text = ""
                    if player.health == 0:
                        show_message("Koniec gry!")
                        pygame.quit()
                else:
                    if event.unicode.isdigit():
                        input_text += event.unicode
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, item, _ in elixir_buttons:
                    if rect.collidepoint(event.pos):
                        if item == "Eliksir rozwiązania":
                            input_text = str(correct_answer)
                            player.inventory.remove(item)
                        elixir_buttons = load_elixirs()  # Update buttons

        screen.blit(hero_sprite, hero_rect)
        screen.blit(enemy_sprite, enemy_rect)

        health_bar_width = hero_sprite.get_width()
        health_bar_height = 10
        health_ratio = player.health / 100.0
        bar_x = hero_rect.x
        bar_y = hero_rect.y - 15
        pygame.draw.rect(screen, RED, (bar_x, bar_y, health_bar_width, health_bar_height))
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, health_bar_width * health_ratio, health_bar_height))

        for rect, _, elixir_img in elixir_buttons:
            screen.blit(elixir_img, rect.topleft)

        question_surface = font_large.render(question, True, BLACK)
        screen.blit(question_surface, (WIDTH // 2, HEIGHT // 4))
        input_prompt = "Odpowiedź: " + input_text
        input_surface = font_small.render(input_prompt, True, BLACK)
        screen.blit(input_surface, (WIDTH // 2, 3 * HEIGHT // 4))

        pygame.display.flip()
        clock.tick(30)
