from character import Character
from monster import Monster
from spells import Fireball, IceLance, LightningBolt

warrior = Character(18, 12, 16, 8, 10, 12, 'warrior')
mage = Character(10, 14, 12, 18, 20, 16, 'mage')
hunter = Character(14, 18, 14, 12, 12, 14, 'hunter')
dragon = Monster(12, 10, 12, 6, 6, 6)

fire = Fireball()
ice = IceLance()
light = LightningBolt()

warrior.add_spell(fire)
warrior.add_spell(ice)
mage.add_spell(fire)
mage.add_spell(light)

print(f"Воин: HP={warrior.current_health}/{warrior.max_health}, Мана={warrior.mana}/{warrior.max_mana}, Урон={warrior.damage}, Защита={warrior.defense}")
print(f"Маг: HP={mage.current_health}/{mage.max_health}, Мана={mage.mana}/{mage.max_mana}, Урон={mage.damage}, Защита={mage.defense}")
print(f"Охотник: HP={hunter.current_health}/{hunter.max_health}, Мана={hunter.mana}/{hunter.max_mana}, Урон={hunter.damage}, Защита={hunter.defense}")
print(f"Дракон: HP={goblin.current_health}/{goblin.max_health}, Урон={goblin.damage}, Защита={goblin.defense}")

print("\n--- Воин колдует ---")
try:
    damage = warrior.cast_spell(0)
    print(f"Воин применил {warrior.spells[0].name}, урон {damage}. Осталось маны: {warrior.mana}")
except Exception as e:
    print(e)

print("\n--- Маг колдует ---")
damage = mage.cast_spell(1)
print(f"Маг применил {mage.spells[1].name}, урон {damage}. Осталось маны: {mage.mana}")

print("\n--- Попытка колдовать без маны ---")
try:
    damage = warrior.cast_spell(1)
    warrior.cast_spell(0)
except Exception as e:
    print(e)