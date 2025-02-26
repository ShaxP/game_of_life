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
        self._grid = None
        self.initialize_grid()

    @classmethod
    def from_matrix(cls, matrix):
        """
        Create a Grid from a matrix.
        """
        grid = cls(len(matrix), len(matrix[0]))
        grid._grid = matrix
        return grid

    @property
    def grid(self):
        """
        Get the grid.
        """
        return self._grid

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

    def cell_at(self, row, col):
        """
        Get the value of a cell at a specific position.
        """
        pass
