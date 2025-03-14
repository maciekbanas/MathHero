from constants import *
from utils import *

merchant_image = pygame.image.load(get_asset_path("npcs/merchant.png"))
merchant_figure = pygame.image.load(get_asset_path("npcs/merchant_fig.png"))

class Merchant:
    def __init__(self):
        self.x, self.y = get_random_position_in_grid()
        self.image = pygame.transform.scale(merchant_image, (200, 200))
        self.figure = pygame.transform.scale(merchant_figure, (50, 50))
        self.rect = pygame.Rect(self.x, self.y, 50, 50)
        self.interacted = False

    def draw(self, screen):
        screen.blit(self.figure, (self.x, self.y))

    def check_collision(self, player):
        return self.rect.colliderect(pygame.Rect(player.x, player.y, 50, 50))


merchant = Merchant()


def show_merchant_menu(player):
    """ Displays the merchant menu."""
    menu_width, menu_height = 400, 350  # Increased height to prevent overlap
    menu_x, menu_y = (WIDTH - menu_width) // 2, (HEIGHT - menu_height) // 2
    buy_elixir_img = pygame.image.load(get_asset_path("items/elixir_solution.png"))
    buy_elixir_img = pygame.transform.scale(buy_elixir_img, (100, 100))
    close_button = pygame.Rect(menu_x + 220, menu_y + 300, 100, 30)  # Adjusted position
    buy_button = pygame.Rect(menu_x + 100, menu_y + 300, 100, 30)  # New buy button
    elixir_button = pygame.Rect(menu_x + 50, menu_y + 150, 100, 100)

    merchant_running = True
    while merchant_running:
        pygame.draw.rect(screen, (150, 100, 50), (menu_x, menu_y, menu_width, menu_height))
        pygame.draw.rect(screen, (200, 50, 50), close_button)
        pygame.draw.rect(screen, (50, 200, 50), buy_button)  # Green buy button
        font = pygame.font.SysFont(None, 30)
        close_text = font.render("Zamknij", True, WHITE)
        buy_text = font.render("Kup", True, WHITE)
        screen.blit(close_text, (menu_x + 240, menu_y + 305))  # Adjusted position
        screen.blit(buy_text, (menu_x + 130, menu_y + 305))  # Buy button text
        screen.blit(merchant.image, (menu_x + 150, menu_y + 20))
        screen.blit(buy_elixir_img, (menu_x + 50, menu_y + 150))

        # Display price text higher up
        price_text = font.render("Eliksir rozwiązania. Koszt: 30 monet", True, WHITE)
        screen.blit(price_text, (menu_x + 50, menu_y + 270))

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
                    if player.coins >= 30:
                        player.coins -= 30
                        player.inventory.append("Eliksir rozwiązania")
                        show_message("Zakupiłeś eliksir rozwiązania zagadki!")
                    else:
                        show_message("Brak odpowiedniej ilości monet!")

