import pygame
# Wczytywanie grafik
player_sprites = {
    "Rycerz": pygame.image.load("knight.png"),
    "Czarodziejka": pygame.image.load("sorceress.png"),
    "Wilczas": pygame.image.load("wolf-warrior.png"),
    "Mag": pygame.image.load("mag.png")
}

player_minifig_sprites = {
    "Rycerz": "knight.png",
    "Czarodziejka": "sorceress.png",
    "Wilczas": "wolf-warrior.png",
    "Mag": "mag.png"
}

enemy_sprites = {
    "Goblin": pygame.image.load("goblin.jpg"),
    "Golem": pygame.image.load("golem.jpg"),
    "Troll": pygame.image.load("troll.jpg"),
    "Ogr": pygame.image.load("ogre.jpg")
}
