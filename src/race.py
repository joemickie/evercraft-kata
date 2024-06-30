# src/race.py

class Race:
    def __init__(self, name):
        self.name = name

    def apply_race_modifiers(self, character):
        pass

class Human(Race):
    def __init__(self):
        super().__init__("Human")

class Orc(Race):
    def __init__(self):
        super().__init__("Orc")

    def apply_race_modifiers(self, character):
        character.strength += 2
        character.intelligence -= 1
        character.wisdom -= 1
        character.charisma -= 1
        character.armor_class += 2

class Dwarf(Race):
    def __init__(self):
        super().__init__("Dwarf")

    def apply_race_modifiers(self, character):
        character.constitution += 1
        character.charisma -= 1

    def double_constitution_modifier(self, character):
        if character._modifier(character.constitution) > 0:
            return character._modifier(character.constitution) * 2
        return character._modifier(character.constitution)

class Elf(Race):
    def __init__(self):
        super().__init__("Elf")

    def apply_race_modifiers(self, character):
        character.dexterity += 1
        character.constitution -= 1

    def adjust_critical_range(self, roll):
        return roll >= 19

class Halfling(Race):
    def __init__(self):
        super().__init__("Halfling")

    def apply_race_modifiers(self, character):
        character.dexterity += 1
        character.strength -= 1
        character.armor_class += 2

    def check_alignment(self, alignment):
        return alignment != "Evil"
