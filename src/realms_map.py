import pygame

from utils import *
from inventory import show_inventory

class WorldMap:
    def __init__(self, player, player_game, start_position=(1, 1)):
        self.grid_size = 100
        self.cols, self.rows = 8, 8
        self.map_width = self.cols * self.grid_size
        self.map_height = self.rows * self.grid_size
        self.player = player
        self.player_game = player_game
        self.start_position = start_position
        self.player.x, self.player.y = self.start_position[0] * self.grid_size, self.start_position[1] * self.grid_size

        self.lands = {
            "Zamek": (1, 1),
            "Złoty Las": (4, 2),
            "Wieża Maga": (0, 7),
            "Łyse Łąki": (1, 4),
            "Grzybowe Bagna": (2, 4),
            "Szare Skały": (1, 6),
            "Wyschły Wąwóz": (1, 7),
            "Mglista Puszcza": (2, 3),
            "Stalowe Wyżyny": (0, 6),
            "Lodowa Kraina": (7, 0)
        }
        castle_image = pygame.image.load(get_asset_path("lands/castle.png"))
        wizard_tower_image = pygame.image.load(get_asset_path("lands/wizard_tower.png"))
        bald_meadows_image = pygame.image.load(get_asset_path("lands/bald_meadows.png"))
        goblin_forest_image = pygame.image.load(get_asset_path("lands/dark_forest.png"))
        mushroom_swamps_image = pygame.image.load(get_asset_path("lands/mushroom_swamps.png"))
        steel_hills_image = pygame.image.load(get_asset_path("lands/steel_hills.png"))
        ice_realm_image = pygame.image.load(get_asset_path("lands/ice_realm.png"))
        grey_rocks_image = pygame.image.load(get_asset_path("lands/grey_rocks.png"))
        dry_ravine_image = pygame.image.load(get_asset_path("lands/dry_ravine.png"))
        golden_forest_image = pygame.image.load(get_asset_path("lands/golden_forest.png"))

        self.land_images = {
            "Zamek": pygame.transform.smoothscale(castle_image, (100, 100)),
            "Złoty Las": pygame.transform.smoothscale(golden_forest_image, (100, 100)),
            "Wieża Maga": pygame.transform.smoothscale(wizard_tower_image, (100, 100)),
            "Łyse Łąki": pygame.transform.smoothscale(bald_meadows_image, (100, 100)),
            "Mglista Puszcza": pygame.transform.smoothscale(goblin_forest_image, (100, 100)),
            "Grzybowe Bagna": pygame.transform.smoothscale(mushroom_swamps_image, (100, 100)),
            "Stalowe Wyżyny": pygame.transform.smoothscale(steel_hills_image, (100, 100)),
            "Lodowa Kraina": pygame.transform.smoothscale(ice_realm_image, (100, 100)),
            "Szare Skały": pygame.transform.smoothscale(grey_rocks_image, (100, 100)),
            "Wyschły Wąwóz": pygame.transform.smoothscale(dry_ravine_image, (100, 100))
        }

        realm_dim = 700

        self.realm_images = {
            "Zamek": pygame.transform.smoothscale(castle_image, (realm_dim, realm_dim)),
            "Złoty Las": pygame.transform.smoothscale(golden_forest_image, (realm_dim, realm_dim)),
            "Wieża Maga": pygame.transform.smoothscale(wizard_tower_image, (realm_dim, realm_dim)),
            "Łyse Łąki": pygame.transform.smoothscale(bald_meadows_image, (realm_dim, realm_dim)),
            "Mglista Puszcza": pygame.transform.smoothscale(goblin_forest_image, (realm_dim, realm_dim)),
            "Grzybowe Bagna": pygame.transform.smoothscale(mushroom_swamps_image, (realm_dim, realm_dim)),
            "Stalowe Wyżyny": pygame.transform.smoothscale(steel_hills_image, (realm_dim, realm_dim)),
            "Lodowa Kraina": pygame.transform.smoothscale(ice_realm_image, (realm_dim, realm_dim)),
            "Szare Skały": pygame.transform.smoothscale(grey_rocks_image, (realm_dim, realm_dim)),
            "Wyschły Wąwóz": pygame.transform.smoothscale(dry_ravine_image, (realm_dim, realm_dim))
        }

        self.land_descriptions = {
            "Zamek": "Home sweet home",
            "Złoty Las": "Zamieszkane przez elfy, gotowe pomóc.",
            "Wieża Maga": "",
            "Łyse Łąki": "Pełne niebezpiecznych maruderów.",
            "Mglista Puszcza": "Gęste, tajemnicze lasy pełne goblinów, gnomów i trolli. Idealne do ćwiczenia dodawania.",
            "Grzybowe Bagna": "Mroczne, wilgotne bagna zamieszkałe przez gobliny i tajemnicze grzyboludy. Nauka odejmowania jest kluczowa, by przetrwać.",
            "Stalowe Wyżyny": "Wysokie wyżyny zamieszkałe przez potężne golemy. Tutaj nauczysz się mnożenia.",
            "Szare Skały": "Opustoszone, na pierwszy rzut oka.",
            "Wyschły Wąwóz": "Zamieszkany przez wygłodniałe ogry...",
            "Lodowa Kraina": "Mroźna i tajemnicza kraina, której mieszkańcy posługują się liczbami w niezwykły sposób."
        }

        for land, (col, row) in self.lands.items():
            if self.player.x == col * self.grid_size and self.player.y == row * self.grid_size:
                self.selected_land = land
                break

        self.enter_button = pygame.Rect(WIDTH / 2, HEIGHT - 60, 220, 40)
        self.inventory_button = pygame.Rect(20, HEIGHT - 60, 150, 40)
        self.quit_button = pygame.Rect(WIDTH - 170, HEIGHT - 60, 150, 40)

    def draw(self, screen):
        screen.fill((50, 50, 50))
        for col in range(self.cols):
            for row in range(self.rows):
                pygame.draw.rect(screen, (100, 100, 100),
                                 (col * self.grid_size, row * self.grid_size, self.grid_size, self.grid_size), 1)

        for land, (col, row) in self.lands.items():
            screen.blit(self.land_images[land], (col * self.grid_size, row * self.grid_size))

        screen.blit(self.player.realm_sprite, (self.player.x, self.player.y))

        if self.selected_land:
            screen.blit(self.realm_images[self.selected_land], (WIDTH / 2 + 40, 20))
            font = pygame.font.SysFont(None, 40)
            land_text = font.render(self.selected_land, True, WHITE)
            screen.blit(land_text, (WIDTH / 2 + 40, 680))

            description_font = pygame.font.SysFont(None, 30)
            wrapped_text = wrap_text(self.land_descriptions[self.selected_land], description_font, 400)
            for i, line in enumerate(wrapped_text):
                desc_surface = description_font.render(line, True, WHITE)
                screen.blit(desc_surface, (WIDTH / 2 + 40, 710 + i * 25))

            font = pygame.font.SysFont(None, 30)
            pygame.draw.rect(screen, (0, 200, 0), self.enter_button)
            enter_text = font.render("Wejdź do krainy", True, WHITE)
            screen.blit(enter_text, (WIDTH / 2 + 30, HEIGHT - 50))

        pygame.draw.rect(screen, (0, 150, 200), self.inventory_button)
        pygame.draw.rect(screen, (200, 50, 50), self.quit_button)
        font = pygame.font.SysFont(None, 30)
        inventory_text = font.render("Ekwipunek", True, WHITE)
        quit_text = font.render("Zakończ", True, WHITE)
        screen.blit(inventory_text, (35, HEIGHT - 50))
        screen.blit(quit_text, (WIDTH - 145, HEIGHT - 50))


    def move_player(self, direction):
        new_x, new_y = self.player.x, self.player.y
        if direction == "UP" and self.player.y > 0:
            new_y -= self.grid_size
        elif direction == "DOWN" and self.player.y < (self.rows - 1) * self.grid_size:
            new_y += self.grid_size
        elif direction == "LEFT" and self.player.x > 0:
            new_x -= self.grid_size
        elif direction == "RIGHT" and self.player.x < (self.cols - 1) * self.grid_size:
            new_x += self.grid_size

        self.player.x, self.player.y = new_x, new_y
        self.selected_land = None
        for land, (col, row) in self.lands.items():
            if new_x == col * self.grid_size and new_y == row * self.grid_size:
                self.selected_land = land

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.move_player("UP")
            elif event.key == pygame.K_DOWN:
                self.move_player("DOWN")
            elif event.key == pygame.K_LEFT:
                self.move_player("LEFT")
            elif event.key == pygame.K_RIGHT:
                self.move_player("RIGHT")
            elif event.key == pygame.K_RETURN:
                if self.selected_land:
                    return self.selected_land
            return None
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.selected_land and self.enter_button.collidepoint(event.pos):
                return self.selected_land
            elif self.inventory_button.collidepoint(event.pos):
                show_inventory(self.player_game)
            elif self.quit_button.collidepoint(event.pos):
                pygame.quit()
                exit()
        return None

def show_world_map(player, player_game, start_position):
    world_map = WorldMap(player, player_game, start_position)
    running = True
    while running:
        screen.fill((0, 0, 0))
        world_map.draw(screen)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            selected_land = world_map.handle_event(event)
            if selected_land:
                return selected_land, (world_map.player.x // 100, world_map.player.y // 100)
