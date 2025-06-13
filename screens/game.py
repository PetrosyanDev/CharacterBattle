import pygame
import random
from .base import Screen
import utils.colors as colors


class Game(Screen):
    MARGIN = 20
    BTN_H = 60

    def __init__(self, window, fonts, player_char, enemy_char):
        super().__init__(window, fonts)
        self.player_char = player_char
        self.enemy_char = enemy_char
        self.buttons = []
        self.winner = None
        self.wait = False
        self.next = 0
        if player_char and player_char.frames:
            self.player_img = pygame.image.load(player_char.frames[0]).convert_alpha()
        else:
            self.player_img = pygame.Surface((100, 100))
            self.player_img.fill(colors.BLACK_25)
        if enemy_char and enemy_char.frames:
            self.enemy_img = pygame.image.load(enemy_char.frames[0]).convert_alpha()
        else:
            self.enemy_img = pygame.Surface((100, 100))
            self.enemy_img.fill(colors.BLACK_25)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if not self.winner and not self.wait:
                for i, rect in enumerate(self.buttons):
                    if rect.collidepoint(event.pos):
                        atk = self.player_char.abilities[i]
                        dmg = atk.calculate_damage(self.player_char, self.enemy_char)
                        self.enemy_char.take_damage(dmg)
                        if self.enemy_char.is_defeated():
                            self.winner = self.player_char.name
                        self.buttons = []
                        self.wait = True
                        self.next = pygame.time.get_ticks() + 600
                        break

    def update(self):
        if self.wait and pygame.time.get_ticks() >= self.next:
            if not self.winner:
                atk = random.choice(self.enemy_char.abilities)
                dmg = atk.calculate_damage(self.enemy_char, self.player_char)
                self.player_char.take_damage(dmg)
                if self.player_char.is_defeated():
                    self.winner = self.enemy_char.name
            self.wait = False

    def render(self):
        self.window.fill(colors.BACKGROUND)
        p_text = f"{self.player_char.name} HP: {self.player_char.current_hp}"
        e_text = f"{self.enemy_char.name} HP: {self.enemy_char.current_hp}"
        p_img = self.fonts["H3"].render(p_text, True, colors.PRIMARY)
        e_img = self.fonts["H3"].render(e_text, True, colors.RED)
        self.window.blit(p_img, (40, 40))
        self.window.blit(e_img, (self.window.get_width() - e_img.get_width() - 40, 40))

        w, h = self.window.get_size()
        btn_w = (w - self.MARGIN * 3) / 2
        btn_y = h - self.BTN_H - self.MARGIN

        ps = w * 0.4 / self.player_img.get_width()
        pe = w * 0.3 / self.enemy_img.get_width()
        pi = pygame.transform.scale(self.player_img, (int(self.player_img.get_width() * ps), int(self.player_img.get_height() * ps)))
        ei = pygame.transform.scale(self.enemy_img, (int(self.enemy_img.get_width() * pe), int(self.enemy_img.get_height() * pe)))
        er = ei.get_rect()
        er.midright = (w * 0.75, btn_y - self.MARGIN)
        pr = pi.get_rect()
        pr.midleft = (w * 0.25, btn_y)
        self.window.blit(ei, er)
        self.window.blit(pi, pr)

        self.buttons = []
        if not self.wait and not self.winner:
            for i, atk in enumerate(self.player_char.abilities):
                x = self.MARGIN + i * (btn_w + self.MARGIN)
                rect = pygame.Rect(x, btn_y, btn_w, self.BTN_H)
                pygame.draw.rect(self.window, colors.PRIMARY, rect, border_radius=8)
                txt = self.fonts["H4"].render(atk.name, True, colors.WHITE)
                self.window.blit(txt, (rect.centerx - txt.get_width() / 2, rect.centery - txt.get_height() / 2))
                self.buttons.append(rect)

        if self.winner:
            msg = self.fonts["H2"].render(f"{self.winner} wins", True, colors.GREEN)
            self.window.blit(msg, (w / 2 - msg.get_width() / 2, h / 2 - msg.get_height() / 2))

