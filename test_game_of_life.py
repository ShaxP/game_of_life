import pytest

from grid import Grid

@pytest.fixture
def blinker_pattern():
    return [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ]

@pytest.fixture
def toad_pattern():
    return [
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [1, 0, 0, 1],
        [0, 1, 0, 0],
    ]

@pytest.fixture
def neighbor_pattern():
    return [
        [1, 1, 0],
        [1, 0, 0],
        [0, 0, 0]
    ]

def test_grid_initialization():
    grid = Grid(4, 5)
    assert grid.rows == 4
    assert grid.cols == 5
    assert all(cell == 0 for row in grid.grid for cell in row)

def test_grid_randomization():
    grid = Grid(4, 5)
    assert grid.rows == 4
    assert grid.cols == 5
    assert all(cell in [0, 1] for row in grid.grid for cell in row)

def test_clear_grid(blinker_pattern):
    grid = Grid.from_matrix(blinker_pattern)
    assert grid.cell_at(0, 0) == 0
    assert grid.cell_at(1, 1) == 1
    grid.clear_grid()
    assert all(cell == 0 for row in grid.grid for cell in row)

def test_neighbor_counting(neighbor_pattern):
    grid = Grid.from_matrix(neighbor_pattern)
    assert grid.get_neighbors(0, 0) == 2
    assert grid.get_neighbors(1, 1) == 3
    assert grid.get_neighbors(2, 2) == 0

def test_next_generation(blinker_pattern):
    grid = Grid.from_matrix(blinker_pattern)
    grid.next_generation()
    assert grid.grid == [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ]

def test_toggle_cell_at():
    pattern = [
        [0, 1],
    ]
    grid = Grid.from_matrix(pattern)
    assert grid.grid[0][0] == 0
    assert grid.grid[0][1] == 1
    grid.toggle_cell_at(0, 0)
    grid.toggle_cell_at(0, 1)
    assert grid.grid[0][0] == 1
    assert grid.grid[0][1] == 0

def test_load_pattern(toad_pattern):
    grid = Grid(10, 10)
    grid.load_pattern(toad_pattern, 2, 3)
    assert grid.grid == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

def test_load_pattern_close_to_borders(toad_pattern):
    grid = Grid(10, 10)
    grid.load_pattern(toad_pattern, 8, 7)
    assert grid.grid == [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    ]
