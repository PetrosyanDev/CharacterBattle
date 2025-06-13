import random

class Ability:
    def __init__(self, name, power, type, accuracy):
        self.name = name
        self.power = power
        self.type = type
        self.accuracy = accuracy

    def calculate_damage(self, attacker, defender):
        if random.randint(1, 100) > self.accuracy:
            return 0

        base_damage = (
            (attacker.atk / defender.defense) * self.power)
        return int(base_damage)
    

# All Abilities.

# Elecrric
thunder_shock = Ability(name="Thunder Shock", power=20, type="ELECTRIC", accuracy=100)

# Flying
wing_attack = Ability(name="Wing Attack", power=34, type="FLYING", accuracy=80)
drill_peck = Ability(name="Drill Peck", power=50, type="FLYING", accuracy=50)

# fire
flamethrower = Ability(name="Flamethrower", power=80, type="FIRE", accuracy=20)
