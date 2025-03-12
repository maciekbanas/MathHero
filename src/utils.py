import os
import random
from constants import *

def wrap_text(text, font, max_width):

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        test_line = current_line + " " + word if current_line else word
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines

def get_asset_path(relative_path):
    return os.path.join(ASSETS_DIR, relative_path)

def draw_grid():
    """
    Draws a visible grid on the screen.
    """
    for x in range(0, WIDTH, 50):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 50):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (WIDTH, y))

def get_random_position_in_grid():
    """ Returns a random position within a grid cell."""
    grid_x = random.randint(0, (WIDTH // 50) - 1) * 50
    grid_y = random.randint(0, (HEIGHT // 50) - 1) * 50
    return grid_x, grid_y

def draw_ui_buttons():
    """
    Draws the 'Ekwipunek' and 'Powrót' buttons on the screen.
    """
    font = pygame.font.SysFont(None, 40)

    # --- Ekwipunek Button (Bottom Left) ---
    inventory_text = font.render("Ekwipunek", True, BLACK)
    inventory_rect = pygame.Rect(20, HEIGHT - 70, 180, 50)

    pygame.draw.rect(screen, GREY, inventory_rect, border_radius=8)
    pygame.draw.rect(screen, BLACK, inventory_rect, 2)  # Border
    screen.blit(inventory_text, (inventory_rect.x + 15, inventory_rect.y + 10))

    back_text = font.render("Powrót", True, BLACK)
    back_rect = pygame.Rect(WIDTH - 200, HEIGHT - 70, 180, 50)

    pygame.draw.rect(screen, GREY, back_rect, border_radius=8)
    pygame.draw.rect(screen, BLACK, back_rect, 2)
    screen.blit(back_text, (back_rect.x + 50, back_rect.y + 10))

    return inventory_rect, back_rect

def draw_merchant_button():
    font = pygame.font.SysFont(None, 40)
    merchant_text = font.render("Kupiec-mag", True, BLACK)
    merchant_button = pygame.Rect(WIDTH/2, HEIGHT - 70, 180, 50)
    pygame.draw.rect(screen, (200, 200, 50), merchant_button)
    pygame.draw.rect(screen, BLACK, merchant_button, 2)
    screen.blit(merchant_text, (merchant_button.x + 10, merchant_button.y + 10))

    return merchant_button
def show_message(message):
    message_font = pygame.font.SysFont(None, 60)
    message_surface = message_font.render(message, True, BLACK)
    message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.fill(WHITE)
    screen.blit(message_surface, message_rect)
    pygame.display.flip()

    pygame.time.delay(1000)