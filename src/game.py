import sys

import pygame

from src.grid import Grid
from src.renderer import Renderer


class Game:
    """Main game class that orchestrates the Game of Life simulation."""

    # Screen dimensions
    WINDOW_WIDTH = 1200
    WINDOW_HEIGHT = 800

    # Grid dimensions
    GRID_WIDTH = 100
    GRID_HEIGHT = 60
    CELL_SIZE = 10

    # Speed settings
    MIN_SPEED = 1
    MAX_SPEED = 10
    DEFAULT_SPEED = 2

    def __init__(self):
        """Initialize the Game of Life application."""
        pygame.init()

        # Create the game window
        self.screen = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pygame.display.set_caption("Conway's Game of Life")

        # Initialize grid and renderer
        self.grid = Grid(self.GRID_WIDTH, self.GRID_HEIGHT)
        self.renderer = Renderer(
            self.screen, self.GRID_WIDTH, self.GRID_HEIGHT, self.CELL_SIZE
        )

        # Game state
        self.is_running = True
        self.is_playing = False
        self.generation = 0
        self.simulation_speed = self.DEFAULT_SPEED

        # Clock for FPS management
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.frame_counter = 0
        self.current_fps = 0
