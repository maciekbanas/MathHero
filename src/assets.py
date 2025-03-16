import os
import pygame
from utils import get_asset_path

# Wczytywanie grafik
player_sprites = {
    "Rycerz": pygame.image.load(get_asset_path(os.path.join("characters", "knight.png"))),
    "Czarodziejka": pygame.image.load(get_asset_path(os.path.join("characters", "sorceress.png"))),
    "Wilczas": pygame.image.load(get_asset_path(os.path.join("characters", "wolf_warrior.png"))),
    "Mag": pygame.image.load(get_asset_path(os.path.join("characters", "mag.png")))
}

player_minifig_sprites = {
    "Rycerz": get_asset_path(os.path.join("characters", "knight_fig.png")),
    "Czarodziejka": get_asset_path(os.path.join("characters", "sorceress_fig.png")),
    "Wilczas": get_asset_path(os.path.join("characters", "wolf_warrior_fig.png")),
    "Mag": get_asset_path(os.path.join("characters", "mag_fig.png"))
}

enemy_sprites = {
    "Goblin": pygame.image.load(get_asset_path(os.path.join("enemies", "goblin.png"))),
    "Spider": pygame.image.load(get_asset_path(os.path.join("enemies", "giant_spider.png"))),
    "Golem": pygame.image.load(get_asset_path(os.path.join("enemies", "golem.png"))),
    "Gnom": pygame.image.load(get_asset_path(os.path.join("enemies", "gnome.png"))),
    "Ork": pygame.image.load(get_asset_path(os.path.join("enemies", "orc.png"))),
    "Troll": pygame.image.load(get_asset_path(os.path.join("enemies", "troll.png"))),
    "Grzybolud": pygame.image.load(get_asset_path(os.path.join("enemies", "mushroomkin.png"))),
    "Wilk": pygame.image.load(get_asset_path(os.path.join("enemies", "wolf.png")))
}

enemy_fig_sprites = {
    "Goblin": pygame.image.load(get_asset_path(os.path.join("enemies", "goblin_fig.png"))),
    "Spider": pygame.image.load(get_asset_path(os.path.join("enemies", "giant_spider.png"))),
    "Golem": pygame.image.load(get_asset_path(os.path.join("enemies", "golem_fig.png"))),
    "Gnom": pygame.image.load(get_asset_path(os.path.join("enemies", "gnome_fig.png"))),
    "Ork": pygame.image.load(get_asset_path(os.path.join("enemies", "orc_fig.png"))),
    "Troll": pygame.image.load(get_asset_path(os.path.join("enemies", "troll_fig.png"))),
    "Grzybolud": pygame.image.load(get_asset_path(os.path.join("enemies", "mushroomkin_fig.png"))),
    "Wilk": pygame.image.load(get_asset_path(os.path.join("enemies", "wolf_fig.png")))
}