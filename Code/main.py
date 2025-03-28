import pygame
from settings import *

# Set up pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
running = True

tile_set = pygame.image.load('Assets/2D Pixel Dungeon Asset Pack/character and tileset/Dungeon_Tileset.png').convert()

# Set up the main game loop 
while running:
    
    # If the user presses the exit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill('purple')

    screen.blit(tile_set.subsurface((0, 16, 16, 16)), (64, 64))

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()