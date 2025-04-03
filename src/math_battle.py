from assets import enemy_sprites
from constants import *
from utils import show_message
import os

import pygame
import math

def draw_clock(surface, center, radius, hour, minute):
    pygame.draw.circle(surface, (255, 255, 255), center, radius)
    pygame.draw.circle(surface, (0, 0, 0), center, radius, 3)

    for h in range(12):
        angle = math.radians(h * 30 - 90)  # co 30 stopni
        x = center[0] + int(math.cos(angle) * (radius - 10))
        y = center[1] + int(math.sin(angle) * (radius - 10))
        pygame.draw.circle(surface, (0, 0, 0), (x, y), 4)

    # Wskazówka minutowa
    minute_angle = math.radians(minute * 6 - 90)  # 360/60 = 6 stopni na minutę
    minute_x = center[0] + int(math.cos(minute_angle) * (radius - 20))
    minute_y = center[1] + int(math.sin(minute_angle) * (radius - 20))
    pygame.draw.line(surface, (0, 0, 0), center, (minute_x, minute_y), 3)

    # Wskazówka godzinowa
    hour_angle = math.radians((hour % 12 + minute / 60) * 30 - 90)  # 360/12 = 30 stopni na godzinę
    hour_x = center[0] + int(math.cos(hour_angle) * (radius - 40))
    hour_y = center[1] + int(math.sin(hour_angle) * (radius - 40))
    pygame.draw.line(surface, (0, 0, 0), center, (hour_x, hour_y), 5)

    # Środek zegara
    pygame.draw.circle(surface, (0, 0, 0), center, 5)

def math_battle(player, enemy_type, selected_land):
    """
    Displays the battle screen and awards coins for winning.
    """
    import random

    hour_input = ""
    minute_input = ""
    active_field = "hour"
    max_length = 2

    coin_rewards = {
        "Bees": 0,
        "Goblin": 10, "Grzybołak": 5, "Grzybolud": 5, "Wilk": 5,
        "Niedzwiedz": 0,
        "Gnom": 5, "Spider": 10, "Szkielet": 10,
        "Troll": 20, "Golem": 20, "Ork": 20, "Upiór": 10,
        "Mag": 30, "Magmowy Golem": 30
    }
    xp_rewards = {
        "Bees": 5,
        "Goblin": 10, "Grzybolud": 5, "Grzybołak": 5, "Wilk": 5,
        "Niedzwiedz": 10,
        "Gnom": 5, "Spider": 10, "Szkielet": 10,
        "Troll": 20, "Golem": 20, "Ork": 20, "Upiór": 20,
        "Mag": 50, "Magmowy Golem": 50
    }

    damage = {
        "Bees": 5,
        "Gnom": 10,
        "Wilk": 10, "Goblin": 10, "Grzybołak": 10, "Grzybolud": 10,
        "Spider": 15, "Szkielet": 15,
        "Niedzwiedz": 20, "Upiór": 20,
        "Troll": 30, "Golem": 30, "Ork": 20,
        "Mag": 30, "Magmowy Golem": 40
    }

    if enemy_type == "Gnom":
        a, b = random.randint(1, 10), random.randint(1, 10)
        question = f"Ile to {a} + {b}?"
        correct_answer = a + b
    elif enemy_type == "Bees":
        a, b = random.randint(1, 5), random.randint(1, 5)
        question = f"Ile to {a} + {b}?"
        correct_answer = a + b
    elif enemy_type == "Niedzwiedz":
        a, b, c = random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)
        question = f"Ile to {a} + {b} + {c}?"
        correct_answer = a + b + c
    elif enemy_type == "Goblin":
        a, b = random.randint(1, 4), random.randint(1, 4)
        question = f"Ile to {a} x {b}?"
        correct_answer = a * b
    elif enemy_type == "Troll":
        a, b = random.randint(10, 30), random.randint(10, 30)
        question = f"Ile to {a} + {b}?"
        correct_answer = a + b
    elif enemy_type == "Grzybołak":
        a, b = random.randint(1, 10), random.randint(0, 5)
        if a < b:
            a, b = b, a
        question = f"Ile to {a} - {b}?"
        correct_answer = a - b
    elif enemy_type == "Grzybolud":
        a, b = random.randint(6, 30), random.randint(6, 20)
        if a < b:
            a, b = b, a
        question = f"Ile to {a} - {b}?"
        correct_answer = a - b
    elif enemy_type == "Golem":
        a = random.randint(2, 10)
        b = random.randint(2, min(30 // a, 10))
        question = f"Ile to {a} x {b}?"
        correct_answer = a * b
    elif enemy_type == "Ork":
        a, b = random.randint(1, 10), random.randint(1, 10)
        question = f"Ile to {a} x {b}?"
        correct_answer = a * b
    elif enemy_type == "Szkielet":
        a, b = random.randint(1, 5), random.randint(1, 5)
        question = f"Ile to {a} x {b}?"
        correct_answer = a * b
    elif enemy_type in ["Upiór", "Mag Ognia", "Magmowy Golem"]:
        if enemy_type == "Mag Ognia":
            divisor = random.randint(2, 10)
            quotient = random.randint(1, 5)
        elif enemy_type == "Magmowy Golem":
            divisor = random.randint(2, 20)
            quotient = random.randint(1, 5)
        else:
            divisor = random.randint(2, 5)
            quotient = random.randint(1, 5)
        dividend = divisor * quotient
        question = f"Ile to {dividend} ÷ {divisor}?"
        correct_answer = quotient
    elif enemy_type == "Mag":
        hour = random.randint(1, 12)
        minute = random.choice([0, 15, 30, 45])
        question = "Która jest godzina na zegarze?"
        correct_answer = f"{hour:02}:{minute:02}"
        clock_time = (hour, minute)
    else:
        a = random.randint(2, 10)
        b = random.randint(2, min(30 // a, 10))
        question = f"Ile to {a} + {b}?"
        correct_answer = a + b

    enemy_size = (300, 300) if enemy_type in ["Troll", "Golem", "Magmowy Golem"] else (200, 200)
    enemy_sprite = enemy_sprites[enemy_type]
    enemy_sprite = pygame.transform.smoothscale(enemy_sprite, enemy_size)
    input_text = ""
    clock = pygame.time.Clock()
    battle_active = True
    font_large = pygame.font.SysFont(None, 48)
    font_small = pygame.font.SysFont(None, 36)

    if "Tarcza" in player.inventory and not hasattr(player, "shield_health"):
        player.shield_health = 40

    def load_items():
        elixir_buttons = []
        for idx, item in enumerate(player.inventory):
            if item == "Eliksir rozwiązania":
                item_path = "assets/items/elixir_solution.png"
            elif item == "Tarcza":
                item_path = "assets/items/shield.png"
            else:
                continue

            if os.path.exists(item_path):
                elixir_img = pygame.image.load(item_path)
                elixir_img = pygame.transform.smoothscale(elixir_img, (80, 80))
                rect = pygame.Rect(50 + idx * 80, HEIGHT - 100, 80, 80)
                elixir_buttons.append((rect, item, elixir_img))
        return elixir_buttons

    elixir_buttons = load_items()

    while battle_active:
        screen.fill((200, 200, 200))

        hero_sprite = player.battle_sprite
        hero_rect = hero_sprite.get_rect(center=(WIDTH // 4, HEIGHT // 2))
        enemy_rect = enemy_sprite.get_rect(center=(3 * WIDTH // 4, HEIGHT // 2))

        if enemy_type == "Mag":
            draw_clock(screen, (WIDTH // 2, HEIGHT // 2), 120, *clock_time)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if enemy_type == "Mag":
                        if active_field == "minute" and minute_input:
                            minute_input = minute_input[:-1]
                        elif active_field == "hour" and hour_input:
                            hour_input = hour_input[:-1]
                    else:
                        input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    try:
                        if enemy_type == "Mag":
                            user_answer = f"{int(hour_input):02}:{int(minute_input):02}"
                        else:
                            user_answer = int(input_text)
                        if user_answer == correct_answer:
                            player.coins += coin_rewards.get(enemy_type, 0)
                            player.xp += xp_rewards.get(enemy_type, 0)
                            show_message(
                                f"Pokonałeś {enemy_type}. Zdobyłeś {coin_rewards[enemy_type]} monet oraz {xp_rewards[enemy_type]} punktów XP!")
                            return True
                        else:
                            dmg = damage[enemy_type]
                            if "Tarcza" in player.inventory and hasattr(player,
                                                                        "shield_health") and player.shield_health > 0:
                                if player.shield_health >= dmg:
                                    player.shield_health -= dmg
                                    if player.shield_health == 0:
                                        player.inventory.remove("Tarcza")
                                        show_message("Tarcza uległa zniszczeniu!")
                                        elixir_buttons = load_items()
                                else:
                                    overflow = dmg - player.shield_health
                                    player.shield_health = 0
                                    player.inventory.remove("Tarcza")
                                    show_message("Tarcza uległa zniszczeniu!")
                                    elixir_buttons = load_items()
                                    player.health -= overflow
                            else:
                                player.health -= dmg
                    except ValueError:
                        pass
                    input_text = ""
                    if player.health <= 0:
                        show_message("Koniec gry!")
                        pygame.quit()
                else:
                    if event.unicode.isdigit():
                        if enemy_type == "Mag":
                            if active_field == "hour" and len(hour_input) < max_length:
                                hour_input += event.unicode
                                if len(hour_input) == max_length:
                                    active_field = "minute"
                            elif active_field == "minute" and len(minute_input) < max_length:
                                minute_input += event.unicode
                        else:
                            input_text += event.unicode
                    elif event.key in [pygame.K_RIGHT, pygame.K_LEFT]:
                        if active_field == "hour":
                            active_field = "minute"
                        else:
                            active_field = "hour"
            if event.type == pygame.MOUSEBUTTONDOWN:
                for rect, item, _ in elixir_buttons:
                    if rect.collidepoint(event.pos):
                        if item == "Eliksir rozwiązania":
                            input_text = str(correct_answer)
                            player.inventory.remove(item)
                        elixir_buttons = load_items()

        screen.blit(hero_sprite, hero_rect)
        screen.blit(enemy_sprite, enemy_rect)

        health_bar_width = hero_sprite.get_width()
        health_bar_height = 10
        health_ratio = player.health / 100.0
        bar_x = hero_rect.x
        bar_y = hero_rect.y - 15
        pygame.draw.rect(screen, RED, (bar_x, bar_y, health_bar_width, health_bar_height))
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, health_bar_width * health_ratio, health_bar_height))

        if "Tarcza" in player.inventory and hasattr(player, "shield_health") and player.shield_health > 0:
            shield_bar_width = hero_sprite.get_width()
            shield_bar_height = 10
            shield_ratio = player.shield_health / 40.0
            shield_bar_x = hero_rect.x
            shield_bar_y = hero_rect.y - 30
            pygame.draw.rect(screen, (128, 128, 128), (shield_bar_x, shield_bar_y, shield_bar_width, shield_bar_height))
            pygame.draw.rect(screen, (0, 0, 255),
                             (shield_bar_x, shield_bar_y, shield_bar_width * shield_ratio, shield_bar_height))

        for rect, _, elixir_img in elixir_buttons:
            screen.blit(elixir_img, rect.topleft)

        question_surface = font_large.render(question, True, BLACK)
        screen.blit(question_surface, (WIDTH // 2, HEIGHT // 4))
        if enemy_type == "Mag":
            input_prompt = f"Odpowiedź: {hour_input: <2}:{minute_input: <2}"
            color = (0, 0, 0)
            if active_field == "hour":
                input_prompt = f"[{hour_input: <2}]:{minute_input: <2}"
            else:
                input_prompt = f"{hour_input: <2}:[{minute_input: <2}]"
            input_surface = font_small.render(input_prompt, True, BLACK)
            screen.blit(input_surface, (WIDTH // 2 - 50, 3 * HEIGHT // 4))
        else:
            input_prompt = "Odpowiedź: " + input_text
            input_surface = font_small.render(input_prompt, True, BLACK)
            screen.blit(input_surface, (WIDTH // 2, 3 * HEIGHT // 4))

        pygame.display.flip()
        clock.tick(30)
