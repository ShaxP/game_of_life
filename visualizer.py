import sys
import pygame

from grid import Grid

class GameVisualizer:
    def __init__(self, grid: Grid, cell_size=20, fps=10):
        """
        Initialize the PyGame visualizer.
        
        Args:
            grid (Grid): The grid to visualize
            cell_size (int): Size of each cell in pixels
            fps (int): Frames per second
        """
        pygame.init()
        self.grid = grid
        self.cell_size = cell_size
        self.width = cell_size * grid.cols
        self.height = cell_size * grid.rows
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.paused = False
        self.mouse_pos = None
        pygame.display.set_caption("Game of Life")

        # Colors
        self.bg_color = (0, 0, 0)
        self.fg_color = (255, 255, 255)


    def draw_grid(self):
        """
        Draw the current state of the grid.
        """
        self.screen.fill(self.bg_color)

        # Draw cells
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                color = self.fg_color if self.grid.cell_at(row, col) else self.bg_color
                pygame.draw.rect(self.screen,
                               color,
                               (col * self.cell_size,
                                row * self.cell_size,
                                self.cell_size - 1,
                                self.cell_size - 1))

        pygame.display.flip()

    def loop(self):
        while True:
            self.handle_events()
            if not self.running:
                self.cleanup()
                sys.exit()
            if not self.paused:
                self.draw_grid()
                self.grid.next_generation()
                self.clock.tick(self.fps)


    def handle_events(self):
        """
        Handle PyGame events.
        
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.paused = not self.paused
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = event.pos

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
