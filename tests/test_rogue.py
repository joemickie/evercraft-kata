# tests/test_rogue.py

import pytest
from src.rogue import Rogue

def test_rogue_creation():
    with pytest.raises(ValueError):
        Rogue(name="Robin Hood", alignment="Good")

def test_rogue_attack_bonus():
    rogue = Rogue(name="Robin Hood", alignment="Neutral", dexterity=15)
    assert rogue.attack_bonus() == 2  # Dexterity modifier is +2

def test_rogue_critical_multiplier():
    rogue = Rogue(name="Robin Hood", alignment="Neutral")
    assert rogue.critical_multiplier() == 3  # Rogues do triple damage on critical hits

if __name__ == "__main__":
    pytest.main()
