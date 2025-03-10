import pygame
from constants import *


def show_inventory(player):
    """
    Displays the inventory screen with the character portrait and collected coins.
    """
    inventory_running = True
    inventory_screen = pygame.Surface((WIDTH // 3, HEIGHT // 2))  # Slightly larger inventory window
    inventory_screen.fill(WHITE)

    font = pygame.font.SysFont(None, 40)
    title = font.render("Ekwipunek", True, BLACK)

    # Load and scale the coin image
    coin_image = pygame.image.load("assets/ui/coin.png")
    coin_image = pygame.transform.scale(coin_image, (50, 50))

    # Position for the coin display
    coin_x = WIDTH // 2 - 40
    coin_y = HEIGHT // 3 + 230

    # Position for the close button (moved lower)
    close_button_rect = pygame.Rect(WIDTH // 2 - 60, HEIGHT // 3 + 300, 140, 50)

    while inventory_running:
        screen.fill(GREY)
        screen.blit(inventory_screen, (WIDTH // 3, HEIGHT // 3))
        screen.blit(title, (WIDTH // 2 - 50, HEIGHT // 3 + 20))

        # Display character sprite
        character_sprite = pygame.transform.scale(player.battle_sprite, (150, 150))
        screen.blit(character_sprite, (WIDTH // 2 - 75, HEIGHT // 3 + 60))

        # Display coin image and count
        screen.blit(coin_image, (coin_x, coin_y))
        coins_text = font.render(f"{player.coins}", True, BLACK)
        screen.blit(coins_text, (coin_x + 60, coin_y + 10))  # Adjust text position

        # Draw "Close" button (moved lower)
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

def draw_inventory_button():
    """
    Draws the inventory button on the screen.
    """
    font = pygame.font.SysFont(None, 40)
    inventory_text = font.render("Ekwipunek", True, BLACK)

    # Define button position and size
    inventory_rect = pygame.Rect(20, HEIGHT - 70, 180, 50)

    # Ensure button is visible
    pygame.draw.rect(screen, GREY, inventory_rect, border_radius=8)
    pygame.draw.rect(screen, BLACK, inventory_rect, 2)  # Black border
    screen.blit(inventory_text, (inventory_rect.x + 15, inventory_rect.y + 10))

    return inventory_rect  # Return rect for click detection

