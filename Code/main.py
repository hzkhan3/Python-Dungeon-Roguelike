import pygame
from Code.settings import *

# Set up pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

# Set up the main game loop 
while running:
    
    # If the user presses the exit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()