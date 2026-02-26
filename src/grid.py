import random

from src.cell import Cell


class Grid:
    """
    Manages a 2D grid of cells for the Game of Life simulation.

    Handles cell creation, state updates, and neighbor calculations.
    """

    def __init__(self, width: int, height: int):
        """
        Initialize the grid with given dimensions.

        Args:
            width: Number of columns in the grid
            height: Number of rows in the grid
        """
        self.width = width
        self.height = height
        self.cells = [[Cell(x, y) for x in range(width)] for y in range(height)]

    def get_cell(self, x: int, y: int) -> Cell:
        """
        Get a cell at the specified coordinates.

        Args:
            x: X coordinate
            y: Y coordinate

        Returns:
            The cell at the given position
        """
        # Wrap coordinates for toroidal grid
        x = x % self.width
        y = y % self.height
        return self.cells[y][x]

    def count_alive_neighbors(self, x: int, y: int) -> int:
        """
        Count the number of alive neighbors for a cell.

        Args:
            x: X coordinate of the cell
            y: Y coordinate of the cell

        Returns:
            Number of alive neighbors (0-8)
        """
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue

                neighbor_x = (x + dx) % self.width
                neighbor_y = (y + dy) % self.height

                if self.cells[neighbor_y][neighbor_x].alive:
                    count += 1

        return count

    def update(self) -> None:
        """
        Calculate and apply the next generation of cells.

        First calculates the next state for all cells based on their neighbors,
        then updates all cells simultaneously to the next state.
        """
        # Calculate next states for all cells
        for y in range(self.height):
            for x in range(self.width):
                cell = self.cells[y][x]
                alive_neighbors = self.count_alive_neighbors(x, y)
                cell.calculate_next_state(alive_neighbors)

        # Apply next states
        for y in range(self.height):
            for x in range(self.width):
                self.cells[y][x].apply_next_state()

    def randomize(self) -> None:
        """Fill the grid with random dead/alive cells."""
        for y in range(self.height):
            for x in range(self.width):
                alive = random.choice([True, False])
                self.cells[y][x].set_alive(alive)

    def clear(self) -> None:
        """Clear the grid - make all cells dead."""
        for y in range(self.height):
            for x in range(self.width):
                self.cells[y][x].set_alive(False)

    def toggle_cell(self, x: int, y: int) -> None:
        """
        Toggle a cell at the specified coordinates.

        Args:
            x: X coordinate
            y: Y coordinate
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.cells[y][x].toggle()

    def set_cell(self, x: int, y: int, alive: bool) -> None:
        """
        Set a cell's state at the specified coordinates.

        Args:
            x: X coordinate
            y: Y coordinate
            alive: Whether the cell should be alive
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.cells[y][x].set_alive(alive)

    def get_alive_count(self) -> int:
        """
        Count the total number of alive cells.

        Returns:
            Number of alive cells in the grid
        """
        return sum(
            1
            for y in range(self.height)
            for x in range(self.width)
            if self.cells[y][x].alive
        )

    def get_generation_number(self) -> int:
        """
        Get a hash representing the current grid state.

        Useful for detecting oscillators or static patterns.

        Returns:
            Hash of the current grid state
        """
        state = ""
        for y in range(self.height):
            for x in range(self.width):
                state += "1" if self.cells[y][x].alive else "0"
        return hash(state)
