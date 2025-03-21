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

dark_tree_image = load_and_resize("obstacles/dark_forest_tree.png")
rock_image = load_and_resize("obstacles/rock.png")
icy_rock_image = load_and_resize("obstacles/icy_rock.png")
murky_swamp_image = load_and_resize("obstacles/murky_swamp.png")

class Obstacle:
    """ Represents an obstacle on the map. """
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (self.x * grid_size, self.y * grid_size))

def main():
    """
    Main game loop.
    """
    global running
    player_character = choose_character()

    # Initialize player's starting position
    world_position = (2, 2)
    player = Player(WIDTH // 2 // grid_size * grid_size + 40, HEIGHT // 2 // grid_size * grid_size + 40, player_character)
    map_player = Player(world_position[0] * 100, world_position[1] * 100, player_character)

    while True:

        selected_land, world_position = show_world_map(map_player, player, world_position)
        print(f"Gracz wszedł do: {selected_land}")

        if selected_land == "Mglista Puszcza":
            enemy_types = ["Goblin", "Spider", "Troll"]
            background_color = (85, 116, 119)
            background = forest_map
            obstacle_image = dark_tree_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }
        elif selected_land == "Zamek":
            enemy_types = []
            background_color = (244, 241, 232)
            background = castle_map
            obstacle_image = dark_tree_image
            obstacle_positions = {
                (10, 10)
            }
        elif selected_land == "Grzybowe Bagna":
            enemy_types = ["Spider", "Grzybolud"]
            background_color = (85, 116, 119)
            background = swamps_map
            obstacle_image = murky_swamp_image
            obstacle_positions = {
                (2, 2), (5, 6), (7, 2), (8, 8), (10, 6)
            }
        elif selected_land == "Stalowe Wyżyny":
            enemy_types = ["Golem"]
            background_color = (244, 241, 232)
            background = hills_map
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (8, 12), (4, 10), (9, 7)
            }
        elif selected_land == "Lodowa Kraina":
            enemy_types = ["Wilk", "Golem"]
            background_color = WHITE
            background = ice_realm_map
            obstacle_image = icy_rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }
        elif selected_land == "Łyse Łąki":
            enemy_types = ["Ork", "Goblin"]
            background_color = (244, 241, 232)
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }
        else:
            enemy_types = ["Wilk"]
            background_color = (244, 241, 232)
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }

        obstacles = [Obstacle(x, y, obstacle_image) for x, y in obstacle_positions]

        if enemy_types:
            enemies = [
                Enemy(*get_valid_random_position(obstacle_positions), random.choice(enemy_types))
                for _ in range(6)
            ]
        else:
            enemies = []

        if not selected_land == "Zamek":
            berries = [
                Berry(*get_valid_random_position(obstacle_positions)) for _ in range(3)
            ]
        else:
            berries = []

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
            # player.animation.update(dt)

            screen.fill(background_color)
            # screen.blit(background, (0, 0))
            draw_grid()

            current_image = player.sprite
            screen.blit(current_image, (player.x - 40, player.y - 40))

            pygame.draw.rect(screen, RED, (player.x - 40, player.y - 40, grid_size, 5))
            pygame.draw.rect(screen, GREEN, (player.x - 40, player.y - 40, grid_size * (player.health / 100), 5))

            for obstacle in obstacles:
                obstacle.draw(screen)

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

            if selected_land in ["Zamek", "Wieża Maga"]:
                merchant.draw(screen)
                if merchant.check_collision(player):
                    show_merchant_button = True
                else:
                    show_merchant_button = False
            else:
                show_merchant_button = False

            if show_merchant_button:
                merchant_button = draw_merchant_button()

            if not selected_land == "Zamek" and not enemies:
                show_message("Wygrałeś! Pokonałeś wszystkich przeciwników!")

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
                        running = False
                    if show_merchant_button and merchant_button.collidepoint(event.pos):
                        show_merchant_menu(player)
                elif event.type == pygame.KEYDOWN:
                    if show_merchant_button and event.key == pygame.K_RETURN:
                        show_merchant_menu(player)

    pygame.quit()


if __name__ == "__main__":
    main()
