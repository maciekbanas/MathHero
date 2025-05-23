from player import Player
from enemy import Enemy
from realms_map import show_world_map
from choose_character import choose_character
from items import Berry
from math_battle import math_battle
from inventory import *
from merchant import *
from blacksmith import *
from goblin_aviator import *
from save_load import *
from start import start_screen

pygame.init()
pygame.display.set_caption("Math RPG")

dark_tree_image = load_and_resize("obstacles/dark_forest_tree.png")
rock_image = load_and_resize("obstacles/rock.png")
icy_rock_image = load_and_resize("obstacles/icy_rock.png")
murky_swamp_image = load_and_resize("obstacles/murky_swamp.png")
tree_image = load_and_resize("obstacles/tree.png")

magma_rock_image = load_and_resize("obstacles/magma_rock.png")

class Obstacle:
    """ Represents an obstacle on the map. """
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

    def draw(self, screen):
        screen.blit(self.image, (self.x * grid_size, self.y * grid_size))

bridge_background_image = load_and_resize("maps/Bridge.png", WIDTH, HEIGHT)
forest_background_image = load_and_resize("maps/Forest.png", WIDTH, HEIGHT)
def main(player, world_position = None, selected_land = None, completed_realms = set()):
    """
    Main game loop.
    """
    global running

    if world_position is None:
        if player_character == "Czarodziejka":
            world_position = (3, 2)
        elif player_character == "Rabbit":
            world_position = (0, 1)
        elif player_character == "Kocias":
            world_position = (0, 1)
        elif player_character == "Wilczas":
            world_position = (1, 1)

    map_player = Player(world_position[0] * 100, world_position[1] * 100, player_character)

    while True:

        selected_land, world_position = show_world_map(map_player, player, completed_realms, world_position)
        print(f"Gracz wszedł do: {selected_land}")

        if selected_land == "Lasy":
            enemy_types = ["Gnom", "Grzybołak", "Bees", "Wilk"]
            enemies_number = 6
            background_color = (244, 241, 232)
            obstacle_image = tree_image
            obstacle_positions = {
                (2, 2), (3, 4), (3, 5), (5, 6), (7, 2), (2, 8),
                (6, 6), (6, 7), (7, 7), (10, 8),
                (13, 5), (13, 6),
                (15, 1), (15, 2), (16, 2), (16, 3)
            }
        elif selected_land == "Bór":
            enemy_types = ["Gnom", "Grzybołak", "Wilk", "Bees", "Niedzwiedz"]
            enemies_number = 6
            background_color = (244, 241, 232)
            obstacle_image = tree_image
            obstacle_positions = {
                (2, 2), (3, 4), (3, 5), (5, 6), (7, 2), (2, 8),
                (6, 6), (6, 7), (7, 7), (10, 8),
                (13, 5), (13, 6),
                (15, 1), (15, 2), (16, 2), (16, 3)
            }
        elif selected_land in ["Dzikie Bory"]:
            enemy_types = ["Gnom", "Grzybołak", "Niedzwiedz", "Goblin"]
            enemies_number = 7
            background_color = (244, 241, 232)
            obstacle_image = tree_image
            obstacle_positions = {
                (2, 2), (3, 4), (3, 5), (5, 6), (7, 2), (2, 8),
                (6, 6), (6, 7), (7, 7), (10, 8),
                (13, 5), (13, 6),
                (15, 1), (15, 2), (16, 2), (16, 3)
            }
        elif selected_land == "Łąki":
            enemy_types = ["Gnom", "Bees"]
            enemies_number = 5
            background_color = (244, 241, 232)
            obstacle_image = tree_image
            obstacle_positions = {
                (5, 6)
            }
        elif selected_land == "Mglista Puszcza":
            enemy_types = ["Goblin", "Spider", "Troll"]
            enemies_number = 8
            background_color = (85, 116, 119)
            obstacle_image = dark_tree_image
            obstacle_positions = {
                (3, 4), (3, 5), (5, 6), (7, 2), (2, 8),
                (6, 6), (6, 7), (7, 7),
            }
        elif selected_land == "Zamek":
            enemy_types = []
            enemies_number = 0
            background_color = (244, 241, 232)
            obstacle_image = tree_image
            obstacle_positions = {
                (10, 4)
            }
        elif selected_land == "Miasto":
            enemy_types = []
            enemies_number = 0
            background_color = (244, 241, 232)
            obstacle_image = tree_image
            obstacle_positions = {
                (8, 6), (6, 8), (10, 3)
            }
        elif selected_land == "Górska Wies":
            enemy_types = []
            enemies_number = 0
            background_color = (244, 241, 232)
            obstacle_image = tree_image
            obstacle_positions = {
                (8, 6), (6, 8), (10, 3)
            }
        elif selected_land == "Złoty Las":
            enemy_types = []
            enemies_number = 0
            background_color = (244, 241, 232)
            obstacle_image = tree_image
            obstacle_positions = {
                (10, 10), (3, 3), (4, 3), (7, 8)
            }
        elif selected_land == "Starożytne Ruiny":
            enemy_types = ["Grzybołak", "Niedzwiedz", "Troll"]
            enemies_number = 6
            background_color = (244, 241, 232)
            obstacle_image = tree_image
            obstacle_positions = {
                (10, 10), (3, 3), (4, 3), (7, 8)
            }
        elif selected_land == "Grzybowe Bagna":
            enemy_types = ["Spider", "Grzybolud"]
            enemies_number = 8
            background_color = (85, 116, 119)
            obstacle_image = murky_swamp_image
            obstacle_positions = {
                (2, 2), (5, 6), (7, 2), (8, 8), (10, 6)
            }
        elif selected_land == "Stalowe Wyżyny":
            enemy_types = ["Golem"]
            enemies_number = 5
            background_color = (244, 241, 232)
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (8, 12), (4, 10), (9, 7)
            }
        elif selected_land == "Lodowa Kraina":
            enemy_types = ["Wilk"]
            enemies_number = 8
            background_color = WHITE
            obstacle_image = icy_rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }
        elif selected_land == "Most":
            enemy_types = ["Wilk"]
            enemies_number = 4
            background_color = (244, 241, 232)
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }
            guard_image = load_and_resize("places/guard_tower.png", 200, 200)
            guard_position = (8, 4)
        elif selected_land == "Łyse Łąki":
            enemy_types = ["Ork", "Goblin"]
            enemies_number = 7
            background_color = (244, 241, 232)
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }
        elif selected_land == "Krwawe Wzgórza":
            enemy_types = ["Ork"]
            enemies_number = 10
            background_color = (244, 241, 232)
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }
        elif selected_land == "Dzikie Brzegi":
            enemy_types = ["Ork", "Goblin"]
            enemies_number = 7
            background_color = (244, 241, 232)
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }
        elif selected_land == "Tajemnicza Zatoka":
            enemy_types = ["Upiór"]
            enemies_number = 8
            background_color = (244, 241, 232)
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }
        elif selected_land == "Wyschły Wąwóz":
            enemy_types = ["Ork", "Szkielet"]
            enemies_number = 7
            background_color = (244, 241, 232)
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }
        elif selected_land == "Szare Skały":
            enemy_types = ["Szkielet"]
            enemies_number = 7
            background_color = (244, 241, 232)
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6),
                (10, 8), (10, 9), (8, 2), (8, 4), (9, 6),
                (16, 4), (15, 7), (18, 9)
            }
        elif selected_land == "Wieża Maga":
            enemy_types = ["Mag", "Mag Ognia", "Golem"]
            enemies_number = 8
            background_color = (244, 241, 232)
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }
        elif selected_land == "Magmowe Wzgórza":
            enemy_types = ["Mag Ognia", "Magmowy Golem"]
            enemies_number = 8
            background_color = (80, 36, 20)
            obstacle_image = magma_rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6),
                (10, 10), (10, 5), (12, 8), (15, 7),
                (9, 2), (8, 3), (14, 4), (18, 3)
            }
        else:
            enemy_types = ["Wilk"]
            enemies_number = 6
            background_color = (244, 241, 232)
            obstacle_image = rock_image
            obstacle_positions = {
                (3, 4), (5, 6), (7, 2), (2, 8), (6, 6)
            }

        obstacles = [Obstacle(x, y, obstacle_image) for x, y in obstacle_positions]

        if enemy_types:
            enemies = [
                Enemy(*get_valid_random_position(obstacle_positions), random.choice(enemy_types))
                for _ in range(enemies_number)
            ]
        else:
            enemies = []

        if not selected_land in ["Zamek", "Stalowe Wyżyny", "Wyschły Wąwóz", "Szare Skały", "Wieża Maga", "Magmowe Wzgórza"]:
            berries = [
                Berry(*get_valid_random_position(obstacle_positions)) for _ in range(3)
            ]
        else:
            berries = []

        merchant = Merchant()
        aviator = Aviator()
        blacksmith = Blacksmith()

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
            player.move(keys, obstacle_positions)
            player.update_position()
            # player.animation.update(dt)

            screen.fill(background_color)
            # screen.blit(background, (0, 0))
            draw_grid()

            current_image = player.sprite
            screen.blit(current_image, (player.x - 40, player.y - 40))

            pygame.draw.rect(screen, RED, (player.x - 40, player.y - 50, grid_size, 5))
            pygame.draw.rect(screen, GREEN, (player.x - 40, player.y - 50, grid_size * (player.health / 100), 5))

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

            show_merchant_button = False
            show_aviator_button = False
            show_blacksmith_button = False

            if selected_land == "Most":
                screen.blit(guard_image, (guard_position[0] * grid_size, guard_position[1] * grid_size))

            if selected_land in ["Zamek", "Wieża Maga"]:
                merchant.draw(screen)
                if merchant.check_collision(player):
                    show_merchant_button = True
                else:
                    show_merchant_button = False
            elif selected_land == "Miasto":
                aviator.draw(screen)
                blacksmith.draw(screen)
                if blacksmith.check_collision(player):
                    show_blacksmith_button = True
                else:
                    show_blacksmith_button = False

                if aviator.check_collision(player):
                    show_aviator_button = True
                else:
                    show_aviator_button = False
            else:
                show_merchant_button = False
                show_aviator_button = False
                show_blacksmith_button = False

            if show_merchant_button:
                merchant_button = draw_merchant_button()

            if show_aviator_button:
                aviator_button = draw_aviator_button()

            if show_blacksmith_button:
                blacksmith_button = draw_blacksmith_button()

            inventory_button, back_button = draw_ui_buttons()
            pygame.display.flip()
            pygame.time.delay(30)

            if not enemies and selected_land not in ["Zamek", "Złoty Las", "Miasto", "Górska Wies"]:
                completed_realms.add(selected_land)
                pygame.time.delay(1000)
                show_message("Wrogowie pokonani!")

            aviator_output = ""

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
                    if show_aviator_button and aviator_button.collidepoint(event.pos):
                        aviator_output = show_aviator_menu(player)
                        if (aviator_output != ""):
                            running = False
                            if (aviator_output == "wizard_tower"):
                                world_position = (0, 7)
                            elif (aviator_output == "magma_hills"):
                                world_position = (4, 7)
                            map_player = Player(world_position[0] * 100, world_position[1] * 100, player_character)
                            selected_land, world_position, completed_realms = show_world_map(map_player, player,
                                                                           completed_realms, world_position)
                    if show_blacksmith_button and blacksmith_button.collidepoint(event.pos):
                        show_blacksmith_menu(player)
                elif event.type == pygame.KEYDOWN:
                    if show_merchant_button and event.key == pygame.K_RETURN:
                        show_merchant_menu(player)
                    if show_aviator_button and event.key == pygame.K_RETURN:
                        aviator_output = show_aviator_menu(player)
                        if (aviator_output != ""):
                            running = False
                            if (aviator_output == "wizard_tower"):
                                world_position = (0, 7)
                            elif (aviator_output == "magma_hills"):
                                world_position = (4, 7)
                            map_player = Player(world_position[0] * 100, world_position[1] * 100, player_character)
                            selected_land, world_position, completed_realms = show_world_map(map_player, player,
                                                                           completed_realms, world_position)
                    if show_blacksmith_button and event.key == pygame.K_RETURN:
                        show_blacksmith_menu(player)
                    if event.key == pygame.K_s:
                        save_game_state(player, world_position, selected_land, completed_realms)
                        show_message("Zapisany stan gry!")
                    if event.key == pygame.K_l:
                        state = load_game_state()
                        show_message("Załadowano grę!")
                        if state is not None:
                            player.x = state["player"]["x"]
                            player.y = state["player"]["y"]
                            player.health = state["player"]["health"]
                            player.xp = state["player"]["xp"]
                            player.coins = state["player"]["coins"]
                            player.character = state["player"]["character"]
                            player.inventory = state["player"]["inventory"]
                            world_position = state["world_position"]
                            selected_land = state["selected_land"]
                            completed_realms = set(state["completed_realms"])

    pygame.quit()


if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Math RPG")

    selection = start_screen(screen)
    if selection == "new":
        player_character = choose_character()
        player = Player(WIDTH // 2 // grid_size * grid_size + 40, HEIGHT // 2 // grid_size * grid_size + 40,
                        player_character)
        main(player)
    else:
        state = load_game_state()
        show_message("Załadowano grę!")
        if state is not None:
            player_character = state["player"]["character"]
            player = Player(WIDTH // 2 // grid_size * grid_size + 40, HEIGHT // 2 // grid_size * grid_size + 40,
                            player_character)
            player.x = state["player"]["x"]
            player.y = state["player"]["y"]
            player.health = state["player"]["health"]
            player.xp = state["player"]["xp"]
            player.coins = state["player"]["coins"]
            player.character = state["player"]["character"]
            player.inventory = state["player"]["inventory"]
            world_position = state["world_position"]
            selected_land = state["selected_land"]
            completed_realms = set(state["completed_realms"])

            main(player, world_position, selected_land, completed_realms)