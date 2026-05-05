from abc import ABC, abstractmethod
import math

class Unit(ABC):
    def __init__(self, strength, dexterity, constitution, wisdom, intelligence, charisma):
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.spells = []
        self.mana = 0

    @abstractmethod
    def calculate_max_health(self):
        pass

    @abstractmethod
    def calculate_damage(self):
        pass

    @abstractmethod
    def calculate_defense(self):
        pass

    @abstractmethod
    def calculate_max_mana(self):
        pass

    def add_spell(self, spell):
        self.spells.append(spell)

    def cast_spell(self, index):
        if not (0 <= index < len(self.spells)):
            raise IndexError("Некорректный индекс заклинания")
        
        spell = self.spells[index]
        
        if self.mana >= spell.mana_cost:
            self.mana -= spell.mana_cost
            return spell.cast()
        else:
            raise ValueError(f"Недостаточно маны: нужно {spell.mana_cost}, доступно {self.mana}")