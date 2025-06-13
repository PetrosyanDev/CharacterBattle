from .ability import Ability


class Character:
    def __init__(self, name, elements, max_hp, atk, defense, image=[]):
        self.name = name  # "Zapdos"
        self.elements = elements  # ["ELECTRIC", "FLYING"]
        self.max_hp = max_hp  # 200
        self.current_hp = max_hp  # 200
        self.atk = atk  # 185
        self.defense = defense  # 178
        self.abilities = []
        self.image = image  # ["./assets/zapdos_1.png"].


    def take_damage(self, damage):
        self.current_hp = max(0, self.current_hp - damage)

    def is_defeated(self):
        return self.current_hp <= 0

    def add_ability(self, ability: Ability):
        self.abilities.append(ability)