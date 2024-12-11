

import pygame

# Initialize Pygame
pygame.init()


# Set up the display
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Game Character")

# Define background color (RGB format)
background_color = (0, 0, 255)  # Blue background

# Load the character image
character_image = pygame.image.load('character.png')  # Make sure your image file is named 'character.png' or update this path
character_rect = character_image.get_rect()

# Create a class to handle drawing the character
class GameCharacter:
    def __init__(self, image, screen):
        self.image = image
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.center = (screen.get_width() // 2, screen.get_height() // 2)  # Center on the screen

    def draw(self):
        # Fill the screen with the background color
        self.screen.fill(background_color)
        # Draw the character image at the center
        self.screen.blit(self.image, self.rect)

# Create an instance of the GameCharacter class
character = GameCharacter(character_image, screen)

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the character on the screen
    character.draw()

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
