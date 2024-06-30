# tests/test_monk.py

import pytest
from src.monk import Monk

def test_monk_hit_points():
    monk = Monk(name="Bruce Lee", alignment="Lawful")
    assert monk.hit_points == 6  # Constitution is 10, so modifier is 0, hit points should be 6.

def test_monk_attack_bonus():
    monk = Monk(name="Bruce Lee", alignment="Lawful")
    assert monk.attack_bonus() == 1  # Level 1 monk gets +1 attack bonus
    monk.gain_experience(3000)
    assert monk.attack_bonus() == 3  # Level 4 monk gets +3 attack bonus

if __name__ == "__main__":
    pytest.main()
