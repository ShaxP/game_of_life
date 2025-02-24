# Game of Life Implementation Exercise

## Overview

This exercise will help you implement Conway's Game of Life using Python and PyGame. The project demonstrates object-oriented programming, modular design, and working with external libraries.

## Requirements

- Python 3.7 or higher
- PyGame
- Pytest

## Setup

1. Clone this repository
1. Create and activate a virtual environment:

    ```bash
    # Create virtual environment
    python -m venv .venv

    # Activate virtual environment
    # On Windows:
    .venv\Scripts\activate
    # On macOS/Linux:
    source .venv/bin/activate
    ```

1. Install dependencies:

```bash
pip install -r requirements.txt
```

## Project Structure

- `game_of_life.py`: Contains the core game logic
- `visualizer.py`: Handles the graphical display using PyGame
- `test_game_of_life.py`: Contains tests for the game logic
- `.venv/`: Virtual environment directory (not tracked in git)

## Game Controls

- Click cells to toggle them between alive/dead
- Space bar to pause/resume the simulation
- Close window to exit

## Implementation Tasks

### 1. Complete the Grid Implementation

In `game_of_life.py`, implement the following methods in the `Grid` class:

#### a. `initialize_grid()`

- Create a 2D list for the grid
- Randomly initialize cells as alive (1) or dead (0)

#### b. `get_neighbors(row, col)`

- Count live neighbors for a cell at given coordinates
- Remember to handle edge cases
- Cells outside the grid are considered dead

#### c. `next_generation()`

- Create a new grid based on the Game of Life rules
- Apply all rules simultaneously to all cells

### 2. Rules of the Game

1. Any live cell with fewer than two live neighbors dies (under-population)
2. Any live cell with two or three live neighbors lives on to the next generation
3. Any live cell with more than three live neighbors dies (overpopulation)
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction)

### 3. Testing Your Implementation

Run the tests:

```bash
python -m pytest test_game_of_life.py
```

## Bonus Challenges

1. Add the ability to:
   - Save/load patterns to/from files
   - Clear the grid
   - Generate common patterns (glider, blinker, etc.)
2. Add controls for:
   - Simulation speed
   - Grid size
   - Cell colors
3. Implement:
   - Population statistics
   - Generation counter
   - Infinite grid

## Learning Objectives

- Object-oriented programming in Python
- Working with 2D lists
- Event handling with PyGame
- Writing and running tests
- Modular code design
- Game loop implementation

## Tips

- Break down the problem into smaller parts
- Test your implementation incrementally
- Use print statements or debugger to track issues
- Consider edge cases in your implementation
