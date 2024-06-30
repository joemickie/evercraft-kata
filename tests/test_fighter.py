# tests/test_fighter.py

import pytest
from src.fighter import Fighter

def test_fighter_hit_points():
    fighter = Fighter(name="Conan", alignment="Neutral")
    assert fighter.hit_points == 10  # Constitution is 10, so modifier is 0, hit points should be 10.

def test_fighter_attack_bonus():
    fighter = Fighter(name="Conan", alignment="Neutral")
    assert fighter.attack_bonus() == 1  # Level 1 fighter gets +1 attack bonus
    fighter.gain_experience(1000)
    assert fighter.attack_bonus() == 2  # Level 2 fighter gets +2 attack bonus

if __name__ == "__main__":
    pytest.main()
