import unit
import random

class Archer(unit.Unit):
    def __init__(self, name, position=None):
        super().__init__(name=name, hp=60, attack=20, position=position, moves_left=2)
        self.unit_type = "Archer"


class Warrior(unit.Unit):
    def __init__(self, name, position=None):
        super().__init__(name=name, hp=100, attack=30, position=position, moves_left=2)
        self.unit_type = "Warrior"


class Healer(unit.Unit):
    def __init__(self, name, position=None):
        super().__init__(name=name, hp=70, attack=0, position=position, moves_left=2)
        self.unit_type = "Healer"

    def attack(self, target):
        # Healer не атакует, а лечит союзника
        if self._in_range(target) and target.team == self.team:
            healed = 25
            target.hp = min(target.max_hp, target.hp + healed)
            print(f"{self.name} (Healer) лечит {target.name} на {healed} HP.")
        else:
            print(f"{target.name} вне зоны лечения или не союзник.")


class Mage(unit.Unit):
    def __init__(self, name, position=None):
        super().__init__(name=name, hp=50, attack=40, position=position, moves_left=2)
        self.unit_type = "Mage"
        self.mana = 100
    