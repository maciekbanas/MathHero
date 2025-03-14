from player import Player
from enemy import Enemy
from realms_map import show_world_map
from choose_character import choose_character
from items import Berry
from math_battle import math_battle
from inventory import *
from merchant import *

pygame.init()
pygame.display.set_caption("Math RPG")

forest_map = pygame.image.load(get_asset_path(os.path.join("maps", "dark_forest.png")))
forest_map = pygame.transform.scale(forest_map, (WIDTH, HEIGHT))

swamps_map = pygame.image.load(get_asset_path(os.path.join("maps", "mushroom_swamps.png")))
swamps_map = pygame.transform.scale(swamps_map, (WIDTH, HEIGHT))

hills_map = pygame.image.load(get_asset_path(os.path.join("maps", "steel_hills.png")))
hills_map = pygame.transform.scale(hills_map, (WIDTH, HEIGHT))

ice_realm_map = pygame.image.load(get_asset_path(os.path.join("maps", "ice_realm.png")))
ice_realm_map = pygame.transform.scale(ice_realm_map, (WIDTH, HEIGHT))

castle_map = pygame.image.load(get_asset_path(os.path.join("maps", "castle.png")))
castle_map = pygame.transform.scale(castle_map, (WIDTH, HEIGHT))

def main():
    """
    Main game loop.
    """
    global running
    player_character = choose_character()

    # Initialize player's starting position
    world_position = (2, 2)
    player = Player(WIDTH // 2 // 50 * 50 + 25, HEIGHT // 2 // 50 * 50 + 25, player_character)
    map_player = Player(world_position[0] * 100, world_position[1] * 100, player_character)

    while True:

        selected_land, world_position = show_world_map(map_player, player, world_position)
        print(f"Gracz wszedł do: {selected_land}")

        if selected_land == "Mglista Puszcza":
            enemy_types = ["Goblin", "Spider", "Troll"]
            background = forest_map
        elif selected_land == "Zamek":
            enemy_types = ["Gnom"]
            background = castle_map
        elif selected_land == "Grzybowe Bagna":
            enemy_types = ["Spider", "Grzybolud"]
            background = swamps_map
        elif selected_land == "Stalowe Wyżyny":
            enemy_types = ["Golem"]
            background = hills_map
        elif selected_land == "Lodowa Kraina":
            enemy_types = ["Wilk", "Golem"]
            background = ice_realm_map

        enemies = [
            Enemy(*get_random_position_in_grid(), random.choice(enemy_types))
            for _ in range(8)
        ]

        berries = [
            Berry(*get_random_position_in_grid()) for _ in range(3)
        ]

        merchant = Merchant()

        clock = pygame.time.Clock()
        running = True
        while running:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_BACKSPACE:
                    running = False

            keys = pygame.key.get_pressed()
            player.move(keys)
            player.update_position()
            player.animation.update(dt)

            screen.fill(WHITE)
            draw_grid()
            merchant.draw(screen)

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

            for berry in berries[:]:
                if berry.check_collision(player):
                    if player.health < 100:
                        player.health = min(100, player.health + 20)
                        berries.remove(berry)

            if merchant.check_collision(player):
                show_merchant_button = True
            else:
                show_merchant_button = False

            if show_merchant_button:
                merchant_button = draw_merchant_button()

            if not merchant.check_collision(player):
                merchant.interacted = False

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
                    if inventory_button.collidepoint(event.pos):
                        show_inventory(player)
                    if back_button.collidepoint(event.pos):
                        running = False  # Return to world map
                    if show_merchant_button and merchant_button.collidepoint(event.pos):
                        show_merchant_menu(player)

    pygame.quit()


if __name__ == "__main__":
    main()
