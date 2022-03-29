#### ---- SET UP ---- ####

# --- Libraries --- #
import random
import pygame
pygame.init()

# --- Window --- #
window = pygame.display.set_mode([500, 500])
window.fill((0, 0, 0))

# --- Variables --- #
max_circles = random.randint(20, 50)
color_increment = int(255 / max_circles)

#### ---- DRAW LOOP ---- ####
quit = False
for i in range(max_circles):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True

    color = (i * color_increment, i * color_increment, i * color_increment)
    radius = i * 5

    point = (random.randint(25, 475), random.randint(25, 475))

    # --- Draw circle and pause --- #
    pygame.draw.circle(window, color, point, radius)
    pygame.display.flip()
    pygame.time.wait(200)
    
    if quit == True:
        break
        
print(str(max_circles) + " circles")
