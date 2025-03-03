from src.constants import *
def show_message(message):
    message_font = pygame.font.SysFont(None, 60)
    message_surface = message_font.render(message, True, BLACK)
    message_rect = message_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))

    screen.fill(WHITE)
    screen.blit(message_surface, message_rect)
    pygame.display.flip()

    pygame.time.delay(1000)