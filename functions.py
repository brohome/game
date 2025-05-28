import characters as c

def get_players() -> list:
    print("Сейчас вам предстоит выбрать персонажа, выбирайте с умом.")
    count = 0
    d = {1: c.Mage, 2: c.Warrior, 3: c.Archer, 4: c.Healer}
    result = []

    while count < 3:
        print("Выберите за какого персонажа вы будете играть:\n" \
        "1. Маг\n" \
        "2. Защитник\n" \
        "3. Атакующий\n"
        "4. Лекарь\n")

        character = int(input("Введите число: "))
        if character not in (1, 2, 3, 4):
            continue

        result.append(d[character](name=input("Дайте имя своему персонажу: ")))
        count += 1


    return result


def choose_player(players: list):
    print(f"\nВыберите персонажа за которого будете ходить\n")

    for ind, i in enumerate(players, start=0):
        print(f"{ind}. Тип: {i.unit_type} Имя: {i.name}")
                
    num = int(input("Введите число: "))

    players[num].__str__()
    return num
