import sys

import pygame
import pygame_gui
from pygame_gui.elements import UIButton

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
        self.gui_width = 150
        self.width = cell_size * grid.cols + self.gui_width
        self.height = cell_size * grid.rows
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.gui_clock = pygame.time.Clock()
        self.fps = fps
        self.running = True
        self.paused = True
        self.mouse_pos = None
        self.off_screen = pygame.Surface((self.width, self.height))
        pygame.display.set_caption("Game of Life")

        # Gui stuff
        self.gui = pygame_gui.UIManager((self.gui_width, self.height))
        self.event_handlers = {}
        x = 10
        y = 10
        width = 100
        height = 50
        space = 10
        self.pause_button = self.button(
            self.pause_button_label,
            x, y, width, height,
            self.toggle_pause
        )

        y += height + space
        self.button(
            "Clear",
            x, y, width, height,
            self.clear_grid
        )

        y += height + space
        self.button(
            "Randomize",
            x, y, width, height,
            self.randomize_grid
        )

        # Colors
        self.fg_color = (0, 0, 0)
        self.bg_color = (255, 255, 255)
        self.cell_border_color = (192, 192, 192)

    @property
    def pause_button_label(self) -> str:
        return "Resume" if self.paused else "Pause"

    def button(self, label: str, x, y, width, height, event_handler) -> UIButton:
        button = UIButton(
            relative_rect=pygame.Rect((x, y), (width, height)),
            text=label, manager=self.gui
        )
        self.event_handlers[button] = event_handler
        return button

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
                        self.cell_size - 1,
                    ),
                    width=0,
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
            time_delta = self.gui_clock.tick(self.fps) / 1000.0
            self.handle_events()
            self.gui.update(time_delta)
            self.gui.draw_ui(self.screen)
            if not self.running:
                self.cleanup()
                sys.exit()
            self.draw_grid()
            if not self.paused:
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
                    self.toggle_pause(self.pause_button)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_pos = event.pos
                pos = self.get_cell_position(event.pos)
                if pos:
                    self.grid.toggle_cell_at(pos[0], pos[1])
                    self.draw_grid()
            elif event.type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element in self.event_handlers:
                    handler = self.event_handlers[event.ui_element]
                    handler(event.ui_element)
            self.gui.process_events(event)

    def toggle_pause(self, button):
        self.paused = not self.paused
        button.set_text(self.pause_button_label)
        self.gui.update(0.0)

    def clear_grid(self, _):
        self.grid.clear_grid()

    def randomize_grid(self, _):
        self.grid.randomize_grid()

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
            if x < self.gui_width:
                return None
            return (y // self.cell_size, (x - self.gui_width) // self.cell_size)
        return None

    def cleanup(self):
        """
        Clean up PyGame resources.
        """
        pygame.quit()
