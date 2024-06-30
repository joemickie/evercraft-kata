# src/equipment.py

class Weapon:
    def __init__(self, name, damage, attack_bonus=0, special_properties=None):
        self.name = name
        self.damage = damage
        self.attack_bonus = attack_bonus
        self.special_properties = special_properties or {}

    def __repr__(self):
        return f"{self.name} (Damage: {self.damage}, Attack Bonus: {self.attack_bonus})"

class Armor:
    def __init__(self, name, armor_class_bonus, damage_reduction=0):
        self.name = name
        self.armor_class_bonus = armor_class_bonus
        self.damage_reduction = damage_reduction

    def __repr__(self):
        return f"{self.name} (AC Bonus: {self.armor_class_bonus}, DR: {self.damage_reduction})"

class Item:
    def __init__(self, name, properties=None):
        self.name = name
        self.properties = properties or {}

    def __repr__(self):
        return self.name
