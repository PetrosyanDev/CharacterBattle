import pygame
import sys
from pygame.locals import QUIT

pygame.init()

screen = pygame.display.set_mode((1280, 720))

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
