from utils import *

class WorldMap:
    def __init__(self, player, start_position=(2, 2)):
        self.grid_size = 100
        self.cols, self.rows = 5, 5  # Larger grid for future expansion
        self.map_width = self.cols * self.grid_size
        self.map_height = self.rows * self.grid_size
        self.player = player
        self.start_position = start_position
        self.player.x, self.player.y = self.start_position[0] * self.grid_size, self.start_position[1] * self.grid_size

        # Define active lands and their positions
        self.lands = {
            "Goblinowe Lasy": (1, 2),
            "Grzybowe Bagna": (2, 1),
            "Stalowe Wyżyny": (3, 3),
            "Lodowa Kraina": (4, 4)
        }
        goblin_forest_image = pygame.image.load(get_asset_path("lands/goblin_forest.png"))
        mushroom_swamps_image = pygame.image.load(get_asset_path("lands/mushroom_swamps.png"))
        steel_hills_image = pygame.image.load(get_asset_path("lands/steel_hills.png"))
        ice_realm_image = pygame.image.load(get_asset_path("lands/ice_realm.png"))

        self.land_images = {
            "Goblinowe Lasy": pygame.transform.scale(goblin_forest_image, (100, 100)),
            "Grzybowe Bagna": pygame.transform.scale(mushroom_swamps_image, (100, 100)),
            "Stalowe Wyżyny": pygame.transform.scale(steel_hills_image, (100, 100)),
            "Lodowa Kraina": pygame.transform.scale(ice_realm_image, (100, 100))
        }

        realm_dim = 400

        self.realm_images = {
            "Goblinowe Lasy": pygame.transform.scale(goblin_forest_image, (realm_dim, realm_dim)),
            "Grzybowe Bagna": pygame.transform.scale(mushroom_swamps_image, (realm_dim, realm_dim)),
            "Stalowe Wyżyny": pygame.transform.scale(steel_hills_image, (realm_dim, realm_dim)),
            "Lodowa Kraina": pygame.transform.scale(ice_realm_image, (realm_dim, realm_dim))
        }

        self.land_descriptions = {
            "Goblinowe Lasy": "Gęste, tajemnicze lasy pełne goblinów, gnomów i trolli. Idealne do ćwiczenia dodawania.",
            "Grzybowe Bagna": "Mroczne, wilgotne bagna zamieszkałe przez gobliny i tajemnicze grzyboludy. Nauka odejmowania jest kluczowa, by przetrwać.",
            "Stalowe Wyżyny": "Wysokie wyżyny zamieszkałe przez potężne golemy. Tutaj nauczysz się mnożenia.",
            "Lodowa Kraina": "Mroźna i tajemnicza kraina, której mieszkańcy posługują się liczbami w niezwykły sposób."
        }

        self.selected_land = None
        self.enter_button = pygame.Rect(WIDTH / 2, HEIGHT - 100, 220, 50)

        self.castle_image = pygame.transform.scale(
            pygame.image.load(get_asset_path("lands/castle.png")), (100, 100)
        )

    def draw(self, screen):
        screen.fill((50, 50, 50))
        for col in range(self.cols):
            for row in range(self.rows):
                pygame.draw.rect(screen, (100, 100, 100),
                                 (col * self.grid_size, row * self.grid_size, self.grid_size, self.grid_size), 1)

        for land, (col, row) in self.lands.items():
            screen.blit(self.land_images[land], (col * self.grid_size, row * self.grid_size))

        screen.blit(self.castle_image,
                    (2 * self.grid_size, 2 * self.grid_size))

        screen.blit(self.player.realm_sprite, (self.player.x, self.player.y))

        if self.selected_land:
            screen.blit(self.realm_images[self.selected_land], (WIDTH / 2, 20))
            font = pygame.font.SysFont(None, 40)
            land_text = font.render(self.selected_land, True, WHITE)
            screen.blit(land_text, (WIDTH / 2, 430))  # Move text below the image

            description_font = pygame.font.SysFont(None, 30)
            wrapped_text = wrap_text(self.land_descriptions[self.selected_land], description_font, 400)
            for i, line in enumerate(wrapped_text):
                desc_surface = description_font.render(line, True, WHITE)
                screen.blit(desc_surface, (WIDTH / 2, 470 + i * 25))  # Move description below the image

            pygame.draw.rect(screen, (0, 200, 0), self.enter_button)
            enter_text = font.render("Wejdź do krainy", True, WHITE)
            screen.blit(enter_text, (WIDTH / 2, HEIGHT - 85))

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
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.selected_land and self.enter_button.collidepoint(event.pos):
                return self.selected_land
        return None

def show_world_map(player, start_position):
    world_map = WorldMap(player, start_position)
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
