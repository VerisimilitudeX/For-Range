# --- Setup window --- #
import pygame
pygame.init()
window = pygame.display.set_mode([500, 500])
fading = False
brightness = 0

# --- Create bars --- #
bars = []

for i in range(10):
    x = i * 50
    y = 0
    width = 25
    height = 500
    rect = pygame.Rect(x, y, width, height)
    bars.append(rect)
    
# --- Main loop --- #
drawing = True
while drawing:

    # --- Close window --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

    # --- Change colors --- #
    if brightness >= 200:
        fading = True
    if brightness <= 0:
        fading = False

    if fading:
        brightness -= 1
    else:
        brightness += 1

    # --- Draw --- #
    window.fill((0, 0, 0))
    color = (0 + brightness, 15 + brightness, 30 + brightness)

    for bar in bars:
        pygame.draw.rect(window, color, bar)

    pygame.display.flip()
