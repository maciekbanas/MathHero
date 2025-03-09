import random
from constants import *
from assets import *
from player import Player
from enemy import Enemy
from choose_land import choose_land
from choose_character import choose_character
import items
from math_battle import math_battle
from messages import show_message

pygame.init()
pygame.display.set_caption("Math RPG")

forest_map = pygame.image.load(get_asset_path(os.path.join("maps", "treacherous_forest.png")))
forest_map = pygame.transform.scale(forest_map, (WIDTH, HEIGHT))

swamps_map = pygame.image.load(get_asset_path(os.path.join("maps", "mushroom_swamps.png")))
swamps_map = pygame.transform.scale(swamps_map, (WIDTH, HEIGHT))

hills_map = pygame.image.load(get_asset_path(os.path.join("maps", "steel_hills.png")))
hills_map = pygame.transform.scale(hills_map, (WIDTH, HEIGHT))

ice_realm_map = pygame.image.load(get_asset_path(os.path.join("maps", "ice_realm.png")))
ice_realm_map = pygame.transform.scale(ice_realm_map, (WIDTH, HEIGHT))

def return_to_land_selection():
    global running
    running = False
    main()

def main():
    global running
    player_character = choose_character()
    selected_land = choose_land()
    player = Player(WIDTH // 2, HEIGHT // 2, player_character)

    if selected_land == "Zdradzieckie Lasy":
        enemy_types = ["Goblin", "Gnom", "Troll"]
        background = forest_map
    elif selected_land == "Grzybowe Bagna":
        enemy_types = ["Gnom", "Grzybolud"]
        background = swamps_map
    elif selected_land == "Stalowe Wyżyny":
        enemy_types = ["Golem"]
        background = hills_map
    elif selected_land == "Zimowe Królestwo":
        enemy_types = ["Golem"]
        background = ice_realm_map

    enemies = [
        Enemy(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), random.choice(enemy_types))
        for _ in range(5)
    ]

    berries = items.generate_berries()

    clock = pygame.time.Clock()
    running = True
    while running:
        dt = clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                return_to_land_selection()

        keys = pygame.key.get_pressed()
        player.move(keys)
        player.animation.update(dt)

        screen.blit(background, (0, 0))

        current_image = player.animation.get_image()
        screen.blit(current_image, (player.x, player.y))

        pygame.draw.rect(screen, RED, (player.x, player.y - 15, 50, 5))
        pygame.draw.rect(screen, GREEN, (player.x, player.y - 15, 50 * (player.health / 100), 5))

        for enemy in enemies[:]:
            enemy.draw(screen)
            if enemy.check_collision(player):
                if math_battle(player, enemy.type, selected_land):
                    enemies.remove(enemy)
                    show_message("Pokonałeś wroga!")

        for berry in berries[:]:
            screen.blit(items.berry_image, (berry.x, berry.y))
            if pygame.Rect(player.x, player.y, 50, 50).colliderect(berry):
                if player.health < 100:
                    player.health = min(100, player.health + 20)
                    berries.remove(berry)

        if not enemies:
            show_message("Wygrałeś! Pokonałeś wszystkich przeciwników!")
            running = False

        font = pygame.font.SysFont(None, 40)
        back_text = font.render("Powrót", True, BLACK)
        text_width, text_height = back_text.get_size()
        padding = 20
        back_rect = pygame.Rect(WIDTH - text_width - padding, 20, text_width + padding, text_height + padding // 2)
        pygame.draw.rect(screen, GREY, back_rect)
        screen.blit(back_text, (back_rect.x + padding // 2, back_rect.y + padding // 4))

        pygame.display.flip()
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_rect.collidepoint(event.pos):
                    return_to_land_selection()

    pygame.quit()

if __name__ == "__main__":
    main()
