import sys
import pygame
import pygame_gui

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
        self.gui_width = 300
        self.width = cell_size * grid.cols + self.gui_width
        self.height = cell_size * grid.rows
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.gui_clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.paused = False
        self.mouse_pos = None
        self.off_screen = pygame.Surface((self.width, self.height))
        pygame.display.set_caption("Game of Life")

        # Gui stuff
        self.gui = pygame_gui.UIManager((self.gui_width, self.height))
        x = 10
        y = 10
        width = 100
        height = 50
        space = 10
        self.reset_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((x, y), (width, height)),
            text='Reset',
            manager=self.gui
        )
        y += height + space
        self.pause_button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((x, y), (width, height)),
            text='Resume' if self.paused else 'Pause',
            manager=self.gui
        )

        # Colors
        self.fg_color = (0, 0, 0)
        self.bg_color = (255, 255, 255)
        self.cell_border_color = (192, 192, 192)

    def draw_cells(self):
        self.off_screen.fill(self.cell_border_color)
        for row in range(self.grid.rows):
            for col in range(self.grid.cols):
                color = self.fg_color if self.grid.cell_at(row, col) else self.bg_color
                pygame.draw.rect(
                    self.off_screen,
                    color,
                    (
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size - 1,
                        self.cell_size - 1
                    ),
                    width=0
                )

    def draw_grid(self):
        """
        Draw the current state of the grid.
        """
        self.draw_cells()
        self.screen.blit(self.off_screen, (self.gui_width, 0))
        pygame.display.update()

    def loop(self):
        while True:
            time_delta = self.gui_clock.tick(self.fps)/1000.0
            self.handle_events()
            self.gui.update(time_delta)
            print(f"Paused: {self.paused}, label: {self.pause_button.text}")
            self.gui.draw_ui(self.screen)
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
                    self.toggle_pause()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = event.pos
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.reset_button:
                    self.grid.initialize_grid()
                elif event.ui_element == self.pause_button:
                    self.toggle_pause()
            self.gui.process_events(event)

    def toggle_pause(self):
        self.paused = not self.paused
        self.pause_button.set_text('Resume' if self.paused else 'Pause')
        self.gui.update(0.0)

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
