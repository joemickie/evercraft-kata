# src/paladin.py

from src.character import Character
from src.race import Human

class Paladin(Character):
    def __init__(self, name, alignment, race=Human(), strength=10, dexterity=10, constitution=10, wisdom=10, intelligence=10, charisma=10):
        if alignment != "Good":
            raise ValueError("Paladins can only have Good alignment")
        super().__init__(name, alignment, race, strength, dexterity, constitution, wisdom, intelligence, charisma)

    def base_hit_points(self):
        return 8

    def attack_bonus(self):
        return self.level

    def attack(self, target, roll):
        attack_bonus = self.attack_bonus() + self._modifier(self.strength)
        if target.alignment == "Evil":
            attack_bonus += 2
        attack_roll = roll + attack_bonus
        if roll == 20 or attack_roll >= target.armor_class:
            damage = 1 + self._modifier(self.strength)
            if target.alignment == "Evil":
                damage += 2
            if roll == 20:
                damage *= 3 if target.alignment == "Evil" else 2
            target.hit_points -= damage
            self.gain_experience(10)
            return True
        return False
