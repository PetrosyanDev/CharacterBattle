
from entities.character import Character
import entities.ability as ability

# Zapdos
Zapdos = Character(name="Zapdos", elements=["ELECTRIC", "FLYING"], max_hp=180, atk=185,  defense=178, sp_atk=240, sp_def=185)
Zapdos.add_ability(ability.thunder_shock)
Zapdos.add_ability(ability.drill_peck)

# Charizard
Charizard = Character(name="Charizard", elements=["FIRE", "FLYING"], max_hp=129, atk=198, defense=188, sp_atk=259, sp_def=201)
Charizard.add_ability(ability.flamethrower)
Charizard.add_ability(ability.wing_attack)

# Pidgeot
Pidgeot = Character(name="Pidgeot",elements=["NORMAL", "FLYING"], max_hp=251, atk=166, defense=154, sp_atk=184, sp_def=160)
Pidgeot.add_ability(ability.drill_peck)
Pidgeot.add_ability(ability.wing_attack)