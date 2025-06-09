import entity
import pygame
import utils.colors as colors
import utils.fonts as fonts
import pygame


# Welcome Screen
def welcome():
    window.fill(colors.BACKGROUND)

    # Welcome Text
    header = FONTS["H1"].render("Character Battle", True, colors.PRIMARY)
    window.blit(header, (SCREEN[0]/2 - header.get_width()/2, 200))
    # window.blit(header, (100, 200))

    welcom = FONTS["H3"].render("Press Enter to Begin", True, colors.BLACK_50)
    window.blit(welcom, (SCREEN[0]/2 - welcom.get_width()/2, 250+header.get_height()))

    # # Draw Rect
    # pygame.draw.rect(window, colors.PRIMARY, (200, 300, 100, 100), border_radius=20)


    # Display Character
    zap_img = pygame.image.load(char.frames[0])
    window.blit(zap_img, (0, 0))


# Screen 2
def screen2():
    window.fill(colors.BLACK_75)

    # Draw Rect
    pygame.draw.rect(window, colors.RED, (200, 300, 100, 100))



def main():
    global window, char, SCREEN, FONTS
    char = entity.Zapdos

    pygame.init()
    FONTS = fonts.load_fonts()

    SCREEN = (1280, 720)
    window = pygame.display.set_mode(SCREEN)
    pygame.display.set_caption("Character Battle")

    clock = pygame.time.Clock()
    FPS = 60

    screens = [welcome, screen2]
    screencount = 0

    # game loop
    running = True
    while running:

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False
                if event.key == pygame.K_RETURN:
                    screencount = (screencount + 1) % len(screens)

        screens[screencount]()

        # update
        clock.tick(FPS)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
	main()


# OTHER

# a = entity.Zapdos
# b = entity.Charizard

# print(a.current_hp)
# print(b.current_hp)
# dmg = perform_attack(a, b, a.abilities[0])
# print(f'{a.name} used {a.abilities[0].name} and dealt {dmg} damage')
# print(a.current_hp)
# print(b.current_hp)




# def perform_attack(attacker: entity.Character, defender: entity.Character, ability: entity.Ability):
#     damage = ability.calculate_damage(attacker, defender)
#     defender.take_damage(damage)
#     return damage