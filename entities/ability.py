class Ability:
    def __init__(self, name, power, type_):
        self.name = name
        self.power = power
        self.type_ = type_
        # Todo: Add accuracy

    def calculate_damage(self, attacker, defender):
        multiplier = 1.0  # Todo: Implement type effectiveness
        base_damage = (
            (attacker.atk / defender.defense) * self.power) * multiplier
        return int(base_damage)