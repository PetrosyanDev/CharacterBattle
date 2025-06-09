import pygame
from .base import Screen
import utils.colors as colors


class CharacterSelection(Screen):
    CARD_SIZE = (260, 360)
    IMAGE_SIZE = (150, 150)

    def __init__(self, window, fonts, characters):
        super().__init__(window, fonts)
        self.characters = characters
        self.images = []
        for char in characters:
            if char.frames:
                img = pygame.image.load(char.frames[0])
                img = pygame.transform.scale(img, self.IMAGE_SIZE)
            else:
                img = pygame.Surface(self.IMAGE_SIZE)
                img.fill(colors.BLACK_25)
            self.images.append(img)

    def render(self):
        self.window.fill(colors.BACKGROUND)
        header = self.fonts["H2"].render("Choose Your Character", True, colors.PRIMARY)
        header_x = self.window.get_width() / 2 - header.get_width() / 2
        self.window.blit(header, (header_x, 40))

        total_width = len(self.characters) * self.CARD_SIZE[0] + (len(self.characters) - 1) * 40
        start_x = (self.window.get_width() - total_width) / 2
        y = 120

        for idx, char in enumerate(self.characters):
            x = start_x + idx * (self.CARD_SIZE[0] + 40)
            card_rect = pygame.Rect(x, y, *self.CARD_SIZE)
            shadow_rect = card_rect.move(5, 5)
            pygame.draw.rect(self.window, colors.BLACK_50, shadow_rect, border_radius=15)
            pygame.draw.rect(self.window, colors.SECONDARY, card_rect, border_radius=15)

            img_rect = pygame.Rect(0, 0, *self.IMAGE_SIZE)
            img_rect.centerx = card_rect.centerx
            img_rect.top = card_rect.top + 20
            self.window.blit(self.images[idx], img_rect)

            text_y = img_rect.bottom + 10
            name_text = self.fonts["H4"].render(char.name, True, colors.BLACK)
            name_x = card_rect.centerx - name_text.get_width() / 2
            self.window.blit(name_text, (name_x, text_y))

            stats = f"ATK: {char.atk}  DEF: {char.defense}"
            stats_text = self.fonts["P"].render(stats, True, colors.BLACK)
            stats_x = card_rect.centerx - stats_text.get_width() / 2
            self.window.blit(stats_text, (stats_x, text_y + name_text.get_height() + 5))

            btn_rect = pygame.Rect(0, 0, 180, 40)
            btn_rect.centerx = card_rect.centerx
            btn_rect.bottom = card_rect.bottom - 20
            pygame.draw.rect(self.window, colors.PRIMARY, btn_rect, border_radius=8)
            btn_text = self.fonts["H4"].render("Choose Character", True, colors.WHITE)
            btn_text_x = btn_rect.centerx - btn_text.get_width() / 2
            btn_text_y = btn_rect.centery - btn_text.get_height() / 2
            self.window.blit(btn_text, (btn_text_x, btn_text_y))

