from abc import ABC, abstractmethod

class Unit(ABC):
    @abstractmethod
    def __init__(self, hp: int, name: str, attack: int, position, moves_left: int):
        self.hp = hp
        self.name = name
        self.attack = attack
        self.position = position
        self.moves_left = moves_left
        self.unit_type = None

    def move(self, x, y):
        if x > self.position + self.moves_left or y > self.position + self.moves_left:
            return 'Error'
        count_moves = abs(self.position[0] - x) + abs(self.position[1] - y)
        if self.moves_left < count_moves:
            return 'Error'
        
        self.position = (x, y)

    def take_damage(self, damage):
        self.hp -= damage

    def is_alive(self):
        if self.hp < 0:
            return False
        return True

    def _in_range(self):
        pass

    def get_attack(self, target):
        if self._in_range(target):
            damage = self.attack_power
            target.take_damage(damage)
            print(f"{self.name} (Warrior) атакует {target.name} и наносит {damage} урона.")
        else:
            print(f"{target.name} вне зоны досягаемости для {self.name}.")

    def __str__(self,):
        print(f'\nПоказатели персонажа {self.unit_type}:{self.name} :\n\n' \
        f'\tЗдоровье: {self.hp}\n' \
        f'\tАтака: {self.attack}\n' \
        f'\tПозиция: {self.position}\n' \
        f'\nШагов на этот ход осталось: {self.moves_left}\n')