import math
from unit import Unit

class Monster(Unit):
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)

    def calculate_max_health(self):
        return math.floor(self.constitution * 8 + self.strength / 3)

    def calculate_damage(self):
        return math.floor(self.strength * 2 + self.constitution / 5)

    def calculate_defense(self):
        return math.floor(self.constitution * 1.2 + self.strength / 5)