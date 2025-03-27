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

def load_and_resize(image_path, width = 80, height = 80):
    return pygame.transform.smoothscale(pygame.image.load(get_asset_path(image_path)), (width, height))

def draw_grid():
    """
    Draws a visible grid on the screen.
    """
    for x in range(0, WIDTH, 80):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, 80):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (WIDTH, y))

def get_random_position_in_grid():
    """ Returns a random position within a grid cell."""
    grid_x = random.randint(0, (WIDTH // 80) - 1) * 80
    grid_y = random.randint(0, (HEIGHT // 80) - 1) * 80
    return grid_x, grid_y

def get_valid_random_position(obstacle_positions):
    """ Find a random grid position that is not occupied by an obstacle. """
    while True:
        x, y = random.randint(0, WIDTH // 80 - 1) * 80, random.randint(0, HEIGHT // 80 - 1) * 80
        if (x, y) not in obstacle_positions:
            return x, y

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

    back_text = font.render("Opuść krainę", True, BLACK)
    back_rect = pygame.Rect(WIDTH - 240, HEIGHT - 70, 220, 50)

    pygame.draw.rect(screen, GREY, back_rect, border_radius=8)
    pygame.draw.rect(screen, BLACK, back_rect, 2)
    screen.blit(back_text, (back_rect.x + 10, back_rect.y + 10))

    return inventory_rect, back_rect

def draw_quit_button():
    font_buttons = pygame.font.SysFont(None, 30)
    quit_button = pygame.Rect(WIDTH - 170, HEIGHT - 60, 150, 40)
    pygame.draw.rect(screen, (200, 50, 50), quit_button)
    quit_text = font_buttons.render("Zakończ", True, WHITE)
    screen.blit(quit_text, (WIDTH - 145, HEIGHT - 50))
    return quit_button

def draw_merchant_button():
    font = pygame.font.SysFont(None, 40)
    merchant_text = font.render("Kupiec-mag", True, BLACK)
    merchant_button = pygame.Rect(WIDTH/2 - 100, HEIGHT - 70, 180, 50)
    pygame.draw.rect(screen, (200, 200, 50), merchant_button)
    pygame.draw.rect(screen, BLACK, merchant_button, 2)
    screen.blit(merchant_text, (merchant_button.x + 10, merchant_button.y + 10))

    return merchant_button


def draw_blacksmith_button():
    font = pygame.font.SysFont(None, 40)
    merchant_text = font.render("Kowal", True, BLACK)
    merchant_button = pygame.Rect(WIDTH/2 - 100, HEIGHT - 70, 180, 50)
    pygame.draw.rect(screen, (200, 200, 50), merchant_button)
    pygame.draw.rect(screen, BLACK, merchant_button, 2)
    screen.blit(merchant_text, (merchant_button.x + 50, merchant_button.y + 10))

    return merchant_button


def draw_aviator_button():
    font = pygame.font.SysFont(None, 40)
    aviator_text = font.render("Goblin-lotnik", True, BLACK)
    aviator_button = pygame.Rect(WIDTH/2 - 100, HEIGHT - 70, 200, 50)
    pygame.draw.rect(screen, (200, 200, 50), aviator_button)
    pygame.draw.rect(screen, BLACK, aviator_button, 2)
    screen.blit(aviator_text, (aviator_button.x + 10, aviator_button.y + 10))

    return aviator_button


def show_message(message):
    message_font = pygame.font.SysFont(None, 60)
    message_surface = message_font.render(message, True, BLACK)
    message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    padding = 20
    box_rect = message_rect.inflate(padding * 2, padding * 2)

    pygame.draw.rect(screen, WHITE, box_rect)
    pygame.draw.rect(screen, BLACK, box_rect, 2)

    screen.blit(message_surface, message_rect)
    pygame.display.flip()

    pygame.time.delay(1000)

def get_npc_image(image_path):
    return pygame.transform.smoothscale(pygame.image.load(get_asset_path(image_path)), (250, 250))

def draw_npc_screen(menu_width, menu_height, menu_x, menu_y):
    pygame.draw.rect(screen, BROWN, (menu_x, menu_y, menu_width, menu_height))