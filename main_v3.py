def init_cells(cells_string):
    cells_list = []
    a, b = 0, 3
    for i in range(3):
        cells_list.append(list(cells_string[a:b]))
        a += 3
        b += 3
    return cells_list

def print_field(cells_list):
    print('---------')
    for i in range(3):
        print('| ', end='')
        for j in range(3):
            print(cells_list[i][j], '', end='')
        print('|')
    print('---------')

def check_from1to3(number):
    one_two_three = [1, 2, 3]
    if number in one_two_three:
        return True
    return False

def coordinates_is_numeric(coordinates):
    """
    coordinates: list[x, y]
    """
    return coordinates[0].isnumeric() and coordinates[1].isnumeric()

def check_coordinates():
    while True:
        coordinates_string_list = input().split(' ')
        if (coordinates_is_numeric(coordinates_string_list)):
            x = int(coordinates_string_list[0])
            y = int(coordinates_string_list[1])
        else:
            print("You should enter numbers!")
            continue
        if check_from1to3(x) and check_from1to3(y):
            i, j = 3 - y, x - 1
            if cells_list[i][j] != ' ':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                global move_number
                if (move_number % 2) == 1:
                    cells_list[i][j] = 'X'
                else:
                    cells_list[i][j] = 'O'
                move_number += 1
                break
        else:
            print("Coordinates should be from 1 to 3!")
            continue

def check_game_state(cells_list):
    # Часть полей (1. и 3.) создавалась для расчета результата игры при 
    # условии, что изначально вводится непустое поле для игры cells_string

    # 1. Расчет количества X и О (проверка невозможного исхода, когда
    # разница в количестве больше, чем 1):

    global move_number
    if move_number < 5: return True

    total_x, total_o, total_ = 0, 0, 0
    for i in range(3):
        for j in range(3):
            if cells_list[i][j] == 'X':
                total_x += 1
            if cells_list[i][j] == 'O':
                total_o += 1
            if cells_list[i][j] == ' ':
                total_ += 1
    if abs(total_o - total_x) > 1:
        print('Impossible')
        return

    # 2. Определение победителя:
    # 2.1 побеждает диагональ
    if (
        cells_list[1][1] != ' ' and 
        cells_list[0][0] == cells_list[1][1] == cells_list[2][2] or 
        cells_list[0][2] == cells_list[1][1] == cells_list[2][0]
    ):
        print(f"{cells_list[1][1]} wins")
        return False

    # 2.2 побеждает строка
    count = 0
    for i in range(3):
        if (
            cells_list[i][0] != ' ' and
            cells_list[i][0] == cells_list[i][1] == cells_list[i][2]
        ):
            count += 1
            winner = cells_list[i][0]
            print(f"{winner} wins")
            return False
    for j in range(3):
        if (
            cells_list[0][j] != ' ' and
            cells_list[0][j] == cells_list[1][j] == cells_list[2][j]
        ):
            count += 1
            winner = cells_list[0][j]
            print(f"{winner} wins")
            return False

    # 3. Невозможный исход, когда побеждают сразу оба; ничья; продолжение игры
    if count > 1:
        print('Impossible')
        return
    elif count == 1:
        print(f"{winner} wins")
    else:
        if total_ == 0 and count == 0:
            print('Draw')
        else:
            # print('Game not finished')
            return True

print('''
Suppose the bottom left cell on the board has the coordinates (1, 1) and the 
top right cell has the coordinates (3, 3) like in this table:
--------------------
(1 3) (2 3) (3 3)
(1 2) (2 2) (3 2)
(1 1) (2 1) (3 1)
-------------------- 
Make your first X-move!''')

cells_list = init_cells('         ')
move_number = 1

while check_game_state(cells_list):
    print('Enter coordinates: ')
    check_coordinates()
    print_field(cells_list)