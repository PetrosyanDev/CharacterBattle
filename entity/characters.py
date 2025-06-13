from . import ability, Character

# Zapdos
Zapdos = Character(name="Zapdos", elements=["ELECTRIC", "FLYING"], max_hp=180, atk=175,  defense=178, image="./assets/zapdos_1.png")
Zapdos.add_ability(ability.thunder_shock)
Zapdos.add_ability(ability.drill_peck)

# Charizard
Charizard = Character(name="Charizard", elements=["FIRE", "FLYING"], max_hp=129, atk=198, defense=168, image="./assets/charizard_1.png")
Charizard.add_ability(ability.flamethrower)
Charizard.add_ability(ability.wing_attack)

# Pidgeot
# Pidgeot = Character(name="Pidgeot",elements=["NORMAL", "FLYING"], max_hp=251, atk=166, defense=154, frames=[]).
Pidgeot = Character(name="Pidgeot",elements=["NORMAL", "FLYING"], max_hp=200, atk=156, defense=154, image="./assets/pidgeot_1.png")
Pidgeot.add_ability(ability.drill_peck)
Pidgeot.add_ability(ability.wing_attack)