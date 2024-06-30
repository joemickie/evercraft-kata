# src/rogue.py

from src.character import Character
from src.race import Human

class Rogue(Character):
    def __init__(self, name, alignment, race=Human(), strength=10, dexterity=10, constitution=10, wisdom=10, intelligence=10, charisma=10):
        if alignment == "Good":
            raise ValueError("Rogues cannot have Good alignment")
        super().__init__(name, alignment, race, strength, dexterity, constitution, wisdom, intelligence, charisma)

    def critical_multiplier(self):
        return 3

    def attack_bonus(self):
        return self._modifier(self.dexterity)

    def attack(self, target, roll):
        original_dex_mod = target._modifier(target.dexterity)
        if target._modifier(target.dexterity) > 0:
            target.armor_class -= original_dex_mod
        result = super().attack(target, roll)
        target.armor_class += original_dex_mod
        return result
