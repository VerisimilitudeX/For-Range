#### ---- SETUP ---- ####

# --- Pygame --- #
import pygame
pygame.init()

# --- Window --- #
number_of_circles = int(input("How many circles should there be? "))
width = number_of_circles 
window = pygame.display.set_mode([280, width])

# --- Variables --- #
light_color = (200, 200, 255)
dark_color = (100, 100, 255)
darker_circle = 0

# --- Create list of circle centers --- #
margin = 40
center_pos = []
for i in range(width):
    point = (margin + i * 50, 75)
    center_pos.append(point)

#### ---- MAIN LOOP ---- ####
running = True
while running:

    # --- Event loop --- #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #### ---- DRAW CIRCLES ---- ####
    window.fill((255, 255, 255))

    # --- Draw all light circles except 1 dark --- #
    for i in range(len(center_pos)):
        if i != darker_circle:
            pygame.draw.circle(window, light_color, center_pos[i], 15)
        else:
            pygame.draw.circle(window, dark_color, center_pos[i], 20)

    #### ---- FINISH DRAWING ---- ####

    # --- Change which circle should be dark next --- #
    darker_circle += 1
    darker_circle = darker_circle % len(center_pos)

    # --- Finish the frame --- #
    pygame.display.flip()
    pygame.time.wait(300)
