# --- Setup pygame window --- #
import pygame
pygame.init()

window = pygame.display.set_mode([500, 500])
background_color = (20, 30, 60)

# --- Setup drawing circles --- #
circle_color = (120, 130, 160)
centers = []
sizes = []

# --- Main loop --- #
drawing = True
while drawing:

    # --- Close window --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            drawing = False

        # --- Add new circles from clicks --- #
        if event.type == pygame.MOUSEBUTTONDOWN:
            center = pygame.mouse.get_pos()
            centers.append(center)
            sizes.append(100)

    # --- Shrink circles --- #
    for i in range(len(sizes)):
        sizes[i] -= 1

    # --- Draw --- #
    window.fill(background_color)

    for i in range(len(centers)):
        if i > 0:
            pygame.draw.circle(window, circle_color[i], (centers[i]), sizes) 
        
    pygame.display.flip()
