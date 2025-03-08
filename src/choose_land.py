import os
from constants import *
from utils import wrap_text

def choose_land():

    assets_path = os.path.join("../assets", "lands")

    lands = {
        "Zdradzieckie Lasy": {
            "image": pygame.image.load(os.path.join(assets_path, "forest.png")),
            "description": "Gęste, tajemnicze lasy pełne goblinów, gnomów i trolli. Idealne do ćwiczenia dodawania."
        },
        "Stalowe Wyżyny": {
            "image": pygame.image.load(os.path.join(assets_path, "hills.png")),
            "description": "Wysokie wyżyny zamieszkałe przez potężne golemy. Tutaj nauczysz się mnożenia."
        },
        "Grzybowe Bagna": {
            "image": pygame.image.load(os.path.join(assets_path, "swamps.png")),
            "description": "Mroczne, wilgotne bagna spowite mgłą, gdzie każda ścieżka prowadzi w nieznane. Zamieszkałe przez gobliny i tajemnicze grzyboludy, uczą odwagi i umiejętności odejmowania, które pomogą przetrwać w tym zdradliwym terenie."
        },
        "Zimowe Królestwo": {
            "image": pygame.image.load(os.path.join(assets_path, "ice_realm.png")),
            "description": "Tu bardzo zimno..."
        }
    }

    font = pygame.font.SysFont(None, 50)
    desc_font = pygame.font.SysFont(None, 30)
    button_width = WIDTH // 3.5
    button_height = HEIGHT // 3
    start_x = (WIDTH - (3 * button_width + 50)) // 2
    start_y = HEIGHT // 4

    land_buttons = []
    for i, land_name in enumerate(lands.keys()):
        row = i // 3
        col = i % 3
        rect = pygame.Rect(start_x + col * (button_width + 25), start_y + row * (button_height + 25), button_width,
                           button_height)
        land_buttons.append((land_name, rect))

    chosen_land = None

    while chosen_land is None:
        screen.fill(WHITE)
        title_text = font.render("Wybierz krainę", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 8))
        screen.blit(title_text, title_rect)

        mouse_pos = pygame.mouse.get_pos()
        hovered_land = None

        for land_name, rect in land_buttons:
            image = pygame.transform.scale(lands[land_name]["image"], (button_width, button_height))
            screen.blit(image, rect.topleft)
            text_surface = font.render(land_name, True, WHITE)
            text_rect = text_surface.get_rect(center=(rect.centerx, rect.bottom + 30))
            screen.blit(text_surface, text_rect)

            if rect.collidepoint(mouse_pos):
                hovered_land = land_name

        if hovered_land:
            header_surface = font.render(hovered_land, True, BLACK)
            header_rect = header_surface.get_rect(center=(WIDTH // 2, HEIGHT - 150))
            screen.blit(header_surface, header_rect)

            wrapped_text = wrap_text(lands[hovered_land]["description"], desc_font, WIDTH - 100)
            for i, line in enumerate(wrapped_text):
                desc_surface = desc_font.render(line, True, BLACK)
                desc_rect = desc_surface.get_rect(center=(WIDTH // 2, HEIGHT - 120 + i * 30))
                screen.blit(desc_surface, desc_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                for land_name, rect in land_buttons:
                    if rect.collidepoint(mouse_pos):
                        chosen_land = land_name
                        break

    return chosen_land
