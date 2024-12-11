

import os
import pygame
from random import randint

# Ensure the working directory is set to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Better Stars with More Spacing")

# Load the star image
star_image = pygame.image.load('star.png')  # Ensure 'star.png' is in the same folder
star_width, star_height = star_image.get_size()

# Define the spacing between stars
x_spacing = star_width * 1  # Horizontal spacing
y_spacing = star_height * 1  # Vertical spacing

# Calculate how many stars fit on the screen with the added spacing
rows = screen.get_height() // y_spacing
cols = screen.get_width() // x_spacing

# Generate a list of star positions with randomness and increased spacing
stars = []
for row in range(rows):
    for col in range(cols):
        x = col * x_spacing + randint(-10, 10)  # Add randomness to x position
        y = row * y_spacing + randint(-10, 10)  # Add randomness to y position
        stars.append((x, y))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a black background
    screen.fill((0, 0, 0))  # Black background

    # Draw the stars with their randomized positions
    for x, y in stars:
        screen.blit(star_image, (x, y))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
