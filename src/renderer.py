from typing import Optional, Tuple

import pygame


class Renderer:
    """Handles rendering of the Game of Life grid and UI elements."""

    def __init__(
        self,
        screen: pygame.Surface,
        grid_width: int,
        grid_height: int,
        cell_size: int = 10,
    ):
        """
        Initialize the renderer.

        Args:
            screen: Pygame surface to render to
            grid_width: Number of columns in the grid
            grid_height: Number of rows in the grid
            cell_size: Size of each cell in pixels (default: 10)
        """
        self.screen = screen
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size

        # Calculate grid offset to center it on screen
        self.grid_offset_x = 10
        self.grid_offset_y = 10

        # Colors
        self.COLOR_BACKGROUND = (20, 20, 20)
        self.COLOR_GRID_LINE = (50, 50, 50)
        self.COLOR_ALIVE_CELL = (0, 255, 100)
        self.COLOR_DEAD_CELL = (40, 40, 40)
        self.COLOR_TEXT = (200, 200, 200)
        self.COLOR_ACCENT = (100, 200, 255)
        self.COLOR_BUTTON = (80, 80, 80)
        self.COLOR_BUTTON_HOVER = (100, 100, 100)

        # Font for UI text
        self.font_small = pygame.font.Font(None, 24)
        self.font_medium = pygame.font.Font(None, 32)

    def draw_grid(self, grid) -> None:
        """
        Draw the grid of cells.

        Args:
            grid: Grid object containing the cells
        """
        # Draw background
        self.screen.fill(self.COLOR_BACKGROUND)

        # Draw cells
        for y in range(grid.height):
            for x in range(grid.width):
                cell = grid.cells[y][x]
                self._draw_cell(x, y, cell.alive)

        # Draw grid lines
        self._draw_grid_lines()

    def _draw_cell(self, x: int, y: int, alive: bool) -> None:
        """
        Draw a single cell.

        Args:
            x: X coordinate in grid
            y: Y coordinate in grid
            alive: Whether the cell is alive
        """
        screen_x = self.grid_offset_x + x * self.cell_size
        screen_y = self.grid_offset_y + y * self.cell_size

        color = self.COLOR_ALIVE_CELL if alive else self.COLOR_DEAD_CELL

        pygame.draw.rect(
            self.screen, color, (screen_x, screen_y, self.cell_size, self.cell_size)
        )

    def _draw_grid_lines(self) -> None:
        """Draw the grid lines."""
        # Vertical lines
        for x in range(self.grid_width + 1):
            start_pos = (self.grid_offset_x + x * self.cell_size, self.grid_offset_y)
            end_pos = (
                self.grid_offset_x + x * self.cell_size,
                self.grid_offset_y + self.grid_height * self.cell_size,
            )
            pygame.draw.line(self.screen, self.COLOR_GRID_LINE, start_pos, end_pos, 1)

        # Horizontal lines
        for y in range(self.grid_height + 1):
            start_pos = (self.grid_offset_x, self.grid_offset_y + y * self.cell_size)
            end_pos = (
                self.grid_offset_x + self.grid_width * self.cell_size,
                self.grid_offset_y + y * self.cell_size,
            )
            pygame.draw.line(self.screen, self.COLOR_GRID_LINE, start_pos, end_pos, 1)

    def draw_ui(
        self, is_playing: bool, fps: int, generation: int, alive_count: int, speed: int
    ) -> None:
        """
        Draw the UI overlay with status information.

        Args:
            is_playing: Whether the simulation is currently running
            fps: Current frames per second
            generation: Current generation number
            alive_count: Number of alive cells
            speed: Current simulation speed
        """
        # Draw status bar background
        status_bar_height = 60
        pygame.draw.rect(
            self.screen,
            self.COLOR_BUTTON,
            (0, 0, self.screen.get_width(), status_bar_height),
        )

        # Draw status text
        status_text = "PLAYING" if is_playing else "PAUSED"
        status_color = self.COLOR_ALIVE_CELL if is_playing else (200, 100, 100)
        status_surface = self.font_small.render(status_text, True, status_color)
        self.screen.blit(status_surface, (10, 5))

        # Draw generation and alive count
        info_text = (
            f"Gen: {generation} | Alive: {alive_count} | Speed: {speed}x | FPS: {fps}"
        )
        info_surface = self.font_small.render(info_text, True, self.COLOR_TEXT)
        self.screen.blit(info_surface, (10, 30))

        # Draw controls help text
        controls_text = (
            "SPACE: Play/Pause | R: Randomize | C: Clear | ↑/↓: Speed | Click: Draw"
        )
        controls_surface = self.font_small.render(
            controls_text, True, self.COLOR_ACCENT
        )
        self.screen.blit(controls_surface, (10, self.screen.get_height() - 25))

    def get_cell_at_mouse(
        self, mouse_pos: Tuple[int, int]
    ) -> Optional[Tuple[int, int]]:
        """
        Get the grid coordinates of the cell at the mouse position.

        Args:
            mouse_pos: (x, y) tuple of mouse position

        Returns:
            (grid_x, grid_y) tuple or None if mouse is outside grid
        """
        mouse_x, mouse_y = mouse_pos

        # Check if mouse is within grid bounds
        grid_left = self.grid_offset_x
        grid_top = self.grid_offset_y
        grid_right = grid_left + self.grid_width * self.cell_size
        grid_bottom = grid_top + self.grid_height * self.cell_size

        if not (
            grid_left <= mouse_x < grid_right and grid_top <= mouse_y < grid_bottom
        ):
            return None

        # Calculate grid coordinates
        grid_x = (mouse_x - grid_left) // self.cell_size
        grid_y = (mouse_y - grid_top) // self.cell_size

        return (grid_x, grid_y)

    def set_cell_size(self, new_size: int) -> None:
        """
        Set the cell size and recalculate grid positioning.

        Args:
            new_size: New cell size in pixels
        """
        if new_size > 2:
            self.cell_size = new_size

    def clear_screen(self) -> None:
        """Clear the screen to background color."""
        self.screen.fill(self.COLOR_BACKGROUND)
