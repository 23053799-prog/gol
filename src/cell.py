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
