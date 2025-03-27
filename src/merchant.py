from utils import *

merchant_figure = pygame.image.load(get_asset_path("npcs/merchant_fig.png"))

class Merchant:
    def __init__(self):
        self.x, self.y = get_random_position_in_grid()
        self.figure = pygame.transform.smoothscale(merchant_figure, (grid_size, grid_size))
        self.rect = pygame.Rect(self.x, self.y, grid_size, grid_size)
        self.interacted = False

    def draw(self, screen):
        screen.blit(self.figure, (self.x, self.y))

    def check_collision(self, player):
        return self.rect.colliderect(pygame.Rect(player.x, player.y, grid_size, grid_size))


merchant = Merchant()


def show_merchant_menu(player):
    """ Displays the merchant menu."""
    menu_width, menu_height = 450, 400
    menu_x, menu_y = (WIDTH - menu_width) // 2, (HEIGHT - menu_height) // 2
    buy_elixir_img = pygame.image.load(get_asset_path("items/elixir_solution.png"))
    buy_elixir_img = pygame.transform.smoothscale(buy_elixir_img, (100, 100))
    close_button = pygame.Rect(menu_x + 320, menu_y + 360, 100, 30)
    buy_button = pygame.Rect(menu_x + 40, menu_y + 360, 100, 30)
    elixir_button = pygame.Rect(menu_x + 50, menu_y + 190, 100, 100)

    merchant_running = True
    while merchant_running:
        draw_npc_screen(menu_width, menu_height, menu_x, menu_y)
        pygame.draw.rect(screen, (200, 50, 50), close_button)
        pygame.draw.rect(screen, (GREEN), buy_button)
        font = pygame.font.SysFont(None, 30)
        close_text = font.render("Zamknij", True, WHITE)
        buy_text = font.render("Kup", True, WHITE)
        screen.blit(close_text, (menu_x + 330, menu_y + 365))
        screen.blit(buy_text, (menu_x + 70, menu_y + 365))
        merchant_image = get_npc_image("npcs/merchant.png")
        screen.blit(merchant_image, (menu_x + 100, menu_y + 20))
        screen.blit(buy_elixir_img, (menu_x + 50, menu_y + 250))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button.collidepoint(event.pos):
                    merchant.interacted = True
                    merchant_running = False
                elif elixir_button.collidepoint(event.pos) or buy_button.collidepoint(event.pos):
                    if player.coins >= 50:
                        player.coins -= 50
                        player.inventory.append("Eliksir rozwiązania")
                        show_message("Zakupiłeś eliksir rozwiązania zagadki!")
                    else:
                        show_message("Brak odpowiedniej ilości monet (50)!")

