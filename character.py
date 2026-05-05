import math
from unit import Unit

class Character(Unit):
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma, character_class):
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
        
        valid_classes = ['warrior', 'mage', 'hunter']
        if character_class not in valid_classes:
            raise ValueError(f"Недопустимый класс персонажа: {character_class}")
        
        self.character_class = character_class
        self.max_health = self.calculate_max_health()
        self.current_health = self.max_health
        self.damage = self.calculate_damage()
        self.defense = self.calculate_defense()

    def calculate_max_health(self):
        return math.floor(self.constitution * 10 + self.strength / 2)

    def calculate_damage(self):
        if self.character_class == 'warrior':
            return math.floor(self.strength * 2.2 + self.constitution / 3)
        elif self.character_class == 'mage':
            return math.floor(self.intelligence * 2.5 + self.wisdom / 2)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.9 + self.strength / 3)

    def calculate_defense(self):
        if self.character_class == 'warrior':
            return math.floor(self.constitution * 1.8 + self.strength / 4)
        elif self.character_class == 'mage':
            return math.floor(self.wisdom * 1.3 + self.intelligence / 6)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.6 + self.constitution / 5)