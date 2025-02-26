from grid import Grid
from visualizer import GameVisualizer


def main():
    # Create a 30x40 grid
    grid = Grid(30, 40)
    visualizer = GameVisualizer(grid=grid)
    visualizer.loop()

if __name__ == "__main__":
    main()
