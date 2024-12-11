



import pygame

# Initialize Pygame
pygame.init()

# Set up the display (empty screen)
screen = pygame.display.set_mode((800, 600))  # 800x600 window
pygame.display.set_caption("Key Press Detection")

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Detect key presses
            print(f"Key pressed: {event.key}")  # Print the key's keycode

    # Fill the screen with a color (optional, can leave it blank)
    screen.fill((255, 255, 255))  # White background

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
 