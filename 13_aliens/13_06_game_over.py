



import os
import pygame
from random import randint

# Ensure the working directory is set to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Sideways Shooter Part 2: Game Over")

# Load the ship image and set it to face right
character_image = pygame.image.load('character.png')  # Ensure 'character.png' is in the same folder
character_image = pygame.transform.scale(character_image, (50, 50))  # Resize ship
# Rotate the ship image to face 90 degrees to the right
character_image = pygame.transform.rotate(character_image, -90)  # Rotate 90 degrees counterclockwise
character_rect = character_image.get_rect()

# Set the ship's initial position
character_rect.left = 50  # Ship starts at the left side
character_rect.centery = screen.get_height() // 2  # Vertically centered

# Set the speed of the ship, bullets, and aliens (using floats for slower speeds)
ship_speed = 2.0  # Slow down the ship (float)
bullet_speed = 5.0  # Slow down the bullets (float)
alien_speed = 1.0  # Aliens will now move at 1.0 (slower but visible)

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

# Create the Alien class
class Alien:
    def __init__(self, x, y):
        self.image = pygame.image.load('alien.png')  # Load alien image
        self.image = pygame.transform.scale(self.image, (50, 50))  # Resize alien
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        """Move the alien towards the ship."""
        self.rect.x -= alien_speed  # Move left towards the ship

    def draw(self, screen):
        """Draw the alien on the screen."""
        screen.blit(self.image, self.rect)

# List to store bullets and aliens
bullets = []
aliens = []

# Create a fleet of aliens on the right side
for _ in range(5):  # Create 5 aliens for now
    x = screen.get_width() - randint(50, 100)  # Random x position on the right side
    y = randint(50, screen.get_height() - 50)  # Random y position within the screen
    aliens.append(Alien(x, y))

# Game counters
ship_hits = 0  # Track the number of times the ship is hit
alien_hits = 0  # Track the number of aliens hit by bullets

# Game over conditions
max_ship_hits = 3  # Game over if ship gets hit 3 times
max_alien_hits = 10  # Game over if the player hits 10 aliens

# Font for displaying text
font = pygame.font.SysFont(None, 55)

# Function to display the game over message
def display_game_over(message):
    game_over_text = font.render(message, True, (255, 255, 255))  # White text
    screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2))

# Main game loop
running = True
clock = pygame.time.Clock()  # To track the frame rate

while running:
    clock.tick(60)  # Maintain 60 FPS
    
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

    # Update alien positions and check for collisions
    for alien in aliens[:]:
        alien.update()  # Move the alien towards the ship
        # Check if the alien collides with the ship
        if alien.rect.colliderect(character_rect):
            ship_hits += 1  # Increment ship hit counter
            aliens.remove(alien)  # Remove alien if it hits the ship
            if ship_hits >= max_ship_hits:  # Check if the game over condition is met
                display_game_over("Game Over! Ship was hit too many times!")
                pygame.display.update()
                pygame.time.wait(2000)  # Wait 2 seconds before quitting
                running = False
                break
        # Check if the alien collides with any bullet
        for bullet in bullets[:]:
            if alien.rect.colliderect(bullet.rect):  # Collision detected
                aliens.remove(alien)  # Remove the alien if hit by bullet
                bullets.remove(bullet)  # Remove the bullet that hit the alien
                alien_hits += 1  # Increment alien hit counter
                break  # Stop checking other bullets after collision

        if alien.rect.x < 0:  # If the alien reaches the left side, remove it
            aliens.remove(alien)

    # Fill the screen with a black background
    screen.fill((0, 0, 0))  # Black background

    # Draw the ship (character) always facing right
    screen.blit(character_image, character_rect)

    # Draw all active bullets
    for bullet in bullets:
        bullet.draw(screen)

    # Draw all active aliens
    for alien in aliens:
        alien.draw(screen)

    # Display the number of aliens hit
    alien_hits_text = font.render(f"Aliens Hit: {alien_hits}", True, (255, 255, 255))  # White text
    screen.blit(alien_hits_text, (10, 10))

    # Display the number of ship hits
    ship_hits_text = font.render(f"Ship Hits: {ship_hits}", True, (255, 255, 255))  # White text
    screen.blit(ship_hits_text, (screen.get_width() - ship_hits_text.get_width() - 10, 10))

    # Check for game over (if alien_hits reach max_alien_hits)
    if alien_hits >= max_alien_hits:
        display_game_over("Game Over! You hit enough aliens!")
        pygame.display.update()
        pygame.time.wait(2000)  # Wait 2 seconds before quitting
        running = False

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()