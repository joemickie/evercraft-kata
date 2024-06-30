# src/character.py

from src.race import Human
from src.equipment import Weapon, Armor, Item

class Character:
    def __init__(self, name, alignment, race=Human(), strength=10, dexterity=10, constitution=10, wisdom=10, intelligence=10, charisma=10):
        self.name = name
        self.alignment = alignment
        self.race = race
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.wisdom = wisdom
        self.intelligence = intelligence
        self.charisma = charisma
        self.weapon = None
        self.armor = None
        self.items = []
        self.position = None  # New attribute for grid position
        self.armor_class = 10 + self._modifier(dexterity)
        self.hit_points = max(self.base_hit_points() + self._modifier(constitution), 1)  # Ensure at least 1 HP
        self.experience_points = 0
        self.level = 1
    
        # Apply race modifiers
        self.race.apply_race_modifiers(self)

    def base_hit_points(self):
        return 5

    def _modifier(self, score):
        return (score - 10) // 2

    def equip_weapon(self, weapon):
        self.weapon = weapon

    def equip_armor(self, armor):
        self.armor = armor
        self.armor_class += armor.armor_class_bonus

    def add_item(self, item):
        self.items.append(item)

    def attack(self, target, roll):
        attack_bonus = self.attack_bonus() + self._modifier(self.strength)
        if self.weapon:
            attack_bonus += self.weapon.attack_bonus
        attack_roll = roll + attack_bonus
        if roll == 20 or attack_roll >= target.armor_class:
            damage = 1 + self._modifier(self.strength)
            if self.weapon:
                damage += self.weapon.damage
            if roll == 20:
                damage *= self.critical_multiplier()
            damage = max(damage - (target.armor.damage_reduction if target.armor else 0), 1)
            target.hit_points -= damage
            self.gain_experience(10)
            return True
        return False

    def attack_bonus(self):
        return self.level // 2

    def critical_multiplier(self):
        return 2

    def gain_experience(self, points):
        self.experience_points += points
        while self.experience_points >= 1000 * self.level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.hit_points += max(self.base_hit_points() + self._modifier(self.constitution), 1)

    def is_dead(self):
        return self.hit_points <= 0

    def move_to(self, new_x, new_y, grid):
        if grid.move_character(self, new_x, new_y):
            self.position = (new_x, new_y)
            return True
        return False
