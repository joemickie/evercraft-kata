# src/grid.py

class Cell:
    def __init__(self, terrain="normal"):
        self.terrain = terrain
        self.occupant = None

    def is_occupied(self):
        return self.occupant is not None

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.cells = [[Cell() for _ in range(width)] for _ in range(height)]

    def place_character(self, character, x, y):
        if 0 <= x < self.width and 0 <= y < self.height and not self.cells[y][x].is_occupied():
            self.cells[y][x].occupant = character
            character.position = (x, y)
            return True
        return False

    def move_character(self, character, new_x, new_y):
        x, y = character.position
        if 0 <= new_x < self.width and 0 <= new_y < self.height and not self.cells[new_y][new_x].is_occupied():
            self.cells[y][x].occupant = None
            self.cells[new_y][new_x].occupant = character
            character.position = (new_x, new_y)
            return True
        return False
