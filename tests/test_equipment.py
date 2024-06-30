# tests/test_equipment.py

import pytest
from src.character import Character
from src.equipment import Weapon, Armor, Item

def test_character_equip_weapon():
    character = Character(name="Hero", alignment="Good")
    sword = Weapon(name="Longsword", damage=5)
    character.equip_weapon(sword)
    assert character.weapon == sword

def test_character_equip_armor():
    character = Character(name="Hero", alignment="Good")
    leather_armor = Armor(name="Leather Armor", armor_class_bonus=2)
    character.equip_armor(leather_armor)
    assert character.armor == leather_armor
    assert character.armor_class == 12

def test_character_add_item():
    character = Character(name="Hero", alignment="Good")
    ring = Item(name="Ring of Protection", properties={"armor_class": 2})
    character.add_item(ring)
    assert ring in character.items
