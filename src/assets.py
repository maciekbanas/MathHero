import pygame
# Wczytywanie grafik
player_sprites = {
    "Rycerz": pygame.image.load("../assets/characters/knight.png"),
    "Czarodziejka": pygame.image.load("../assets/characters/sorceress.png"),
    "Wilczas": pygame.image.load("../assets/characters/wolf_warrior.png"),
    "Mag": pygame.image.load("../assets/characters/mag.png")
}

player_minifig_sprites = {
    "Rycerz": "../assets/characters/knight_fig.png",
    "Czarodziejka": "../assets/characters/sorceress_fig.png",
    "Wilczas": "../assets/characters/wolf_warrior_fig.png",
    "Mag": "../assets/characters/mag_fig.png"
}

enemy_sprites = {
    "Goblin": pygame.image.load("../assets/enemies/goblin.png"),
    "Golem": pygame.image.load("../assets/enemies/golem.png"),
    "Gnom": pygame.image.load("../assets/enemies/gnome.png"),
    "Troll": pygame.image.load("../assets/enemies/troll.png"),
    "Grzybolud": pygame.image.load("../assets/enemies/mushroomkin.png")
}
