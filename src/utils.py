import os
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

    # --- Powrót Button (Bottom Right) ---
    back_text = font.render("Powrót", True, BLACK)
    back_rect = pygame.Rect(WIDTH - 200, HEIGHT - 70, 180, 50)

    pygame.draw.rect(screen, GREY, back_rect, border_radius=8)
    pygame.draw.rect(screen, BLACK, back_rect, 2)  # Border
    screen.blit(back_text, (back_rect.x + 50, back_rect.y + 10))

    return inventory_rect, back_rect