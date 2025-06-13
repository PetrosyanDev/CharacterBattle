import pygame
import random
from .base import Screen
import utils.colors as colors


class Game(Screen):
    MARGIN = 20
    BTN_H = 80

    def __init__(self, window, fonts, player_char, enemy_char):
        super().__init__(window, fonts)
        self.window = window
        self.fonts = fonts
        self.player_char = player_char
        self.enemy_char = enemy_char
        self.buttons = []
        self.winner = None

        # timing & state
        self.wait = False
        self.next = 0
        self.message = None
        self.message_end = 0
        self.last_owner = None  # 'player' or 'enemy'

        # load or placeholder images
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
                        # queue player attack
                        self._queue_attack(self.player_char, self.enemy_char, 'player')
                        self.buttons = []
                        break

    def update(self):
        now = pygame.time.get_ticks()
        if not self.wait:
            return

        # message display phase
        if self.message:
            if now < self.message_end:
                return
            # message finished
            self.message = None
            if self.last_owner == 'player':
                # after player's action (hit or miss), enemy turn
                self._queue_attack(self.enemy_char, self.player_char, 'enemy')
                return
            # after enemy message or miss
            self.wait = False
            return

        # pause phase after a hit
        if now < self.next:
            return

        # after enemy hit pause, return control to player
        if self.last_owner == 'enemy':
            self.wait = False
            return

        # if player's hit pause, now it's enemy turn
        if not self.winner and self.last_owner == 'player':
            self._queue_attack(self.enemy_char, self.player_char, 'enemy')
            return

        # clear wait if game ended
        self.wait = False

    def render(self):
        self.window.fill(colors.BACKGROUND)

        # draw HP
        p_img = self.fonts['H3'].render(
            f"{self.player_char.name} HP: {self.player_char.current_hp}", True, colors.PRIMARY
        )
        e_img = self.fonts['H3'].render(
            f"{self.enemy_char.name} HP: {self.enemy_char.current_hp}", True, colors.RED
        )
        self.window.blit(p_img, (40, 40))
        self.window.blit(e_img, (self.window.get_width() - e_img.get_width() - 40, 40))

        w, h = self.window.get_size()
        btn_w = (w - self.MARGIN * 3) / 2
        btn_y = h - self.BTN_H - self.MARGIN

        # scale and position images
        player_scale = min(h * 0.7 / self.player_img.get_height(), w / h)
        enemy_scale = min(h * 0.5 / self.enemy_img.get_height(), w / h)
        player_img = pygame.transform.scale(
            self.player_img,
            (int(self.player_img.get_width() * player_scale), int(self.player_img.get_height() * player_scale)),
        )
        enemy_img = pygame.transform.scale(
            self.enemy_img,
            (int(self.enemy_img.get_width() * enemy_scale), int(self.enemy_img.get_height() * enemy_scale)),
        )
        pr = player_img.get_rect(bottomright=(w * 0.5 - self.MARGIN, btn_y - self.MARGIN))
        er = enemy_img.get_rect(bottomleft=(w * 0.5 + self.MARGIN, btn_y - self.MARGIN))
        self.window.blit(enemy_img, er)
        self.window.blit(player_img, pr)

        # draw message
        if self.message:
            txt = self.fonts['H3'].render(self.message, True, colors.RED)
            x = (w - txt.get_width()) // 2
            y = h - txt.get_height() - self.MARGIN * 2
            self.window.blit(txt, (x, y))

        # draw buttons
        self.buttons = []
        if not self.wait and not self.winner:
            for i, atk in enumerate(self.player_char.abilities):
                x = self.MARGIN + i * (btn_w + self.MARGIN)
                rect = pygame.Rect(x, btn_y, btn_w, self.BTN_H)  # increase height
                pygame.draw.rect(self.window, colors.PRIMARY, rect, border_radius=8)

                # Attack name (centered)
                label = self.fonts['H4'].render(atk.name, True, colors.WHITE)
                self.window.blit(
                    label,
                    (rect.centerx - label.get_width() / 2, rect.y + self.MARGIN*0.7)
                )

                # Info line below: [Type]       [Accuracy]       [Power]
                type_label = self.fonts['H5'].render(atk.type.capitalize(), True, colors.BLACK_25)
                acc_label = self.fonts['H5'].render(f"Acc: {atk.accuracy}%", True, colors.BLACK_25)
                pow_label = self.fonts['H5'].render(f"Pow: {atk.power}", True, colors.BLACK_25)

                self.window.blit(type_label, (rect.x + self.MARGIN, rect.y + self.MARGIN*1.2 + label.get_height()))
                self.window.blit(acc_label, (rect.centerx - acc_label.get_width() / 2, rect.y + self.MARGIN*1.2 + label.get_height()))
                self.window.blit(pow_label, (rect.right - pow_label.get_width() - self.MARGIN, rect.y + self.MARGIN*1.2 + label.get_height()))

                self.buttons.append(rect)


        # draw end panel
        if self.winner:
            panel_w, panel_h = w * 0.75, 150
            panel_rect = pygame.Rect((w - panel_w) / 2, (h - panel_h) / 2, panel_w, panel_h)
            pygame.draw.rect(self.window, colors.PRIMARY, panel_rect, border_radius=15)
            pygame.draw.rect(self.window, colors.BLACK_25, panel_rect, 3, border_radius=15)
            msg = self.fonts['H2'].render(f"{self.winner} wins", True, colors.GREEN)
            self.window.blit(msg, (w / 2 - msg.get_width() / 2, h / 2 - msg.get_height() / 2))

    def _queue_attack(self, attacker, defender, owner_type):
        now = pygame.time.get_ticks()
        self.last_owner = owner_type
        atk = random.choice(attacker.abilities)
        dmg = atk.calculate_damage(attacker, defender)

        if dmg == 0:
            # miss: show message
            self.message = f"{attacker.name} missed!"
            self.message_end = now + 1600
        else:
            # hit: apply damage and pause
            defender.take_damage(dmg)
            if defender.is_defeated():
                self.winner = attacker.name
            self.next = now + 1600

        # lock input until message or pause finishes
        self.wait = True
