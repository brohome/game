import random
import unit
from typing import List

class GameMap:
    def __init__(self, size: int, players: List[unit.Unit]):
        self.size = size
        self.players = players
        self.terrain_map = self._generate_map()
        self._place_players()

    def _generate_map(self) -> List[List[str]]:
        terrain_types = ['Равнина', 'Пусто', 'Гора']
        weights = [0.2, 0.7, 0.1]
        return [[random.choices(terrain_types, weights=weights)[0] for _ in range(self.size)]
                for _ in range(self.size)]

    def _place_players(self):
        count = 0
        for i in range(self.size):
            for j in range(self.size):
                if self.terrain_map[i][j] == 'Пусто' and count < len(self.players):
                    self.terrain_map[i][j] = self.players[count].name
                    self.players[count].position = (i, j)
                    count += 1

        if count < len(self.players):
            print(f"Не удалось разместить {len(self.players) - count} игрок(ов) — не хватает 'Пусто' клеток.")

    def display(self):
        for row in self.terrain_map:
            print('\t'.join(str(cell) for cell in row))