import math
from unit import Unit


class Character(Unit):
    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int , intelligence: int, charisma: int, character_class: str):
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
        """
        Инициализирует персонажа с заданными характеристиками и классом.

        Args:
        strength (int): Сила персонажа.
        dexterity (int): Ловкость персонажа.
        constitution (int): Телосложение персонажа.
        wisdom (int): Мудрость персонажа.
        intelligence (int): Интеллект персонажа.
        charisma (int): Харизма персонажа.
        character_class (str): Класс персонажа ('warrior', 'mage', 'hunter').

        Raises:
        ValueError: Если передан недопустимый класс персонажа.
        """

        valid_classes: str = ['warrior', 'mage', 'hunter']
        if character_class not in valid_classes:
            raise ValueError(f"Недопустимый класс персонажа: {character_class}")
        
        self.character_class: str = character_class
        self.max_health: int = self.calculate_max_health()
        self.current_health: int = self.max_health
        self.damage: int = self.calculate_damage()
        self.defense: int = self.calculate_defense()
        self.max_mana: int = self.calculate_max_mana()
        self.mana: int = self.max_mana

    def calculate_max_health(self):
        """
        Рассчитывает максимальное здоровье персонажа.

        Формула: телосложение * 10 + сила / 2

        Returns:
        int: Максимальное здоровье персонажа.
        """
        return math.floor(self.constitution * 10 + self.strength / 2)

    def calculate_damage(self):
        """
        Рассчитывает базовый урон персонажа в зависимости от его класса.

        Формулы:
        Воин: сила * 2,2 + телосложение / 3
        Маг: интеллект * 2,5 + мудрость / 2
        Охотник: ловкость * 1,9 + сила / 3

        Returns:
        int: Базовый урон персонажа.
        """
        if self.character_class == 'warrior':
            return math.floor(self.strength * 2.2 + self.constitution / 3)
        elif self.character_class == 'mage':
            return math.floor(self.intelligence * 2.5 + self.wisdom / 2)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.9 + self.strength / 3)

    def calculate_defense(self):
        """
        Рассчитывает защиту персонажа в зависимости от его класса.

        Формулы:
        Воин: телосложение * 1,8 + сила / 4
        Маг: мудрость * 1,3 + интеллект / 6
        Охотник: ловкость * 1,6 + телосложение / 5

        Returns:
        int: Значение защиты персонажа.
        """
        if self.character_class == 'warrior':
            return math.floor(self.constitution * 1.8 + self.strength / 4)
        elif self.character_class == 'mage':
            return math.floor(self.wisdom * 1.3 + self.intelligence / 6)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.6 + self.constitution / 5)

    def calculate_max_mana(self):
        """
        Рассчитывает максимальное количество маны персонажа в зависимости от класса.

        Формулы:
        Воин: интеллект + сила / 2
        Маг: интеллект * 3 + мудрость
        Охотник: ловкость * 1,5 + мудрость / 2

        Returns:
        int: Максимальное количество маны.
        """
        if self.character_class == 'warrior':
            return math.floor(self.intelligence + self.strength / 2)
        elif self.character_class == 'mage':
            return math.floor(self.intelligence * 3 + self.wisdom)
        elif self.character_class == 'hunter':
            return math.floor(self.dexterity * 1.5 + self.wisdom / 2)