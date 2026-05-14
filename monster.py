import math
from unit import Unit

class Monster(Unit):
    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int, intelligence: int, charisma: int):
        super().__init__(strength, dexterity, constitution, wisdom, intelligence, charisma)
        """
        Инициализирует монстра с заданными характеристиками.

        Args:
        strength (int): Сила монстра.
        dexterity (int): Ловкость монстра.
        constitution (int): Телосложение монстра.
        wisdom (int): Мудрость монстра.
        intelligence (int): Интеллект монстра.
        charisma (int): Харизма монстра.
        """
        self.max_health: int = self.calculate_max_health()
        self.current_health: int = self.max_health
        self.damage: int = self.calculate_damage()
        self.defense: int = self.calculate_defense()

    def calculate_max_health(self):
        """
        Рассчитывает максимальное здоровье монстра.

        Формула: телосложение * 8 + сила / 3

        Returns:
        int: Максимальное здоровье монстра.
        """
        return math.floor(self.constitution * 8 + self.strength / 3)

    def calculate_damage(self):
        """
        Рассчитывает базовый урон монстра.

        Формула: сила * 2 + телосложение / 5

        Returns:
        int: Базовый урон монстра.
        """
        return math.floor(self.strength * 2 + self.constitution / 5)

    def calculate_defense(self):
        """
        Рассчитывает защиту монстра.

        Формула: телосложение * 1,2 + сила / 5

        Returns:
        int: Значение защиты монстра.
        """
        return math.floor(self.constitution * 1.2 + self.strength / 5)

    def calculate_max_mana(self):
        """
        Рассчитывает максимальное количество маны монстра.

        Монстры не используют магию, поэтому всегда возвращает 0.

        Returns:
        int: Всегда 0.
        """
        return 0