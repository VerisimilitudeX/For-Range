# --- Setup window --- #
import pygame
pygame.init()
window = pygame.display.set_mode([500, 100])

background_color = (0, 0, 0)
bar_color = (255, 230, 200)

# --- Bar countdown --- #
for i in range(10, 0, -1):
    window.fill(background_color)
    rect = pygame.Rect(0, 0, 50 * i, 100)
    pygame.draw.rect(window, bar_color, rect)
    pygame.display.flip()
    pygame.time.wait(500)
