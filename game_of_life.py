import random
from time import sleep

class Grid:
    def __init__(self, rows, cols):
        """
        Initialize the grid with specified dimensions.
        
        Args:
            rows (int): Number of rows in the grid
            cols (int): Number of columns in the grid
        """
        self.rows = rows
        self.cols = cols
        self.grid = None
        self.initialize_grid()

    def initialize_grid(self):
        """
        Initialize the grid with random live/dead cells.
        Live cells are represented by 1, dead cells by 0.
        """
        # TODO: Implement this method
        pass

    def get_neighbors(self, row, col):
        """
        Count the number of live neighbors for a cell.
        
        Args:
            row (int): Row coordinate of the cell
            col (int): Column coordinate of the cell
            
        Returns:
            int: Number of live neighbors
        """
        # TODO: Implement this method
        pass

    def next_generation(self):
        """
        Create the next generation based on the Game of Life rules.
        """
        # TODO: Implement this method
        pass

    def display(self):
        """
        Display the current state of the grid.
        Use 'O' for live cells and '.' for dead cells.
        """
        # TODO: Implement this method
        pass

def main():
    # Create a 20x20 grid
    grid = Grid(20, 20)
    
    # Run the simulation for 50 generations
    for _ in range(50):
        grid.display()
        grid.next_generation()
        sleep(0.2)  # Add a small delay to make the animation visible
        print("\033[H\033[J", end="")  # Clear the console (UNIX/Linux/MacOS)

if __name__ == "__main__":
    main() 