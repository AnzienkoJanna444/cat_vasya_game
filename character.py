import math
from unit import Unit

class Character(Unit):
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)

    def calculate_max_health(self):
        return math.floor(self.constitution * 10 + self.strength / 2)

    def calculate_damage(self):
        return math.floor(self.strength * 1.5 + self.dexterity / 4)

    def calculate_defense(self):
        return math.floor(self.constitution * 1.5 + self.dexterity / 3)