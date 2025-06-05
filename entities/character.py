from .ability import Ability


class Character:
    def __init__(self, name, elements, max_hp, atk, defense, sp_atk, sp_def):
        self.name = name  # e.g. "Zapdos"
        self.elements = elements  # e.g. ["ELECTRIC", "FLYING"]
        self.max_hp = max_hp  # e.g. 200
        self.current_hp = max_hp  # e.g. 200
        self.atk = atk  # e.g. 185
        self.defense = defense  # e.g. 178
        self.sp_atk = sp_atk  # e.g. 240
        self.sp_def = sp_def  # e.g. 185
        self.abilities = [
        ]  # e.g. [Ability("Thunder Shock", 40, "ELECTRIC")...]

    def take_damage(self, damage):
        self.current_hp = max(0, self.current_hp - damage)

    def is_defeated(self):
        return self.current_hp <= 0

    def add_ability(self, ability: Ability):
        self.abilities.append(ability)