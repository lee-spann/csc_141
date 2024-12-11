


import os
import pygame
from random import randint

# Ensure the working directory is set to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Steady Rain")

# Load the raindrop image
raindrop_image = pygame.image.load('raindrop.png')  # Ensure 'raindrop.png' is in the same folder
raindrop_width, raindrop_height = raindrop_image.get_size()

# Define the spacing between raindrops
x_spacing = raindrop_width * 2  # Horizontal spacing
y_spacing = raindrop_height * 2  # Vertical spacing

# Calculate how many raindrops fit on the screen with the added spacing
rows = screen.get_height() // y_spacing
cols = screen.get_width() // x_spacing

# List to store raindrop positions and speeds
raindrops = []
for row in range(rows):
    for col in range(cols):
        x = col * x_spacing + randint(-10, 10)  # Add randomness to x position
        y = row * y_spacing + randint(-10, 10)  # Add randomness to y position
        speed = randint(2, 5)  # Random falling speed for each raindrop
        raindrops.append([x, y, speed])

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the screen with a black background
    screen.fill((0, 0, 0))  # Black background

    # Update the position of each raindrop and draw it
    for raindrop in raindrops[:]:
        raindrop[1] += raindrop[2]  # Move raindrop down by its speed

        # If the raindrop moves off the bottom, reset its position to the top
        if raindrop[1] > screen.get_height():
            raindrop[1] = randint(-10, -5)  # Reset the raindrop's Y position to just above the screen
            raindrop[0] = randint(0, screen.get_width() - raindrop_width)  # Randomize X position

        # Draw the raindrop
        screen.blit(raindrop_image, (raindrop[0], raindrop[1]))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
