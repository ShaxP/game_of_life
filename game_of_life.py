from time import sleep

from grid import Grid
from visualizer import GameVisualizer

def main():
    # Create a 20x20 grid
    grid = Grid(20, 20)
    visualizer = GameVisualizer()
    # Run the simulation for 50 generations
    while True:
        running, paused, _ = visualizer.handle_events()
        if not running:
            break
        if not paused:
            visualizer.draw_grid(grid.grid)
            grid.next_generation()
            sleep(0.2)

if __name__ == "__main__":
    main()
