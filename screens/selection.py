import pygame
from .base import Screen
import utils.colors as colors

class CharacterSelection(Screen):
    def __init__(self, window, fonts, characters):
        super().__init__(window, fonts)
        self.window = window
        self.fonts = fonts
        self.characters = characters
        self.images = []
        self.selected = None
        self.buttons = []
        # load images
        for c in characters:
            img = pygame.image.load(c.image).convert_alpha()
            img = pygame.transform.scale(img, (200, 200))
            self.images.append(img)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for idx, btn in enumerate(self.buttons):
                if btn.collidepoint(event.pos):
                    self.selected = self.characters[idx]

    def render(self):
        w, h = self.window.get_size()
        self.window.fill(colors.BACKGROUND)

        # header
        hdr = self.fonts['H2'].render("Choose Your Character", True, colors.PRIMARY)
        self.window.blit(hdr, ((w - hdr.get_width()) / 2, 40))

        # layout
        n = len(self.characters)
        margin = 50
        card_w = (w - margin * (n + 1)) / n
        card_h = h - 200
        y = 140
        self.buttons = []

        # draw cards
        for i, char in enumerate(self.characters):
            x = margin + i * (card_w + margin)
            card = pygame.Rect(x, y, card_w, card_h)
            pygame.draw.rect(self.window, colors.SECONDARY, card, border_radius=12)

            # HP
            hp_txt = f"HP:{char.max_hp}"
            hp_img = self.fonts['H4'].render(hp_txt, True, colors.BLACK)
            self.window.blit(hp_img, (x + 10, y + 10))

            # image
            img = self.images[i]
            img_y = y + 10 + hp_img.get_height() + img.get_height() / 2
            img_rect = img.get_rect(center=(x + card_w / 2, img_y))
            self.window.blit(img, img_rect)


            # name
            name_img = self.fonts['H4'].render(char.name, True, colors.BLACK)
            nx = x + (card_w - name_img.get_width()) / 2
            self.window.blit(name_img, (nx, img_rect.bottom + 10))

            # stats
            stats_txt = f"ATK:{char.atk} DEF:{char.defense}"
            stats_img = self.fonts['P'].render(stats_txt, True, colors.BLACK_75)
            sx = x + (card_w - stats_img.get_width()) / 2
            self.window.blit(stats_img, (sx, img_rect.bottom + 40))

            # pick button
            btn = pygame.Rect(0, 0, 120, 40)
            btn.centerx = x + card_w / 2
            btn.bottom = y + card_h - 10
            pygame.draw.rect(self.window, colors.PRIMARY, btn, border_radius=8)
            pick_txt = self.fonts['H4'].render("Pick", True, colors.WHITE)
            px = btn.centerx - pick_txt.get_width() / 2
            py = btn.centery - pick_txt.get_height() / 2
            self.window.blit(pick_txt, (px, py))

            self.buttons.append(btn)

# .