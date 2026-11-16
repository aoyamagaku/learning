class Character:
    def __init__(self, *, level: int) -> None:
        self.level = level
        self.health_points = self.base_health_points * level
        self.attack_power = self.base_attack_power * level

    def attack(self, *, target: "Character") -> None:
        print(f"{self.character_name} attacks {target.character_name} Health: "
              f"{target.health_points} with "
              f"{self.attack_power} power")
        target.health_points -= self.attack_power
        print(f"After attack {target.character_name} has hp {target.health_points}")

    def is_alive(self) -> bool:
        return self.health_points > 0

    def __str__(self) -> str:
        return f"{self.character_name} level: {self.level} HP: {self.health_points}"


class Ork(Character):
    base_health_points = 150
    base_attack_power = 10
    character_name = "Ork"

class Elf(Character):
    base_health_points = 60
    base_attack_power = 30
    character_name = "Elf"


def fight(*, character_1: Character, character_2: Character) -> None:
    while character_1.is_alive() and character_2.is_alive():
        character_1.attack(target=character_2)
        if character_2.is_alive():
            character_2.attack(target=character_1)

    print(f"Character 1: {character_1} is alive {character_1.is_alive()}")
    print(f"Character 1: {character_2} is alive {character_2.is_alive()}")

ork = Ork(level=1)
elf = Elf(level=1)

fight(character_1=ork, character_2=elf)