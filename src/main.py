import random
from src.constants import *
from src.assets import *
from player import Player
from src.enemy import Enemy
from src.choose_land import choose_land
from src.choose_character import choose_character
import items
from math_battle import math_battle
from messages import show_message

pygame.init()
pygame.display.set_caption("Math RPG")

player_character = choose_character()
selected_land = choose_land()
player = Player(WIDTH // 2, HEIGHT // 2, player_character)

if selected_land == "Zdradzieckie Lasy":
    enemy_types = ["Goblin", "Gnom", "Troll"]
elif selected_land == "Smrodliwe Bagna":
    enemy_types = ["Gnom", "Grzybolud"]
elif selected_land == "Stalowe Wyżyny":
    enemy_types = ["Golem"]

enemies = [
    Enemy(random.randint(50, WIDTH - 50), random.randint(50, HEIGHT - 50), random.choice(enemy_types))
    for _ in range(5)
]

berries = items.generate_berries()

clock = pygame.time.Clock()
running = True
while running:
    dt = clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False

    keys = pygame.key.get_pressed()
    player.move(keys)
    player.animation.update(dt)

    screen.fill(WHITE)

    current_image = player.animation.get_image()
    screen.blit(current_image, (player.x, player.y))

    pygame.draw.rect(screen, RED, (player.x, player.y - 15, 50, 5))
    pygame.draw.rect(screen, GREEN, (player.x, player.y - 15, 50 * (player.health / 100), 5))

    for enemy in enemies[:]:
        enemy.draw(screen)
        if enemy.check_collision(player):
            if math_battle(player, enemy.type, selected_land):
                enemies.remove(enemy)
                show_message("Pokonałeś wroga!")

    # Rysowanie jagódek
    for berry in berries[:]:
        screen.blit(items.berry_image, (berry.x, berry.y))
        if pygame.Rect(player.x, player.y, 50, 50).colliderect(berry):
            if player.health < 100:
                player.health = min(100, player.health + 20)
                berries.remove(berry)

    if not enemies:
        show_message("Wygrałeś! Pokonałeś wszystkich przeciwników!")
        running = False

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
