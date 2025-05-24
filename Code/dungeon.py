import pygame
import os 
import numpy as np
import random

class Dungeon:
    def __init__(self, width, height, tileset_image, tile_size = 16):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.grid = np.zeros((height, width), dtype = int)
        self.tiles = self.load_tiles(tileset_image)
    
    def load_tiles(self, tileset_image):
        tiles = {
            'wall': {
                'top': [tileset_image.subsurface((16, 0, self.tile_size, self.tile_size)),
                        tileset_image.subsurface((32, 0, self.tile_size, self.tile_size)),
                        tileset_image.subsurface((48, 0, self.tile_size, self.tile_size))],
                'bottom': [tileset_image.subsurface((16, 64, self.tile_size, self.tile_size)),
                           tileset_image.subsurface((32, 64, self.tile_size, self.tile_size)),
                           tileset_image.subsurface((48, 64, self.tile_size, self.tile_size))],
                'side_left': [tileset_image.subsurface((0, 16, self.tile_size, self.tile_size)),
                              tileset_image.subsurface((0, 32, self.tile_size, self.tile_size))],
                'side_right': [tileset_image.subsurface((80, 16, self.tile_size, self.tile_size)),
                               tileset_image.subsurface((80, 32, self.tile_size, self.tile_size))],
                'bottom_corner_left': [tileset_image.subsurface((0, 64, self.tile_size, self.tile_size))],
                'bottom_corner_right': [tileset_image.subsurface((80, 64, self.tile_size, self.tile_size))]
            },
            'floor': [tileset_image.subsurface((96, 0, self.tile_size, self.tile_size)),
                      tileset_image.subsurface((112, 0, self.tile_size, self.tile_size)),
                      tileset_image.subsurface((128, 0, self.tile_size, self.tile_size)),
                      tileset_image.subsurface((144, 0, self.tile_size, self.tile_size)),
                      tileset_image.subsurface((96, 16, self.tile_size, self.tile_size)),
                      tileset_image.subsurface((96, 32, self.tile_size, self.tile_size)),
                      tileset_image.subsurface((112, 16, self.tile_size, self.tile_size)),
                      tileset_image.subsurface((112, 32, self.tile_size, self.tile_size)),
                      tileset_image.subsurface((128, 16, self.tile_size, self.tile_size)),
                      tileset_image.subsurface((128, 32, self.tile_size, self.tile_size)),
                      tileset_image.subsurface((144, 16, self.tile_size, self.tile_size)),
                      tileset_image.subsurface((144, 32, self.tile_size, self.tile_size))],
        }

        return tiles

    def random_walk(self, start_x=None, start_y=None, steps=500):
        
        grid = self.grid

        # If no specified start area, automatically start from the middle
        if start_x == None:
            start_x = self.width // 2
        if start_y == None:
            start_y = self.height // 2
        
        # Start the middle with a floor
        x, y = start_x, start_y
        grid[y, x] = 1

        # Depending on a randomly generated number move in a specific direction and place a floor
        for _ in range(steps):
            direction = random.randint(1, 4)

            if direction == 1 and x > 0:
                x -= 1
            elif direction == 2 and x < self.width - 1:
                x += 1
            elif direction == 3 and y > 0:
                y -= 1
            elif direction == 4 and y < self.height - 1:
                y += 1
            
            grid[y, x] = 1
        
        return grid
    
    def draw(self, grid):
        for x in 
        