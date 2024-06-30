# src/monk.py

from src.character import Character

class Monk(Character):
    def base_hit_points(self):
        return 6

    def attack_bonus(self):
        return (self.level - 1) // 3 + (self.level - 1) // 2 + 1

    def attack(self, target, roll):
        attack_bonus = self.attack_bonus() + (self._modifier(self.strength) if self.level % 3 == 0 else self._modifier(self.dexterity))
        attack_roll = roll + attack_bonus
        if roll == 20 or attack_roll >= target.armor_class:
            damage = 3
            if roll == 20:
                damage *= 2
            target.hit_points -= damage
            self.gain_experience(10)
            return True
        return False

    def armor_class(self):
        return 10 + self._modifier(self.dexterity) + max(self._modifier(self.wisdom), 0)
