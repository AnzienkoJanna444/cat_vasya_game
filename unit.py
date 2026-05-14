from abc import ABC, abstractmethod
import math


class Unit(ABC):
    def __init__(self, strength: int, dexterity: int, constitution: int, wisdom: int, intelligence: int, charisma: int):
        """
    Инициализирует базового юнита с шестью характеристиками.
    
    Args:
    strength (int): Сила юнита.
    dexterity (int): Ловкость юнита.
    constitution (int): Телосложение юнита.
    wisdom (int): Мудрость юнита.
    intelligence (int): Интеллект юнита.
    charisma (int): Харизма юнита.
    """
        self.strength: int = strength
        self.dexterity: int = dexterity
        self.constitution: int = constitution
        self.wisdom: int = wisdom
        self.intelligence: int = intelligence
        self.charisma: int = charisma
        self.spells: int = []
        self.mana: int = 0
    @abstractmethod
    def calculate_max_health(self):
        """
        Абстрактный метод для расчёта максимального здоровья юнита.

        Returns:
        int: Максимальное здоровье юнита.
        """
        pass

    @abstractmethod
    def calculate_damage(self):
        """
        Абстрактный метод для расчёта базового урона юнита.

        Returns:
        int: Базовый урон юнита.
        """
        pass

    @abstractmethod
    def calculate_defense(self):
        """
        Абстрактный метод для расчёта защиты юнита.

        Returns:
        int: Значение защиты юнита.
        """
        pass

    @abstractmethod
    def calculate_max_mana(self):
        """
        Абстрактный метод для расчёта максимальной маны юнита.

        Returns:
        int: Максимальное количество маны юнита.
        """
        pass

    def add_spell(self, spell):
        """
        Добавляет заклинание в список заклинаний юнита.

        Args:
        spell (Spell): Объект заклинания для добавления.
        """
        self.spells.append(spell)

    def cast_spell(self, index):
        """
        Применяет заклинание по указанному индексу.

        Проверяет, достаточно ли у юнита маны для использования заклинания.
        Если достаточно — вычитает стоимость и возвращает урон заклинания.
        Если недостаточно — выбрасывает исключение.

        Args:
        index (int): Индекс заклинания в списке spells.

        Returns:
        int: Урон от применённого заклинания.

        Raises:
        IndexError: Если индекс выходит за пределы списка заклинаний.
        ValueError: Если у юнита недостаточно маны для заклинания.
        """
        if not (0 <= index < len(self.spells)):
            raise IndexError("Некорректный индекс заклинания")
        
        spell = self.spells[index]
        
        if self.mana >= spell.mana_cost:
            self.mana -= spell.mana_cost
            return spell.cast()
        else:
            raise ValueError(f"Недостаточно маны: нужно {spell.mana_cost}, доступно {self.mana}")