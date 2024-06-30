# tests/test_race.py

import pytest
from src.character import Character
from src.race import Human, Orc, Dwarf, Elf, Halfling

def test_human_race():
    char = Character(name="Aragorn", alignment="Good", race=Human())
    assert char.strength == 10  # Default value
    assert char.dexterity == 10  # Default value

def test_orc_race_modifiers():
    char = Character(name="Grishnak", alignment="Evil", race=Orc(), strength=10, intelligence=10, wisdom=10, charisma=10)
    assert char.strength == 12
    assert char.intelligence == 9
    assert char.wisdom == 9
    assert char.charisma == 9
    assert char.armor_class == 12

def test_dwarf_race_modifiers():
    char = Character(name="Gimli", alignment="Good", race=Dwarf(), constitution=10, charisma=10)
    assert char.constitution == 11
    assert char.charisma == 9

def test_elf_race_modifiers():
    char = Character(name="Legolas", alignment="Good", race=Elf(), dexterity=10, constitution=10)
    assert char.dexterity == 11
    assert char.constitution == 9

def test_halfling_race_modifiers():
    char = Character(name="Frodo", alignment="Good", race=Halfling(), dexterity=10, strength=10)
    assert char.dexterity == 11
    assert char.strength == 9
    assert char.armor_class == 12

if __name__ == "__main__":
    pytest.main()
