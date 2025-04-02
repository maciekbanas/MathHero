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
    menu_width, menu_height = 450, 400
    menu_x, menu_y = (WIDTH - menu_width) // 2, (HEIGHT - menu_height) // 2
    buy_flight_img = pygame.image.load(get_asset_path("lands/wizard_tower.png"))
    buy_flight_img = pygame.transform.smoothscale(buy_flight_img, (100, 100))
    close_button = pygame.Rect(menu_x + 320, menu_y + 360, 100, 30)
    buy_button = pygame.Rect(menu_x + 40, menu_y + 360, 100, 30)
    travel_button = pygame.Rect(menu_x + 50, menu_y + 190, 100, 100)

    aviator_running = True
    while aviator_running:
        pygame.draw.rect(screen, BROWN, (menu_x, menu_y, menu_width, menu_height))
        pygame.draw.rect(screen, (200, 50, 50), close_button)
        pygame.draw.rect(screen, (50, 200, 50), buy_button)  # Green buy button
        font = pygame.font.SysFont(None, 30)
        close_text = font.render("Zamknij", True, WHITE)
        buy_text = font.render("Kup lot", True, WHITE)
        screen.blit(close_text, (menu_x + 330, menu_y + 365))
        screen.blit(buy_text, (menu_x + 45, menu_y + 365))
        aviator_image = get_npc_image("npcs/goblin_aviator.png")
        screen.blit(aviator_image, (menu_x + 130, menu_y + 20))
        screen.blit(buy_flight_img, (menu_x + 50, menu_y + 250))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.collidepoint(event.pos):
                    aviator.interacted = True
                    aviator_running = False
                elif travel_button.collidepoint(event.pos) or buy_button.collidepoint(event.pos):
                    if player.coins >= 100:
                        player.coins -= 100
                        show_message("Zakupiłeś lot!")
                        return True
                    else:
                        show_message("Brak odpowiedniej ilości monet (500)!")