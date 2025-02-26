from grid import Grid


def test_grid_initialization():
    grid = Grid(4, 5)
    assert grid.rows == 4
    assert grid.cols == 5
    assert grid.grid is not None

def test_neighbor_counting():
    # Set up a specific pattern
    pattern = [
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]
    grid = Grid.from_matrix(pattern)
    assert grid.get_neighbors(0, 0) == 2
    assert grid.get_neighbors(1, 1) == 3
    assert grid.get_neighbors(2, 2) == 0

def test_next_generation():
    # Set up a blinker pattern
    pattern = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]
    grid = Grid.from_matrix(pattern)
    grid.next_generation()
    assert grid.grid == [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]
