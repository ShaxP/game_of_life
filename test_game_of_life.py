from grid import Grid

def test_grid_initialization():
    grid = Grid(5, 5)
    assert len(grid.grid) == 5
    assert len(grid.grid[0]) == 5
    assert all(cell in (0, 1) for row in grid.grid for cell in row)

def test_neighbor_counting():
    grid = Grid(3, 3)
    # Set up a specific pattern
    grid.grid = [
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]
    assert grid.get_neighbors(0, 0) == 2
    assert grid.get_neighbors(1, 1) == 3
    assert grid.get_neighbors(2, 2) == 0

def test_next_generation():
    grid = Grid(3, 3)
    # Set up a blinker pattern
    grid.grid = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    grid.next_generation()
    assert grid.grid == [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
