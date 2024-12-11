


import pygame

import os
print("Current working directory:", os.getcwd())


# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Grid of Stars")

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


# Load the star image
star_image = pygame.image.load('star.png')  # Make sure the file is in the same folder
star_width, star_height = star_image.get_size()

# Calculate how many stars fit on the screen
rows = screen.get_height() // star_height
cols = screen.get_width() // star_width

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a black background
    screen.fill((0, 0, 0))  # Black background

    # Draw the grid of stars
    for row in range(rows):
        for col in range(cols):
            x = col * star_width  # X position for this star
            y = row * star_height  # Y position for this star
            screen.blit(star_image, (x, y))  # Draw the star at (x, y)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
