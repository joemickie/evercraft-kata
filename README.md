```markdown
# EverCraft-Kata

EverCraft-Kata is a simple role-playing game implementation in Python. It includes various character classes such as Fighters, Rogues, Monks, and Paladins, each with unique abilities and features. The game supports character creation, alignment, combat, leveling, races, and equipment, as well as a grid-based battle map for the Bonus Iteration.

## Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/joemickie/evercraft-kata.git
   ```
2. Navigate to the project directory:
   ```sh
   cd evercraft-kata
   ```
3. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   # On Linux or Mac, use
   source venv/bin/activate
   # On Windows, use
   venv\Scripts\activate
   ```
4. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Features

### Iteration 1 - Core

- **Create a Character**: Characters can be created with a name and alignment (Good, Evil, Neutral).
- **Armor Class & Hit Points**: Characters have an Armor Class (default 10) and Hit Points (default 5).
- **Character Can Attack**: Characters can attack others using a 20-sided die roll.
- **Character Can Be Damaged**: Successful attacks deal 1 point of damage, and critical hits deal double damage.
- **Character Has Abilities Scores**: Characters have Strength, Dexterity, Constitution, Wisdom, Intelligence, and Charisma scores ranging from 1 to 20.
- **Character Ability Modifiers Modify Attributes**: Ability scores modify attack rolls, damage, Armor Class, and Hit Points.
- **A Character can gain experience when attacking**: Characters gain 10 experience points for successful attacks.
- **A Character Can Level**: Characters level up every 1000 experience points, gaining additional Hit Points and attack bonuses.

### Iteration 2 - Classes

- **Characters Have Classes**: Characters can belong to different classes such as Fighter, Rogue, Monk, and Paladin, each with unique abilities and features.
  - **Fighter**: Increased attack rolls and Hit Points per level.
  - **Rogue**: Triple damage on critical hits, ignores opponent's Dexterity modifier for Armor Class, and adds Dexterity modifier to attacks.
  - **Monk**: Increased damage, adds Wisdom modifier to Armor Class, and has a unique attack progression.
  - **Paladin**: Bonus attack and damage against Evil characters, triple damage on critical hits against Evil characters, and increased Hit Points per level.

### Iteration 3 - Races

- **Characters Have Races**: Characters can belong to different races such as Human, Orc, Dwarf, Elf, and Halfling, each with unique modifiers and abilities.
  - **Orc**: Increased Strength, decreased Intelligence, Wisdom, and Charisma, and additional Armor Class.
  - **Dwarf**: Increased Constitution, decreased Charisma, double Constitution modifier to Hit Points, and bonus attack/damage against Orcs.
  - **Elf**: Increased Dexterity, decreased Constitution, expanded critical range, and additional Armor Class against Orcs.
  - **Halfling**: Increased Dexterity, decreased Strength, additional Armor Class against non-Halflings, and cannot have Evil alignment.

### Iteration 4 - Weapons, Armor & Items

- **Weapons**: Characters can wield a single weapon to enhance their combat capabilities.
  - Basic weapons that improve damage (e.g., dagger, longsword).
  - Magic weapons with special properties (e.g., +2 waraxe, elven longsword).
- **Armor**: Characters can wear one suit of armor and carry one shield to improve their Armor Class.
  - Basic armor that improves Armor Class (e.g., leather armor, plate armor).
  - Magic armor with special properties (e.g., elven chain mail).
- **Items**: Characters can carry multiple items that enhance their capabilities.
  - Items that improve combat or abilities (e.g., ring of protection, belt of giant strength, amulet of the heavens).

### Bonus Iteration - Battle Grid

- **Battle Grid**: Multiple characters can be on a grid-based map with terrain that impacts movement and combat.
  - Characters can move on the grid.
  - Weapons have ranges that affect combat.

## Running Tests

To run the tests, use the following command:
```sh
pytest
```

## License

This project is licensed under the MIT License.
```

This README file reflects all the completed features of the EverCraft-Kata project, including the Bonus Iteration - Battle Grid.