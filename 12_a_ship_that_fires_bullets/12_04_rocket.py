


import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Rocket Movement")

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Set the working directory to the script's folder


# Load the character image (rocket)
character_image = pygame.image.load('character.png')  # Your character image file

# Resize the image to make sure it's small enough for the screen
character_image = pygame.transform.scale(character_image, (50, 50))  # Resize to 50x50 pixels

# Get the rect of the image
character_rect = character_image.get_rect()

# Set initial position of the rocket (center of the screen)
character_rect.center = (400, 300)  # Center of the screen

# Set the speed of the rocket's movement
speed = 1

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the keys being pressed
    keys = pygame.key.get_pressed()

    # Move the rocket based on arrow key input
    if keys[pygame.K_LEFT]:
        character_rect.x -= speed  # Move left
    if keys[pygame.K_RIGHT]:
        character_rect.x += speed  # Move right
    if keys[pygame.K_UP]:
        character_rect.y -= speed  # Move up
    if keys[pygame.K_DOWN]:
        character_rect.y += speed  # Move down

    # Prevent the rocket from moving off the screen
    if character_rect.left < 0:
        character_rect.left = 0
    if character_rect.right > 800:
        character_rect.right = 800
    if character_rect.top < 0:
        character_rect.top = 0
    if character_rect.bottom > 600:
        character_rect.bottom = 600

    # Fill the screen with a color (e.g., black)
    screen.fill((0, 0, 0))  # Black background

    # Draw the rocket (character) at the new position
    screen.blit(character_image, character_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

