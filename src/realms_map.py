from utils import *
from inventory import show_inventory

class WorldMap:
    def __init__(self, player, player_game, completed_realms, start_position=(1, 1)):
        self.grid_size = 100
        self.cols, self.rows = 8, 8
        self.map_width = self.cols * self.grid_size
        self.map_height = self.rows * self.grid_size
        self.player = player
        self.player_game = player_game
        self.start_position = start_position
        self.player.x, self.player.y = self.start_position[0] * self.grid_size, self.start_position[1] * self.grid_size

        self.offset_x = (WIDTH - self.map_width) // 10
        self.offset_y = (HEIGHT - self.map_height) // 2

        self.completed_realms = completed_realms
        self.green_tick = pygame.transform.smoothscale(
            pygame.image.load(get_asset_path("ui/green_tick.png")), (30, 30)
        )

        self.map_background = pygame.transform.smoothscale(
            pygame.image.load(get_asset_path("maps/world_map.png")), (self.map_width, self.map_height)
        )

        self.lands = {
            "Zamek": (1, 0),
            "Lasy": (1, 1),
            "Rwąca Rzeka": (1, 2),
            "Tajemnicza Zatoka": (0, 5),
            "Dzikie Brzegi": (0, 4),
            "Most": (2, 2),
            "Złoty Las": (3, 2),
            "Starożytne Ruiny": (3, 3),
            "Łyse Łąki": (1, 4),
            "Krwawe Wzgórza": (1, 5),
            "Dzikie Bory": (2, 3),
            "Mglista Puszcza": (2, 4),
            "Grzybowe Bagna": (3, 4),
            "Szare Skały": (1, 6),
            "Wyschły Wąwóz": (1, 7),
            "Magmowe Wzgórza": (4, 7),
            "Stalowe Wyżyny": (0, 6),
            "Wieża Maga": (0, 7),
            "Lodowa Kraina": (7, 0)
        }
        castle_image = pygame.image.load(get_asset_path("lands/castle.png"))
        town_image = pygame.image.load(get_asset_path("lands/town.png"))
        meadow_image = pygame.image.load(get_asset_path("lands/meadow.png"))
        woods_image = pygame.image.load(get_asset_path("lands/woods.png"))
        forest_image = pygame.image.load(get_asset_path("lands/forest.png"))
        village_image = pygame.image.load(get_asset_path("lands/mountain_village.png"))

        magic_lake_image = pygame.image.load(get_asset_path("lands/magic_lake.png"))
        river_image = pygame.image.load(get_asset_path("lands/river.png"))
        bridge_image = pygame.image.load(get_asset_path("lands/bridge.png"))
        rushing_river_image = pygame.image.load(get_asset_path("lands/rushing_river.png"))
        mountain_stream_image = pygame.image.load(get_asset_path("lands/mountain_stream.png"))
        mountains_image = pygame.image.load(get_asset_path("lands/mountains.png"))

        ancient_ruins_image = pygame.image.load(get_asset_path("lands/ancient_ruins.png"))
        golden_forest_image = pygame.image.load(get_asset_path("lands/golden_forest.png"))

        mysterious_bay_image = pygame.image.load(get_asset_path("lands/mysterious_bay.png"))
        wild_shores_image = pygame.image.load(get_asset_path("lands/wild_shores.png"))
        wizard_tower_image = pygame.image.load(get_asset_path("lands/wizard_tower.png"))
        bald_meadows_image = pygame.image.load(get_asset_path("lands/bald_meadows.png"))
        withering_hills_image = pygame.image.load(get_asset_path("lands/withering_heights.png"))
        wild_forest_image = pygame.image.load(get_asset_path("lands/wild_forest.png"))
        goblin_forest_image = pygame.image.load(get_asset_path("lands/dark_forest.png"))
        mushroom_swamps_image = pygame.image.load(get_asset_path("lands/mushroom_swamps.png"))
        steel_hills_image = pygame.image.load(get_asset_path("lands/steel_hills.png"))
        ice_realm_image = pygame.image.load(get_asset_path("lands/ice_realm.png"))
        grey_rocks_image = pygame.image.load(get_asset_path("lands/grey_rocks.png"))
        dry_ravine_image = pygame.image.load(get_asset_path("lands/dry_ravine.png"))
        magma_hills_image = pygame.image.load(get_asset_path("lands/magma_hills.png"))

        realm_dim = 700

        self.realm_images = {
            "Zamek": pygame.transform.smoothscale(castle_image, (realm_dim, realm_dim)),
            "Miasto": pygame.transform.smoothscale(town_image, (realm_dim, realm_dim)),
            "Łąki": pygame.transform.smoothscale(meadow_image, (realm_dim, realm_dim)),
            "Bór": pygame.transform.smoothscale(forest_image, (realm_dim, realm_dim)),
            "Lasy": pygame.transform.smoothscale(woods_image, (realm_dim, realm_dim)),
            "Tajemnicza Zatoka": pygame.transform.smoothscale(mysterious_bay_image, (realm_dim, realm_dim)),
            "Dzikie Brzegi": pygame.transform.smoothscale(wild_shores_image, (realm_dim, realm_dim)),
            "Czyste Jezioro": pygame.transform.smoothscale(magic_lake_image, (realm_dim, realm_dim)),
            "Góry": pygame.transform.smoothscale(mountains_image, (realm_dim, realm_dim)),
            "Górska Wies": pygame.transform.smoothscale(village_image, (realm_dim, realm_dim)),
            "Przeczysty Strumień": pygame.transform.smoothscale(mountain_stream_image, (realm_dim, realm_dim)),
            "Złoty Las": pygame.transform.smoothscale(golden_forest_image, (realm_dim, realm_dim)),
            "Starożytne Ruiny": pygame.transform.smoothscale(ancient_ruins_image, (realm_dim, realm_dim)),
            "Rzeka": pygame.transform.smoothscale(river_image, (realm_dim, realm_dim)),
            "Most": pygame.transform.smoothscale(bridge_image, (realm_dim, realm_dim)),
            "Rwąca Rzeka": pygame.transform.smoothscale(rushing_river_image, (realm_dim, realm_dim)),
            "Wieża Maga": pygame.transform.smoothscale(wizard_tower_image, (realm_dim, realm_dim)),
            "Łyse Łąki": pygame.transform.smoothscale(bald_meadows_image, (realm_dim, realm_dim)),
            "Krwawe Wzgórza": pygame.transform.smoothscale(withering_hills_image, (realm_dim, realm_dim)),
            "Dzikie Bory": pygame.transform.smoothscale(wild_forest_image, (realm_dim, realm_dim)),
            "Mglista Puszcza": pygame.transform.smoothscale(goblin_forest_image, (realm_dim, realm_dim)),
            "Grzybowe Bagna": pygame.transform.smoothscale(mushroom_swamps_image, (realm_dim, realm_dim)),
            "Stalowe Wyżyny": pygame.transform.smoothscale(steel_hills_image, (realm_dim, realm_dim)),
            "Lodowa Kraina": pygame.transform.smoothscale(ice_realm_image, (realm_dim, realm_dim)),
            "Szare Skały": pygame.transform.smoothscale(grey_rocks_image, (realm_dim, realm_dim)),
            "Wyschły Wąwóz": pygame.transform.smoothscale(dry_ravine_image, (realm_dim, realm_dim)),
            "Magmowe Wzgórza": pygame.transform.smoothscale(magma_hills_image, (realm_dim, realm_dim))
        }

        self.hidden_lands_conditions = {
            "Most": ["Lasy"],
            "Rwąca Rzeka": ["Lasy"],
            "Dzikie Bory": ["Most"],
            "Łyse Łąki": ["Dzikie Bory"],
            "Mglista Puszcza": ["Dzikie Bory"],
            "Starożytne Ruiny": ["Dzikie Bory"],
            "Krwawe Wzgórza": ["Łyse Łąki"],
            "Dzikie Brzegi": ["Łyse Łąki"],
            "Grzybowe Bagna": ["Mglista Puszcza"],
            "Tajemnicza Zatoka": ["Dzikie Brzegi"],
            "Stalowe Wyżyny": ["Tajemnicza Zatoka"],
            "Wieża Maga": ["Stalowe Wyżyny"],
            "Złoty Las": ["Most"],
            "Szare Skały": ["Krwawe Wzgórza"],
            "Wyschły Wąwóz": ["Krwawe Wzgórza"],
            "Lodowa Kraina": ["Złoty Las"],
            "Magmowe Wzgórza": ["Wieża Maga"]
        }

        self.locked_lands = {
            "Dzikie Bory": 100,
            "Mglista Puszcza": 150,
            "Starożytne Ruiny": 150,
            "Łyse Łąki": 150,
            "Dzikie Brzegi": 150,
            "Krwawe Wzgórza": 200,
            "Tajemnicza Zatoka": 200,
            "Grzybowe Bagna": 250,
            "Stalowe Wyżyny": 250,
            "Wieża Maga": 300,
            "Szare Skały": 300,
            "Wyschły Wąwóz": 300,
            "Magmowe Wzgórza": 300,
            "Lodowa Kraina": 300
        }

        self.land_descriptions = {
            "Zamek": "Górujący nad okolicą, ostoja bezpieczeństwa i spokoju... na jak długo?",
            "Miasto": "Gwarne i pełne życia",
            "Łąki": "",
            "Bór": "",
            "Lasy": "",
            "Złoty Las": "Zamieszkane przez elfy, gotowe pomóc.",
            "Starożytne Ruiny": "",
            "Czyste Jezioro": "",
            "Góry": "",
            "Górska Wies": "",
            "Przeczysty Strumień": "",
            "Rzeka": "",
            "Most": "",
            "Rwąca Rzeka": "",
            "Dzikie Brzegi": "",
            "Tajemnicza Zatoka": "",
            "Wieża Maga": "",
            "Łyse Łąki": "Pełne niebezpiecznych maruderów.",
            "Krwawe Wzgórza": "Zamieszkane przez dumnych i wojowniczych orków",
            "Dzikie Bory": "",
            "Mglista Puszcza": "Gęste, tajemnicze lasy pełne goblinów, gnomów i trolli. Idealne do ćwiczenia dodawania.",
            "Grzybowe Bagna": "Mroczne, wilgotne bagna zamieszkałe przez gobliny i tajemnicze grzyboludy. Nauka odejmowania jest kluczowa, by przetrwać.",
            "Stalowe Wyżyny": "Wysokie wyżyny zamieszkałe przez potężne golemy. Tutaj nauczysz się mnożenia.",
            "Szare Skały": "Opustoszone, na pierwszy rzut oka.",
            "Wyschły Wąwóz": "Zamieszkany przez wygłodniałe ogry...",
            "Magmowe Wzgórza": "Gorąco...",
            "Lodowa Kraina": "Mroźna i tajemnicza kraina, której mieszkańcy posługują się liczbami w niezwykły sposób."
        }

        self.land_rects = {}
        for land, (col, row) in self.lands.items():
            rect = pygame.Rect(
                self.offset_x + col * self.grid_size,
                self.offset_y + row * self.grid_size,
                self.grid_size,
                self.grid_size
            )
            self.land_rects[land] = rect

        for land, (col, row) in self.lands.items():
            if self.player.x == col * self.grid_size and self.player.y == row * self.grid_size:
                self.selected_land = land
                break

        self.enter_button = pygame.Rect(self.offset_x + WIDTH / 2, HEIGHT - 60, 220, 40)
        self.inventory_button = pygame.Rect(self.offset_x + 20, HEIGHT - 60, 150, 40)

    def is_land_visible(self, land):
        if land not in self.hidden_lands_conditions:
            return True
        required_realms = self.hidden_lands_conditions[land]
        return all(req in self.completed_realms for req in required_realms)

    def draw(self, screen):
        screen.fill((50, 50, 50))
        screen.blit(self.map_background, (self.offset_x, self.offset_y))

        for land, (col, row) in self.lands.items():
            if not self.is_land_visible(land):
                continue
            dot_x = self.offset_x + col * self.grid_size + self.grid_size // 2
            dot_y = self.offset_y + row * self.grid_size + self.grid_size // 2
            if land in self.locked_lands and self.player_game.xp < self.locked_lands[land]:
                color = (255, 165, 0)
            elif land in self.completed_realms:
                color = (0, 255, 0)
            else:
                color = (255, 255, 255)
            pygame.draw.circle(screen, color, (dot_x, dot_y), 20)

        screen.blit(self.player.realm_sprite, (self.offset_x + self.player.x, self.offset_y + self.player.y))

        if self.selected_land:
            screen.blit(self.realm_images[self.selected_land],
                        (self.offset_x + WIDTH / 2 + 40, self.offset_y + 20))
            font = pygame.font.SysFont(None, 40)
            land_text = font.render(self.selected_land, True, WHITE)
            screen.blit(land_text, (self.offset_x + WIDTH / 2 + 40, self.offset_y + 680))
            description_font = pygame.font.SysFont(None, 30)
            wrapped_text = wrap_text(self.land_descriptions[self.selected_land],
                                     description_font, WIDTH / 2 - self.offset_x)
            for i, line in enumerate(wrapped_text):
                desc_surface = description_font.render(line, True, WHITE)
                screen.blit(desc_surface, (self.offset_x + WIDTH / 2 + 40, self.offset_y + 720 + i * 25))
            if self.selected_land in self.locked_lands and self.player_game.xp < self.locked_lands[self.selected_land]:
                font = pygame.font.SysFont(None, 40)
                lock_text = font.render(f"Zablokowane - wymaga {self.locked_lands[self.selected_land]} XP", True, RED)
                screen.blit(lock_text, (self.offset_x + WIDTH / 2 + 40, HEIGHT - 100))
            else:
                self.draw_enter_button(screen)

        pygame.draw.rect(screen, (0, 150, 200), self.inventory_button)
        font = pygame.font.SysFont(None, 30)
        inventory_text = font.render("Ekwipunek", True, WHITE)
        screen.blit(inventory_text, (self.offset_x + 35, HEIGHT - 50))
        self.quit_button = draw_quit_button()

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

        new_cell = (new_x // self.grid_size, new_y // self.grid_size)
        allowed_cells = {cell for land, cell in self.lands.items()
                         if self.is_land_visible(land)}

        if new_cell not in allowed_cells:
            return

        self.player.x, self.player.y = new_x, new_y
        self.selected_land = None
        for land, (col, row) in self.lands.items():
            if new_cell == (col, row):
                self.selected_land = land

    def draw_enter_button(self, screen):
        font = pygame.font.SysFont(None, 30)
        pygame.draw.rect(screen, GREEN, self.enter_button)
        enter_text = font.render("Wejdź do krainy", True, WHITE)
        screen.blit(enter_text, (self.offset_x + WIDTH / 2 + 30, HEIGHT - 50))
        return self.enter_button

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
                    if (self.selected_land in self.locked_lands and
                        self.player_game.xp < self.locked_lands[self.selected_land]):
                        return None
                    return self.selected_land
            return None
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for land, rect in self.land_rects.items():
                if rect.collidepoint(event.pos):
                    if not self.is_land_visible(land):
                        continue
                    if land in self.locked_lands and self.player_game.xp < self.locked_lands[land]:
                        continue
                    col, row = self.lands[land]
                    self.player.x = col * self.grid_size
                    self.player.y = row * self.grid_size
                    self.selected_land = land
                    break
            if self.selected_land and self.enter_button.collidepoint(event.pos):
                if self.selected_land in self.locked_lands:
                    required_xp = self.locked_lands[self.selected_land]
                    if self.player_game.xp >= required_xp:
                        return self.selected_land
                    else:
                        return None
                else:
                    return self.selected_land
            elif self.inventory_button.collidepoint(event.pos):
                show_inventory(self.player_game)
            elif self.quit_button.collidepoint(event.pos):
                pygame.quit()
                exit()
        return None

def show_world_map(player, player_game, completed_realms, start_position):
    world_map = WorldMap(player, player_game, completed_realms, start_position)
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
                return selected_land, (world_map.player.x // 100, world_map.player.y // 100), world_map.completed_realms
