# src/fighter.py

from src.character import Character

class Fighter(Character):
    def base_hit_points(self):
        return 10

    def attack_bonus(self):
        return self.level

