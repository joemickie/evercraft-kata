# tests/test_grid.py

import pytest
from src.character import Character
from src.grid import Grid

def test_place_character_on_grid():
    grid = Grid(width=5, height=5)
    character = Character(name="Hero", alignment="Good")
    assert grid.place_character(character, 2, 2) == True
    assert character.position == (2, 2)
    assert grid.cells[2][2].occupant == character

def test_move_character_on_grid():
    grid = Grid(width=5, height=5)
    character = Character(name="Hero", alignment="Good")
    grid.place_character(character, 2, 2)
    assert grid.move_character(character, 3, 3) == True
    assert character.position == (3, 3)
    assert grid.cells[3][3].occupant == character
    assert grid.cells[2][2].occupant == None
