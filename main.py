import pygame
from utils import fonts
from screens.welcome import Welcome
from screens.selection import CharacterSelection
from screens.game import Game
import entity

def main():
    pygame.init()
    FONT_DICT = fonts.load_fonts()

    SCREEN_SIZE = (1280, 720)
    window = pygame.display.set_mode(SCREEN_SIZE, pygame.RESIZABLE)
    pygame.display.set_caption("Character Battle")

    clock = pygame.time.Clock()
    FPS = 60

    character = entity.Zapdos


    welcome_scr = Welcome(window, FONT_DICT, character)
    select_scr = CharacterSelection(window, FONT_DICT, [
        entity.Zapdos,
        entity.Charizard,
        entity.Pidgeot,
    ])
    game_scr = Game(window, FONT_DICT)

    screens = [welcome_scr, select_scr, game_scr]
    active_idx = 0

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                    new_width = event.w
                    new_height = event.h

                    if new_width < SCREEN_SIZE[0]:
                        new_width = SCREEN_SIZE[0]
                    if new_height < SCREEN_SIZE[1]:
                        new_height = SCREEN_SIZE[1]

                    window = pygame.display.set_mode((new_width, new_height), pygame.RESIZABLE)
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_RETURN and active_idx == 0:
                    active_idx = active_idx + 1

            # let the active screen handle input if you expand later
            screens[active_idx].handle_event(event)

        # update & draw
        screens[active_idx].update()
        screens[active_idx].render()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
