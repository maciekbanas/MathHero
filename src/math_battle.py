from assets import enemy_sprites
from constants import *
from messages import show_message


def math_battle(player, enemy_type, selected_land):
    """
    Wyświetla ekran walki z pytaniem matematycznym zależnym od wybranej krainy.
    """
    import random

    if selected_land == "Goblinowe Lasy":
        if enemy_type == "Troll":
            a, b = random.randint(6, 15), random.randint(6, 15)
        elif enemy_type == "Gnom":
            a, b = random.randint(0, 20), random.randint(0, 20)
        else:
            a, b = random.randint(1, 10), random.randint(1, 10)
        question = f"Ile to {a} + {b}?"
        correct_answer = a + b
    elif selected_land == "Grzybowe Bagna":
        if enemy_type == "Troll":
            a, b = random.randint(6, 15), random.randint(6, 15)
        elif enemy_type == "Gnom":
            a, b = random.randint(0, 20), random.randint(0, 20)
        else:
            a, b = random.randint(1, 10), random.randint(1, 10)

        if a < b:
            a, b = b, a

        question = f"Ile to {a} - {b}?"
        correct_answer = a - b
    else:
        a = random.randint(2, 10)
        b = random.randint(2, min(30 // a, 10))
        question = f"Ile to {a} x {b}?"
        correct_answer = a * b

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

        hero_sprite = player.battle_sprite
        screen.fill((200, 200, 200))
        hero_rect = hero_sprite.get_rect(center=(WIDTH // 4, HEIGHT // 2))
        enemy_rect = enemy_sprite.get_rect(center=(3 * WIDTH // 4, HEIGHT // 2))
        screen.blit(hero_sprite, hero_rect)
        screen.blit(enemy_sprite, enemy_rect)

        health_bar_width = hero_sprite.get_width()
        health_bar_height = 10
        health_ratio = player.health / 100.0
        bar_x = hero_rect.x
        bar_y = hero_rect.y - 15
        pygame.draw.rect(screen, RED, (bar_x, bar_y, health_bar_width, health_bar_height))
        pygame.draw.rect(screen, GREEN, (bar_x, bar_y, health_bar_width * health_ratio, health_bar_height))

        question_surface = font_large.render(question, True, BLACK)
        question_rect = question_surface.get_rect(center=(WIDTH // 2, HEIGHT // 4))
        screen.blit(question_surface, question_rect)

        input_prompt = "Odpowiedź: " + input_text
        input_surface = font_small.render(input_prompt, True, BLACK)
        input_rect = input_surface.get_rect(center=(WIDTH // 2, 3 * HEIGHT // 4))
        screen.blit(input_surface, input_rect)

        pygame.display.flip()
        clock.tick(30)
