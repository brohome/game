import gamemap as gm
import functions as f

class GameEngine:
    def __init__(self):
        self._players = f.get_players()
        self._gamemap = gm.GameMap(15, self._players)


    def _get_around_player(self, player):
        pos = player.position
        print("\nЧто видит персонаж:\n")

        print(f"{self._gamemap.terrain_map[pos[0] - 1][pos[1] - 1]}  {self._gamemap.terrain_map[pos[0] - 1][pos[1]]}  {self._gamemap.terrain_map[pos[0] - 1][pos[1] + 1]}")

        print(f"{self._gamemap.terrain_map[pos[0]][pos[1] - 1]}  {self._gamemap.terrain_map[pos[0]][pos[1]]}  {self._gamemap.terrain_map[pos[0]][pos[1] + 1]}")

        print(f"{self._gamemap.terrain_map[pos[0] + 1][pos[1] - 1]}  {self._gamemap.terrain_map[pos[0] + 1][pos[1]]}  {self._gamemap.terrain_map[pos[0] + 1][pos[1] + 1]}\n")

    def game(self,):
        def menu():
            player_num = f.choose_player(self._players)
            input("Нажмите любую клавишу чтобы увидет что вокруг")
            self._get_around_player(self._players[player_num])
            

        while True:
            for i in self._players:
                total_moves += i.moves_left

            if total_moves == 0:
                break
            
            print("Выберите одно из предложенных действий:\n")
            print("1. Посмотреть карту\n" \
            "2. Выбрать игрока и начать ход\n")
            num = int(input("Введите число: "))

            if num == 1:
                self._gamemap.display()
            elif num == 2:
                menu()

    



if __name__ == '__main__':
    gmd = GameEngine()
    gmd.game()