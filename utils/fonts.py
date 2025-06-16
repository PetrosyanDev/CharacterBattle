import pygame

font_name = "assets/font.ttf"

def load_fonts():
    return {
        "H1": pygame.font.Font(font_name, 60),
        "H2": pygame.font.Font(font_name, 48),
        "H3": pygame.font.Font(font_name, 36),
        "H4": pygame.font.Font(font_name, 24),
        "H5": pygame.font.Font(font_name, 16),
        "P": pygame.font.Font(font_name, 11)
    }

# https://www.fontspace.com/press-start-2p-font-f11591
# .