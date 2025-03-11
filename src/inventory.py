import pygame
from constants import *


def show_inventory(player):
    """
    Displays the inventory screen with the character portrait and collected coins.
    """
    inventory_running = True

    # Define inventory window size and position
    inventory_width = WIDTH // 3
    inventory_height = HEIGHT // 2
    inventory_x = (WIDTH - inventory_width) // 2
    inventory_y = (HEIGHT - inventory_height) // 2

    inventory_screen = pygame.Surface((inventory_width, inventory_height))
    inventory_screen.fill(WHITE)

    font = pygame.font.SysFont(None, 40)
    title = font.render("Ekwipunek", True, BLACK)

    # Load and scale the coin image
    coin_image = pygame.image.load("assets/ui/coin.png")
    coin_image = pygame.transform.scale(coin_image, (50, 50))

    # Get the original sprite size
    character_sprite = player.battle_sprite
    sprite_width, sprite_height = character_sprite.get_size()

    # Position character sprite in the center
    char_x = inventory_x + (inventory_width - sprite_width) // 2
    char_y = inventory_y + 50

    # Position for the coin display
    coin_x = inventory_x + (inventory_width // 2) - 50
    coin_y = char_y + sprite_height + 30

    # Position for the close button (moved lower)
    close_button_rect = pygame.Rect(inventory_x + (inventory_width - 140) // 2, coin_y + 80, 140, 50)

    while inventory_running:
        screen.fill(GREY)
        screen.blit(inventory_screen, (inventory_x, inventory_y))
        screen.blit(title, (inventory_x + (inventory_width - title.get_width()) // 2, inventory_y + 20))

        screen.blit(character_sprite, (char_x, char_y))

        screen.blit(coin_image, (coin_x, coin_y))
        coins_text = font.render(f"{player.coins}", True, BLACK)
        screen.blit(coins_text, (coin_x + 60, coin_y + 10))  # Adjust text position

        pygame.draw.rect(screen, GREY, close_button_rect, border_radius=8)
        pygame.draw.rect(screen, BLACK, close_button_rect, 2)
        close_text = font.render("Zamknij", True, BLACK)
        screen.blit(close_text, (close_button_rect.x + 20, close_button_rect.y + 10))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if close_button_rect.collidepoint(event.pos):  # Close button clicked
                    inventory_running = False
