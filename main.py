import pygame


def main():

	pygame.init()
	SCREEN = (1280, 720)
	win = pygame.display.set_mode(SCREEN)

	clock = pygame.time.Clock()
	FPS = 60

	# game loop
	running = True
	while running:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					running = False

		clock.tick(FPS)
		pygame.display.update()

	pygame.quit()





if __name__ == "__main__":
	main()