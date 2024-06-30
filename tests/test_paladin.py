# tests/test_paladin.py

import pytest
from src.paladin import Paladin

def test_paladin_creation():
    with pytest.raises(ValueError):
        Paladin(name="Arthur", alignment="Neutral")

def test_paladin_hit_points():
    paladin = Paladin(name="Arthur", alignment="Good")
    assert paladin.hit_points == 8  # Constitution is 10, so modifier is 0, hit points should be 8.

def test_paladin_attack_bonus():
    paladin = Paladin(name="Arthur", alignment="Good")
    assert paladin.attack_bonus() == 1  # Level 1 paladin gets +1 attack bonus
    paladin.gain_experience(1000)
    assert paladin.attack_bonus() == 2  # Level 2 paladin gets +2 attack bonus

if __name__ == "__main__":
    pytest.main()
