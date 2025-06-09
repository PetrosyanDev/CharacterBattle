import pygame
from .base import Screen
import utils.colors as colors

class Game(Screen):
    def render(self):
        self.window.fill(colors.BLACK_75)
        pygame.draw.rect(self.window, colors.RED, (200, 300, 100, 100), border_radius=20)
