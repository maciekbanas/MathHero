import random
from constants import *
from assets import *
from player import Player
from enemy import Enemy
from choose_land import choose_land
from choose_character import choose_character
from items import Berry
from math_battle import math_battle
from messages import show_message
from inventory import *
from utils import draw_ui_buttons

pygame.init()
pygame.display.set_caption("Math RPG")

forest_map = pygame.image.load(get_asset_path(os.path.join("maps", "goblin_forest.png")))
forest_map = pygame.transform.scale(forest_map, (WIDTH, HEIGHT))

swamps_map = pygame.image.load(get_asset_path(os.path.join("maps", "mushroom_swamps.png")))
swamps_map = pygame.transform.scale(swamps_map, (WIDTH, HEIGHT))

hills_map = pygame.image.load(get_asset_path(os.path.join("maps", "steel_hills.png")))
hills_map = pygame.transform.scale(hills_map, (WIDTH, HEIGHT))

ice_realm_map = pygame.image.load(get_asset_path(os.path.join("maps", "ice_realm.png")))
ice_realm_map = pygame.transform.scale(ice_realm_map, (WIDTH, HEIGHT))

def draw_grid():
    """
    Draws a visible grid on the screen.
    """
    for x in range(0, WIDTH, 50):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 50):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (WIDTH, y))

def get_random_position_in_grid():
    """
    Returns a random position within a grid cell, ensuring entities do not overlap grid lines.
    """
    grid_x = random.randint(0, (WIDTH // 50) - 1) * 50
    grid_y = random.randint(0, (HEIGHT // 50) - 1) * 50
    return grid_x, grid_y

def return_to_land_selection():
    """
    Returns to the land selection screen.
    """
    global running
    running = False
    main()

def main():
    """
    Main game loop.
    """
    global running
    player_character = choose_character()
    selected_land = choose_land()
    player = Player(WIDTH // 2 // 50 * 50 + 25, HEIGHT // 2 // 50 * 50 + 25, player_character)

    if selected_land == "Goblinowe Lasy":
        enemy_types = ["Goblin", "Gnom", "Troll"]
        background = forest_map
    elif selected_land == "Grzybowe Bagna":
        enemy_types = ["Gnom", "Grzybolud"]
        background = swamps_map
    elif selected_land == "Stalowe Wyżyny":
        enemy_types = ["Golem"]
        background = hills_map
    elif selected_land == "Zimowe Królestwo":
        enemy_types = ["Wilk", "Golem"]
        background = ice_realm_map

    enemies = [
        Enemy(*get_random_position_in_grid(), random.choice(enemy_types))
        for _ in range(8)
    ]

    berries = [
        Berry(*get_random_position_in_grid()) for _ in range(3)
    ]

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
        player.update_position()
        player.animation.update(dt)

        screen.fill(WHITE)
        draw_grid()

        current_image = player.animation.get_image()
        screen.blit(current_image, (player.x - 25, player.y - 25))

        pygame.draw.rect(screen, RED, (player.x - 25, player.y - 40, 50, 5))
        pygame.draw.rect(screen, GREEN, (player.x - 25, player.y - 40, 50 * (player.health / 100), 5))

        for enemy in enemies[:]:
            enemy.draw(screen)
            if enemy.check_collision(player):
                if math_battle(player, enemy.type, selected_land):
                    enemies.remove(enemy)

        for berry in berries:
            berry.draw(screen)

        # Check if player collects berries
        for berry in berries[:]:  # Iterate over a copy to allow safe removal
            if berry.check_collision(player):
                if player.health < 100:
                    player.health = min(100, player.health + 20)
                    berries.remove(berry)  # Remove the berry after collecting

        if not enemies:
            show_message("Wygrałeś! Pokonałeś wszystkich przeciwników!")
            running = False

        inventory_button, back_button = draw_ui_buttons()
        pygame.display.flip()
        pygame.time.delay(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if inventory_button.collidepoint(event.pos):  # Detect click
                    show_inventory(player)
                if back_button.collidepoint(event.pos):
                    return_to_land_selection()

    pygame.quit()

if __name__ == "__main__":
    main()
