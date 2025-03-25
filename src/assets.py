import os
import pygame
from utils import get_asset_path

player_sprites = {
    "Czarodziejka": pygame.image.load(get_asset_path(os.path.join("characters", "sorceress.png"))),
    "Wilczas": pygame.image.load(get_asset_path(os.path.join("characters", "wolf_warrior.png"))),
    "Rabbit": pygame.image.load(get_asset_path(os.path.join("characters", "rabbit_knight.png"))),
    "Kocias": pygame.image.load(get_asset_path(os.path.join("characters", "cat_warrior.png")))
}

player_minifig_sprites = {
    "Czarodziejka": get_asset_path(os.path.join("characters", "sorceress_fig.png")),
    "Wilczas": get_asset_path(os.path.join("characters", "wolf_warrior_fig.png")),
    "Rabbit": get_asset_path(os.path.join("characters", "rabbit_knight_fig.png")),
    "Kocias": get_asset_path(os.path.join("characters", "cat_warrior_fig.png"))
}

enemy_sprites = {
    "Goblin": pygame.image.load(get_asset_path(os.path.join("enemies", "goblin.png"))),
    "Spider": pygame.image.load(get_asset_path(os.path.join("enemies", "giant_spider.png"))),
    "Golem": pygame.image.load(get_asset_path(os.path.join("enemies", "golem.png"))),
    "Gnom": pygame.image.load(get_asset_path(os.path.join("enemies", "gnome.png"))),
    "Bees": pygame.image.load(get_asset_path(os.path.join("enemies", "bees.png"))),
    "Ork": pygame.image.load(get_asset_path(os.path.join("enemies", "orc.png"))),
    "Troll": pygame.image.load(get_asset_path(os.path.join("enemies", "troll.png"))),
    "Grzybolud": pygame.image.load(get_asset_path(os.path.join("enemies", "mushroomkin.png"))),
    "Wilk": pygame.image.load(get_asset_path(os.path.join("enemies", "wolf.png"))),
    "Niedzwiedz": pygame.image.load(get_asset_path(os.path.join("enemies", "bear.png")))
}

enemy_fig_sprites = {
    "Goblin": pygame.image.load(get_asset_path(os.path.join("enemies", "goblin_fig.png"))),
    "Spider": pygame.image.load(get_asset_path(os.path.join("enemies", "giant_spider.png"))),
    "Golem": pygame.image.load(get_asset_path(os.path.join("enemies", "golem_fig.png"))),
    "Gnom": pygame.image.load(get_asset_path(os.path.join("enemies", "gnome_fig.png"))),
    "Bees": pygame.image.load(get_asset_path(os.path.join("enemies", "bees_fig.png"))),
    "Ork": pygame.image.load(get_asset_path(os.path.join("enemies", "orc_fig.png"))),
    "Troll": pygame.image.load(get_asset_path(os.path.join("enemies", "troll_fig.png"))),
    "Grzybolud": pygame.image.load(get_asset_path(os.path.join("enemies", "mushroomkin_fig.png"))),
    "Wilk": pygame.image.load(get_asset_path(os.path.join("enemies", "wolf_fig.png"))),
    "Niedzwiedz": pygame.image.load(get_asset_path(os.path.join("enemies", "bear_fig.png")))
}