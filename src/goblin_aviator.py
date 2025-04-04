from utils import *

aviator_figure = pygame.image.load(get_asset_path("npcs/goblin_aviator_fig.png"))

class Aviator:
    def __init__(self):
        self.x, self.y = get_random_position_in_grid()
        self.figure = pygame.transform.smoothscale(aviator_figure, (grid_size, grid_size))
        self.rect = pygame.Rect(self.x, self.y, grid_size, grid_size)
        self.interacted = False

    def draw(self, screen):
        screen.blit(self.figure, (self.x, self.y))

    def check_collision(self, player):
        return self.rect.colliderect(pygame.Rect(player.x, player.y, grid_size, grid_size))


aviator = Aviator()


def show_aviator_menu(player):
    """ Displays the aviator menu."""
    menu_width, menu_height = 450, 450
    menu_x, menu_y = (WIDTH - menu_width) // 2, (HEIGHT - menu_height) // 2

    wizard_tower_flight_img = pygame.image.load(get_asset_path("lands/wizard_tower.png"))
    wizard_tower_flight_img = pygame.transform.smoothscale(wizard_tower_flight_img, (100, 100))

    magma_hills_flight_img = pygame.image.load(get_asset_path("lands/magma_hills.png"))
    magma_hills_flight_img = pygame.transform.smoothscale(magma_hills_flight_img, (100, 100))

    close_button = pygame.Rect(menu_x + 320, menu_y + 360, 100, 30)

    aviator_running = True
    while aviator_running:
        pygame.draw.rect(screen, BROWN, (menu_x, menu_y, menu_width, menu_height))
        pygame.draw.rect(screen, (200, 50, 50), close_button)
        font = pygame.font.SysFont(None, 30)
        close_text = font.render("Zamknij", True, WHITE)
        screen.blit(close_text, (menu_x + 330, menu_y + 365))
        aviator_image = get_npc_image("npcs/goblin_aviator.png")
        screen.blit(aviator_image, (menu_x + 100, menu_y + 20))

        wizard_tower_flight_btn = pygame.Rect(menu_x + 50, menu_y + 300, 100, 100)
        screen.blit(wizard_tower_flight_img, (menu_x + 50, menu_y + 300))

        magma_hills_flight_btn = pygame.Rect(menu_x + 150, menu_y + 300, 100, 100)
        screen.blit(magma_hills_flight_img, (menu_x + 150, menu_y + 300))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.collidepoint(event.pos):
                    aviator.interacted = True
                    aviator_running = False
                elif wizard_tower_flight_btn.collidepoint(event.pos):
                    if player.coins >= 150:
                        player.coins -= 150
                        show_message("Zakupiłeś lot!")
                        return "wizard_tower"
                    else:
                        show_message("Brak odpowiedniej ilości monet (150)!")
                elif magma_hills_flight_btn.collidepoint(event.pos):
                    if player.coins >= 300:
                        player.coins -= 300
                        show_message("Zakupiłeś lot!")
                        return "magma_hills"
                    else:
                        show_message("Brak odpowiedniej ilości monet (300)!")