# tests/test_character.py

import pytest
from src.character import Character
from src.race import Human  # Import other races as needed
from src.equipment import Weapon, Armor, Item
from src.grid import Grid

def test_character_creation():
    char = Character(name="Aragorn", alignment="Good", race=Human())
    assert char.name == "Aragorn"
    assert char.alignment == "Good"

def test_default_armor_class_and_hit_points():
    char = Character(name="Aragorn", alignment="Good", race=Human())
    assert char.armor_class == 10
    assert char.hit_points == 5  # Constitution is 10, so modifier is 0, hit points should be 5.

def test_attack():
    char1 = Character(name="Aragorn", alignment="Good", strength=15, race=Human())
    char2 = Character(name="Orc", alignment="Evil", dexterity=8, race=Human())
    char1.attack(char2, roll=15)
    assert char2.hit_points == 2  # 5 - (1 + 2) = 2 (1 base + 2 strength modifier)

def test_critical_hit():
    char1 = Character(name="Aragorn", alignment="Good", strength=15, race=Human())
    char2 = Character(name="Orc", alignment="Evil", dexterity=8, race=Human())
    char1.attack(char2, roll=20)
    assert char2.hit_points == -1  # 5 - 6 = -1 (1 base + 2 strength modifier) * 2 = 6

def test_level_up():
    char1 = Character(name="Aragorn", alignment="Good", strength=15, race=Human())
    char2 = Character(name="Orc", alignment="Evil", dexterity=8, race=Human())
    for _ in range(100):
        char1.attack(char2, roll=15)
    assert char1.level == 2
    assert char1.hit_points == 10  # 5 + 5 (constitution modifier is 0)

def test_is_dead():
    char1 = Character(name="Aragorn", alignment="Good", strength=15, race=Human())
    char2 = Character(name="Orc", alignment="Evil", dexterity=8, race=Human())
    for _ in range(6):
        char1.attack(char2, roll=15)
    assert char2.is_dead()

def test_even_level_attack_bonus():
    char1 = Character(name="Aragorn", alignment="Good", strength=15, race=Human())
    char2 = Character(name="Orc", alignment="Evil", dexterity=8, race=Human())
    char1.experience_points = 1000  # Set to level 2
    char1.attack(char2, roll=14)  # Roll + strength modifier + 1 for even level 2
    assert char2.hit_points == 2  # 5 - (1 + 2 + 1) = 1 (1 base + 2 strength modifier + 1 level bonus)

def test_attack_bonus_for_multiple_even_levels():
    char1 = Character(name="Aragorn", alignment="Good", strength=15, race=Human())
    char2 = Character(name="Orc", alignment="Evil", dexterity=8, race=Human())
    char1.experience_points = 3000  # Set to level 4
    char1.attack(char2, roll=12)  # Roll + strength modifier + 2 for even level 4
    assert char2.hit_points == 2  # 5 - (1 + 2 + 2) = 0 (1 base + 2 strength modifier + 2 level bonus)

def test_character_movement_on_grid():
    grid = Grid(width=5, height=5)
    char = Character(name="Aragorn", alignment="Good")
    grid.place_character(char, 2, 2)
    assert char.position == (2, 2)
    moved = char.move_to(3, 3, grid)
    assert moved == True
    assert char.position == (3, 3)
    assert grid.cells[3][3].occupant == char
    assert grid.cells[2][2].occupant == None

if __name__ == "__main__":
    pytest.main()
