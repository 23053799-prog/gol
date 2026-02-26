class Cell:
    """
    Represents a single cell in the Game of Life grid.

    Each cell can be in one of two states: alive or dead.
    The state transitions are determined by the number of alive neighbors.
    """

    def __init__(self, x, y, alive=False):
        """
        Initialize a cell at the given position.

        Args:
            x (int): The x-coordinate of the cell in the grid
            y (int): The y-coordinate of the cell in the grid
            alive (bool): Initial state of the cell (default: False/dead)
        """
        self.x = x
        self.y = y
        self.alive = alive
        self.next_state = alive

    def toggle(self):
        """Toggle the cell's current state between alive and dead."""
        self.alive = not self.alive
        self.next_state = self.alive

    def set_alive(self, alive):
        """
        Set the cell's state explicitly.

        Args:
            alive (bool): True for alive, False for dead
        """
        self.alive = alive
        self.next_state = alive
    def apply_next_state(self):
        """Apply the next state calculated by Conway's rules."""
        self.alive = self.next_state

    def calculate_next_state(self, alive_neighbors):
        """
        Calculate the next state based on Conway's Game of Life rules.

        Rules:
        1. Any live cell with 2 or 3 live neighbors survives
        2. Any dead cell with exactly 3 live neighbors becomes alive
        3. All other live cells die in the next generation
        4. All other dead cells stay dead

        Args:
            alive_neighbors (int): Number of alive neighbors (0-8)
        """
        if self.alive:
            # Rule 1: Live cell with 2 or 3 neighbors survives
            self.next_state = alive_neighbors in (2, 3)
        else:
            # Rule 2: Dead cell with exactly 3 neighbors becomes alive
            self.next_state = alive_neighbors == 3

    def __repr__(self):
        """String representation of the cell."""
        state = "ALIVE" if self.alive else "DEAD"
        return f"Cell({self.x}, {self.y}) - {state}"
