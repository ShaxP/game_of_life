import random

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
        self.grid = [[random.randint(0, 1) for _ in range(self.cols)] for _ in range(self.rows)]

    def get_neighbors(self, row, col):
        """
        Count the number of live neighbors for a cell.
        
        Args:
            row (int): Row coordinate of the cell
            col (int): Column coordinate of the cell
            
        Returns:
            int: Number of live neighbors
        """
        neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                n_row = row + i
                n_col = col + j
                if 0 <= n_row < self.rows and 0 <= n_col < self.cols:
                    neighbors += self.grid[n_row][n_col]
        return neighbors

    def next_generation(self):
        """
        Create the next generation based on the Game of Life rules.
        """
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                neighbors = self.get_neighbors(row, col)

                # Any live cell with fewer than two live neighbors dies (under-population)
                if self.grid[row][col] == 1 and (neighbors < 2):
                    new_grid[row][col] = 0
                # Any live cell with two or three live neighbors lives on to the next generation
                elif self.grid[row][col] == 1 and (neighbors == 2 or neighbors == 3):
                    new_grid[row][col] = 1
                # Any live cell with more than three live neighbors dies (overpopulation)
                elif self.grid[row][col] == 1 and (neighbors > 3):
                    new_grid[row][col] = 0
                # Any dead cell with exactly three live neighbors becomes a live cell (reproduction)
                elif self.grid[row][col] == 0 and (neighbors == 3):
                    new_grid[row][col] = 1
        self.grid = new_grid
