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
    "Golem": pygame.image.load(get_asset_path(os.path.join("enemies", "golem.png"))),
    "Gnom": pygame.image.load(get_asset_path(os.path.join("enemies", "gnome.png"))),
    "Troll": pygame.image.load(get_asset_path(os.path.join("enemies", "troll.png"))),
    "Grzybolud": pygame.image.load(get_asset_path(os.path.join("enemies", "mushroomkin.png")))
}
