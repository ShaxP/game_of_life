import pygame
import time

class GameVisualizer:
    def __init__(self, cell_size=20, width=800, height=600):
        """
        Initialize the PyGame visualizer.
        
        Args:
            cell_size (int): Size of each cell in pixels
            width (int): Window width in pixels
            height (int): Window height in pixels
        """
        pygame.init()
        self.cell_size = cell_size
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Game of Life")
        
        # Colors
        self.BLACK = (0, 0, 0)
        self.WHITE = (255, 255, 255)
        self.GRAY = (128, 128, 128)
        
        # Calculate grid dimensions
        self.cols = width // cell_size
        self.rows = height // cell_size

    def draw_grid(self, grid):
        """
        Draw the current state of the grid.
        
        Args:
            grid (list): 2D list representing the game grid
        """
        self.screen.fill(self.BLACK)
        
        # Draw cells
        for row in range(min(len(grid), self.rows)):
            for col in range(min(len(grid[0]), self.cols)):
                color = self.WHITE if grid[row][col] else self.BLACK
                pygame.draw.rect(self.screen,
                               color,
                               (col * self.cell_size,
                                row * self.cell_size,
                                self.cell_size - 1,
                                self.cell_size - 1))
        
        pygame.display.flip()

    def handle_events(self):
        """
        Handle PyGame events.
        
        Returns:
            tuple: (running, paused, mouse_pos)
        """
        running = True
        paused = False
        mouse_pos = None
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                
        return running, paused, mouse_pos

    def get_cell_position(self, mouse_pos):
        """
        Convert mouse position to grid coordinates.
        
        Args:
            mouse_pos (tuple): Mouse position in pixels
            
        Returns:
            tuple: Grid coordinates (row, col)
        """
        if mouse_pos:
            x, y = mouse_pos
            return (y // self.cell_size, x // self.cell_size)
        return None

    def cleanup(self):
        """
        Clean up PyGame resources.
        """
        pygame.quit() 