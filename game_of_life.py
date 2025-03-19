import argparse

from grid import Grid
from visualizer import GameVisualizer

DEFAULT_ROWS = 50
DEFAULT_COLS = 50
DEFAULT_CELL_SIZE = 20

def main(rows, cols, cell_size):
    grid = Grid(rows, cols)
    visualizer = GameVisualizer(grid=grid, cell_size=cell_size)
    visualizer.loop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="Game of Life",
        description="This application let's the user play Conway's Game of Life"
    )
    parser.add_argument(
        "-r", "--rows",
        default=DEFAULT_ROWS,
        type=int,
        help="Number of rows in the game board"
    )
    parser.add_argument(
        "-c", "--cols",
        default=DEFAULT_COLS,
        type=int,
        help="Number of columns in the game board"
    )
    parser.add_argument(
        "-s", "--cell-size",
        default=DEFAULT_CELL_SIZE,
        type=int,
        help="The width and height of each cell in the game board"
    )

    args = parser.parse_args()
    main(rows=args.rows, cols=args.cols, cell_size=args.cell_size)
