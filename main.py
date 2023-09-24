"""
Author: SantosXPC
Date: 24/09/2023
Description: This code creates a simple Pygame application that continuously draws random blue circles on a window. The circles have random positions and sizes, creating a visually dynamic effect.

Usage: Run the code, and a window titled "Just Blue" will open. Close the window to exit the application.

License: GNU General Public License (GPL)

"""

import pygame
import random
import time

# Initialize the Pygame library
pygame.init()

# Set the window caption
pygame.display.set_caption("Just Blue")

# Create a window with dimensions 800x600
screen = pygame.display.set_mode((800, 600))

# Main game loop
while True:
    for event in pygame.event.get():
        # Quit the game if the window is closed
        if event.type == pygame.QUIT:
            quit()

    # Fill the screen with a light blue color
    screen.fill((135, 206, 235))

    # Generate random coordinates and radius for the circle
    x = random.randint(10, 790)
    y = random.randint(10, 590)
    r = random.randint(10, 50)

    # Draw a random blue circle on the screen
    pygame.draw.circle(screen, (0, 0, 150), (x, y), r)

    # Update the display
    time.sleep(0.5)
    pygame.display.flip()