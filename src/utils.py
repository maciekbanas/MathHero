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

def draw_back_button():
    font = pygame.font.SysFont(None, 40)
    back_text = font.render("Powrót", True, BLACK)
    text_width, text_height = back_text.get_size()
    padding = 20
    back_rect = pygame.Rect(WIDTH - text_width - padding, 20, text_width + padding, text_height + padding // 2)
    pygame.draw.rect(screen, GREY, back_rect)
    screen.blit(back_text, (back_rect.x + padding // 2, back_rect.y + padding // 4))

    return(back_rect)