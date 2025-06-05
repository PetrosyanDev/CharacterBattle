from entities.character import Character
from entities.ability import Ability
from characters import Zapdos, Charizard


def perform_attack(attacker: Character, defender: Character, ability: Ability):
    damage = ability.calculate_damage(attacker, defender)
    defender.take_damage(damage)
    return damage

# def main():

# 	pygame.init()
# 	SCREEN = (1280, 720)
# 	win = pygame.display.set_mode(SCREEN)

# 	clock = pygame.time.Clock()
# 	FPS = 60

# 	# game loop
# 	running = True
# 	while running:

# 		for event in pygame.event.get():
# 			if event.type == pygame.QUIT:
# 				running = False
# 			elif event.type == pygame.KEYDOWN:
# 				if event.key == pygame.K_ESCAPE:
# 					running = False

# 		clock.tick(FPS)
# 		pygame.display.update()

# 	pygame.quit()

# if __name__ == "__main__":
# 	main()


a = Zapdos
b = Charizard

print(a.current_hp)
print(b.current_hp)
perform_attack(a, b, a.abilities[0])
print(a.current_hp)
print(b.current_hp)