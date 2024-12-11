


import pygame

import os
print("Current working directory:", os.getcwd())


# Initialize Pygame
pygame.init()


# Set up the display
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Sideways Shooter with Resized Ship")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # Set the working directory to the script's folder


# Load the character image (rocket)
character_image = pygame.image.load('character.png')  # Your character image file

# Resize the image to make sure it's small enough for the screen
character_image = pygame.transform.scale(character_image, (50, 50))  # Resize to 50x50 pixels

# Get the rect of the image
character_rect = character_image.get_rect()

# Set initial position of the rocket (left side of the screen)
character_rect.left = 50  # Ship starts at the left side
character_rect.centery = screen.get_height() // 2  # Vertically centered

# Set the speed of the ship
ship_speed = 1

# Create a Bullet class
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 5)  # Bullet is a small rectangle
        self.color = RED

    def update(self):
        """Move the bullet to the right."""
        self.rect.x += 10  # Move the bullet to the right

    def draw(self, screen):
        """Draw the bullet on the screen."""
        pygame.draw.rect(screen, self.color, self.rect)

# List to store active bullets
bullets = []

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Create a bullet at the ship's position
                new_bullet = Bullet(character_rect.right, character_rect.centery)
                bullets.append(new_bullet)

    # Get the keys being pressed
    keys = pygame.key.get_pressed()

    # Move the ship up and down
    if keys[pygame.K_UP] and character_rect.top > 0:
        character_rect.y -= ship_speed  # Move up
    if keys[pygame.K_DOWN] and character_rect.bottom < screen.get_height():
        character_rect.y += ship_speed  # Move down

    # Update bullet positions and remove bullets that go off the screen
    for bullet in bullets[:]:
        bullet.update()  # Move the bullet
        if bullet.rect.right > screen.get_width():  # If the bullet moves off screen
            bullets.remove(bullet)  # Delete the bullet

    # Fill the screen with a black background
    screen.fill(BLACK)

    # Draw the ship (character) at the new position
    screen.blit(character_image, character_rect)

    # Draw all active bullets
    for bullet in bullets:
        bullet.draw(screen)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()


