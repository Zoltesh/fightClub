from CharacterStuff.Character import *
import os


def readInCharacters(characterList):

    f = open(os.path.abspath("CharacterStuff/CharacterList.txt"), "r")

    for line in f:

        if line == "\n":
            continue

        if "ID" in line:
            character_id = int(line.removeprefix("ID: "))
            continue

        if "Name" in line:
            character_name = str(line.removeprefix("Name: "))
            character_name = character_name.removesuffix("\n")
            continue

        if "Level" in line:
            character_level = int(line.removeprefix("Level: "))
            continue

        if "HP" in line:
            character_hp = int(line.removeprefix("HP: "))
            continue

        if "Attack" in line:
            character_attack = int(line.removeprefix("Attack: "))
            continue

        if "Defense" in line:
            character_defense = int(line.removeprefix("Defense: "))
            continue

        if "Agility" in line:
            character_agility = int(line.removeprefix("Agility: "))
            continue

        if "Guard" in line:
            character_guard = int(line.removeprefix("Guard: "))

        try:

            characterList.append(Character(character_id, character_name, character_level, character_hp, character_attack,
                                           character_defense, character_agility, character_guard))

        except Exception as e:

            print(e)

    f.close()