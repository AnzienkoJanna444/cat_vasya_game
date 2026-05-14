from abc import ABC, abstractmethod

class Spell(ABC):
    def __init__(self, name: str, damage: int, mana_cost: int):
        """
        Инициализирует заклинание с заданными параметрами.

        Args:
        name (str): Название заклинания.
        damage (int): Урон заклинания.
        mana_cost (int): Стоимость заклинания в мане.
        """
        self.name: str = name
        self.damage: int = damage
        self.mana_cost: int = mana_cost

    @abstractmethod
    def cast(self):
        """
        Применяет заклинание и возвращает его эффект.

        Returns:
        int: Урон, наносимый заклинанием.
        """
        pass

class Fireball(Spell):
    def __init__(self):
        """
        Инициализирует заклинание "Огненный шар" с уроном 35 и стоимостью 15 маны.
        """
        super().__init__("Огненный шар", 35, 15)

    def cast(self):
        """
        Применяет заклинание "Огненный шар".

        Returns:
            int: Урон 35.
        """
        return self.damage

class IceLance(Spell):
    def __init__(self):
        """
        Инициализирует заклинание "Ледяное копьё" с уроном 25 и стоимостью 10 маны.
        """
        super().__init__("Ледяное копье", 25, 10)

    def cast(self):
        """
        Применяет заклинание "Ледяное копьё".

        Returns:
        int: Урон 25.
        """
        return self.damage

class LightningBolt(Spell):
    def __init__(self):
        """
        Инициализирует заклинание "Разряд молнии" с уроном 40 и стоимостью 20 маны.
        """
        super().__init__("Разряд молнии", 40, 20)

    def cast(self):
        """
        Применяет заклинание "Разряд молнии".

        Returns:
        int: Урон 40.
        """
        return self.damage