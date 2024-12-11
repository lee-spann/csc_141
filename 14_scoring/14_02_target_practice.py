


import os
import pygame
from random import randint

# Ensure the working directory is set to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Target Practice")

# Load the ship image and set it to face right
character_image = pygame.image.load('character.png')  # Ensure 'character.png' is in the same folder
character_image = pygame.transform.scale(character_image, (50, 50))  # Resize ship
# Rotate the ship image to face 90 degrees to the right
character_image = pygame.transform.rotate(character_image, -90)  # Rotate 90 degrees counterclockwise
character_rect = character_image.get_rect()

# Set the ship's initial position
character_rect.left = 50  # Ship starts at the left side
character_rect.centery = screen.get_height() // 2  # Vertically centered

# Set the speed of the ship, bullets, and target (using floats for slower speeds)
ship_speed = 2.0  # Slow down the ship (float)
bullet_speed = 5.0  # Slow down the bullets (float)
target_speed = 1.5  # Speed of the target

# Create the Bullet class
class Bullet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 5)  # Bullet is a small rectangle
        self.color = (255, 0, 0)  # Red color

    def update(self):
        """Move the bullet to the right."""
        self.rect.x += bullet_speed  # Move the bullet by bullet_speed

    def draw(self, screen):
        """Draw the bullet on the screen."""
        pygame.draw.rect(screen, self.color, self.rect)

# Create the Target class
class Target:
    def __init__(self):
        self.rect = pygame.Rect(screen.get_width() - 50, screen.get_height() // 2, 50, 30)  # Target is at the right edge
        self.color = (0, 255, 0)  # Green target
        self.speed = 1.5  # Initial speed of the target

    def update(self):
        """Move the target up and down."""
        self.rect.y += self.speed
        if self.rect.top <= 0 or self.rect.bottom >= screen.get_height():
            self.speed = -self.speed  # Reverse the direction when hitting the top or bottom

    def draw(self, screen):
        """Draw the target on the screen."""
        pygame.draw.rect(screen, self.color, self.rect)

# Game state variables
game_active = False  # Track whether the game is active or in the waiting state
misses = 0  # Track the number of misses
bullets = []
target = Target()

# Font for displaying text
font = pygame.font.SysFont(None, 55)

# Function to display a message on the screen
def display_message(message):
    message_text = font.render(message, True, (255, 255, 255))  # White text
    screen.blit(message_text, (screen.get_width() // 2 - message_text.get_width() // 2, screen.get_height() // 2))

# Function to start the game
def start_game():
    global game_active, misses, bullets, target
    game_active = True
    misses = 0
    bullets.clear()  # Clear the bullets list
    target = Target()  # Reset the target

# Create Play button
play_button_rect = pygame.Rect(screen.get_width() // 2 - 100, screen.get_height() // 2 + 50, 200, 50)

# Main game loop
running = True
clock = pygame.time.Clock()  # To track the frame rate

while running:
    clock.tick(60)  # Maintain 60 FPS
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not game_active:  # Press 'P' to start the game
                start_game()
            elif event.key == pygame.K_SPACE and game_active:
                # Create a bullet at the ship's position
                new_bullet = Bullet(character_rect.right, character_rect.centery)
                bullets.append(new_bullet)

    if game_active:
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

        # Check for collisions between bullets and the target
        for bullet in bullets[:]:
            if target.rect.colliderect(bullet.rect):  # Bullet hits the target
                bullets.remove(bullet)  # Remove the bullet
                target.rect.x = screen.get_width() - 50  # Reset target position
                target.rect.y = randint(50, screen.get_height() - 50)  # Reset random position
                target.speed = randint(1, 3)  # Reset random speed of target

        # Check for misses (when the target passes through the screen without being hit)
        if target.rect.top >= screen.get_height():
            misses += 1
            target.rect.x = screen.get_width() - 50  # Reset target position
            target.rect.y = randint(50, screen.get_height() - 50)  # Random reset position

        # Check for game over condition (3 misses)
        if misses >= 3:
            display_message("Game Over! Missed too many targets!")
            pygame.display.update()
            pygame.time.wait(2000)  # Wait 2 seconds before quitting
            game_active = False
            break

        # Update target and draw everything
        target.update()  # Update target position

        # Fill the screen with a black background
        screen.fill((0, 0, 0))  # Black background

        # Draw the ship (character) always facing right
        screen.blit(character_image, character_rect)

        # Draw the target
        target.draw(screen)

        # Draw all active bullets
        for bullet in bullets:
            bullet.draw(screen)

        # Display misses counter
        misses_text = font.render(f"Misses: {misses}", True, (255, 255, 255))  # White text
        screen.blit(misses_text, (10, 10))

    else:
        # Display the Play button
        pygame.draw.rect(screen, (0, 255, 0), play_button_rect)  # Green button
        display_message("Press P to Play")
    
    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()

