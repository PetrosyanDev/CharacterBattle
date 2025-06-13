from .base import Screen
import utils.colors as colors

class Game(Screen):
    def __init__(self, window, fonts, player_char, enemy_char):
        super().__init__(window, fonts)

        self.player_char = player_char
        self.enemy_char = enemy_char


    def render(self):
        self.window.fill(colors.BACKGROUND)

        # Add header
        header = self.fonts["H2"].render("Character: "+self.player_char.name, True, colors.PRIMARY)
        header_x = self.window.get_width() / 2 - header.get_width() / 2
        self.window.blit(header, (header_x, 40))