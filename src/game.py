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

    def handle_events(self) -> None:
        """Handle pygame events (keyboard, mouse, quit)."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

            elif event.type == pygame.KEYDOWN:
                self._handle_key_press(event.key)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.is_playing:  # Only allow drawing when paused
                    self._handle_mouse_click(event.pos)

    def _handle_key_press(self, key: int) -> None:
        """
        Handle keyboard input.

        Args:
            key: Pygame key constant
        """
        if key == pygame.K_SPACE:
            # Toggle play/pause
            self.is_playing = not self.is_playing

        elif key == pygame.K_r:
            # Randomize the grid
            self.grid.randomize()
            self.generation = 0

        elif key == pygame.K_c:
            # Clear the grid
            self.grid.clear()
            self.generation = 0

        elif key == pygame.K_q:
            # Quit the application
            self.is_running = False

        elif key == pygame.K_UP:
            # Increase simulation speed
            if self.simulation_speed < self.MAX_SPEED:
                self.simulation_speed += 1

        elif key == pygame.K_DOWN:
            # Decrease simulation speed
            if self.simulation_speed > self.MIN_SPEED:
                self.simulation_speed -= 1

    def _handle_mouse_click(self, mouse_pos: tuple) -> None:
        """
        Handle mouse clicks to draw/erase cells.

        Args:
            mouse_pos: (x, y) tuple of mouse position
        """
        grid_coords = self.renderer.get_cell_at_mouse(mouse_pos)
        if grid_coords:
            x, y = grid_coords
            self.grid.toggle_cell(x, y)

    def update(self) -> None:
        """Update the game state."""
        if self.is_playing:
            # Execute simulation step based on speed setting
            # Speed 1 = 1 step per frame, Speed 5 = 5 steps per frame, etc.
            for _ in range(self.simulation_speed):
                self.grid.update()
                self.generation += 1

    def render(self) -> None:
        """Render the game to the screen."""
        # Clear and draw the grid
        self.renderer.draw_grid(self.grid)

        # Draw UI overlay
        alive_count = self.grid.get_alive_count()
        self.renderer.draw_ui(
            self.is_playing,
            int(self.current_fps),
            self.generation,
            alive_count,
            self.simulation_speed,
        )

        # Update the display
        pygame.display.flip()

    def run(self) -> None:
        """Main game loop."""
        while self.is_running:
            # Handle events
            self.handle_events()

            # Update game state
            self.update()

            # Render
            self.render()

            # Control frame rate
            self.clock.tick(self.fps)

            # Calculate current FPS
            self.frame_counter += 1
            if self.frame_counter % 10 == 0:
                self.current_fps = self.clock.get_fps()

        # Cleanup
        pygame.quit()
        sys.exit()
