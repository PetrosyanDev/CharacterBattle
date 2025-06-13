import pygame
import random
from .base import Screen
import utils.colors as colors

class Game(Screen):
    def __init__(self, window, fonts, player_char, enemy_char):
        super().__init__(window, fonts)
        self.window = window
        self.fonts = fonts
        self.player = player_char
        self.enemy = enemy_char
        self.buttons = []
        self.message = ''
        self.winner = ''

        # load images
        if not self.player or not self.player.frames or not self.enemy or not self.enemy.frames:
            return

        img = pygame.image.load(self.player.frames[0]).convert_alpha()
        self.player_img = pygame.transform.scale(img, (450, 450))

        img = pygame.image.load(self.enemy.frames[0]).convert_alpha()
        self.enemy_img = pygame.transform.scale(img, (450, 450))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.winner:
            for rect in self.buttons:
                if rect.collidepoint(event.pos):
                    self._attack(self.player, self.enemy)
                    if not self.winner:
                        self._attack(self.enemy, self.player)
                    break

    def _attack(self, attacker, defender):
        atk = random.choice(attacker.abilities)
        dmg = atk.calculate_damage(attacker, defender)
        if dmg == 0:
            text = f"{attacker.name} missed!"
        else:
            defender.take_damage(dmg)
            text = f"{attacker.name} hit {dmg}"
            if defender.is_defeated():
                self.winner = attacker.name
        # show message
        self.message = text
        self.render()
        pygame.display.update()
        pygame.time.delay(800)
        self.message = ''

    def render(self):
        w, h = self.window.get_size()
        self.window.fill(colors.BACKGROUND)

        # HP bars
        hp1 = self.fonts['H3'].render(f"{self.player.name} HP: {self.player.current_hp}", True, colors.PRIMARY)
        hp2 = self.fonts['H3'].render(f"{self.enemy.name} HP: {self.enemy.current_hp}", True, colors.RED)
        self.window.blit(hp1, (20, 20))
        self.window.blit(hp2, (w - hp2.get_width() - 20, 20))

        # draw characters
        pw, ph = self.player_img.get_size()
        self.window.blit(self.player_img, (w * 0.5 - pw, (h-ph)*0.5))
        _, eh = self.enemy_img.get_size()
        self.window.blit(self.enemy_img, (w * 0.5, (h-eh)*0.5))

        # message
        if self.message:
            msg = self.fonts['H3'].render(self.message, True, colors.RED)
            self.window.blit(msg, ((w - msg.get_width())//2, 100))

        # buttons with accuracy & power
        if not self.winner:
            self.buttons = []
            count = len(self.player.abilities)
            btn_w = (w - 20*(count+1)) // count
            y = h - 60 - 20
            for i, atk in enumerate(self.player.abilities):
                x = 20 + i * (btn_w + 20)
                rect = pygame.Rect(x, y, btn_w, 60)
                pygame.draw.rect(self.window, colors.PRIMARY, rect, border_radius=8)
                # name
                name = self.fonts['H5'].render(atk.name, True, colors.WHITE)
                self.window.blit(name, (x+5, y+5))
                # stats
                stats = self.fonts['P'].render(f"Acc:{atk.accuracy}% Pow:{atk.power}", True, colors.WHITE)
                self.window.blit(stats, (x+5, y+30))
                self.buttons.append(rect)

        # winner message
        if self.winner:
            win_txt = self.fonts['H2'].render(f"{self.winner} wins!", True, colors.GREEN)
            self.window.blit(win_txt, ((w - win_txt.get_width())//2, (h - win_txt.get_height())//2))
