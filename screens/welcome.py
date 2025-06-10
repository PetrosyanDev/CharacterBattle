# screens/welcome.py
import pygame
from .base import Screen
import utils.colors as colors

class Welcome(Screen):
    def __init__(self, window, fonts, char):
        super().__init__(window, fonts)
        self.char = char

    def render(self):
        self.window.fill(colors.BACKGROUND)
        header = self.fonts["H1"].render("Character Battle", True, colors.PRIMARY)
        x = self.window.get_width()/2 - header.get_width()/2
        self.window.blit(header, (x, 200))

        prompt = self.fonts["H3"].render("Press Enter to Begin", True, colors.BLACK_50)
        self.window.blit(prompt, (self.window.get_width()/2 - prompt.get_width()/2, 250 + header.get_height()))

        # zap_img = pygame.image.load(self.char.frames[0])
        # self.window.blit(zap_img, (0,0))
