class Ability:
    def __init__(self, name, power, type, accuracy):
        self.name = name
        self.power = power
        self.type_ = type
        self.accuracy = accuracy

    def calculate_damage(self, attacker, defender):
        # Todo: add accuracy 
        base_damage = (
            (attacker.atk / defender.defense) * self.power)
        return int(base_damage)
    

# All Abilities

# Elecrric
thunder_shock = Ability(name="Thunder Shock", power=10, type="ELECTRIC", accuracy=100)

# Flying
wing_attack = Ability(name="Wing Attack", power=60, type="FLYING", accuracy=80)
drill_peck = Ability(name="Drill Peck", power=80, type="FLYING", accuracy=50)

# fire
flamethrower = Ability(name="Flamethrower", power=90, type="FIRE", accuracy=35)
