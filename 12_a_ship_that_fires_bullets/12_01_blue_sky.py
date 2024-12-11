

import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Blue Sky")

# Define the blue color (RGB format)
blue = (0, 0, 255)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with blue color
    screen.fill(blue)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
