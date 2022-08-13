a = "         "
wins = 0
counter = 0
count_x = 0
count_O = 0
counter_of = 0
number_of_moves = 1
diagonally_list = []
line_1 = []
line_2 = []
line_3 = []


def fight_place(baza):
    print('---------')
    print('|', baza[0], baza[1], baza[2], '|')
    print('|', baza[3], baza[4], baza[5], '|')
    print('|', baza[6], baza[7], baza[8], '|')
    print('---------')


def win_check(new_list1):
    counter1 = 0
    count_o1 = 0
    count_x1 = 0
    diagonally_list1 = []
    wins1 = 0
    for i1 in range(0, 10, 2):
        diagonally_list1.append(new_list1[i1])

    # for diagonals
    if (diagonally_list1[0] == diagonally_list1[2] == diagonally_list1[4] == "X") \
            or (diagonally_list1[1] == diagonally_list1[2] == diagonally_list1[3] == "X"):
        wins1 += 1
        print("X wins")
        return True
    elif (diagonally_list1[0] == diagonally_list1[2] == diagonally_list1[4] == "O") \
            or (diagonally_list1[1] == diagonally_list1[2] == diagonally_list1[3] == "O"):
        wins1 += 1
        print("O wins")
        return True

    # for rows
    for i1 in range(0, 7, 3):
        if new_list1[i1] == new_list1[i1 + 1] == new_list1[i1 + 2] == "X":
            wins1 += 1
            print("X wins")
            return True
        elif new_list1[i1] == new_list1[i1 + 1] == new_list1[i1 + 2] == "O":
            wins1 += 1
            print("O wins")
            return True
    for i1 in range(3):
        if new_list1[i1] == new_list1[i1 + 3] == new_list1[i1 + 6] == "X":
            wins1 += 1
            print("X wins")
            return True
        elif new_list1[i1] == new_list1[i1 + 3] == new_list1[i1 + 6] == "O":
            wins1 += 1
            print("O wins")
            return True
    for i1 in range(9):
        if new_list1[i1] == " ":
            counter1 += 1
    for i1 in range(9):
        if new_list1[i1] == "X":
            count_x1 += 1
        elif new_list1[i1] == "O":
            count_o1 += 1
    if wins1 == 0 and counter1 == 0:
        print("Draw")
        return True
    elif wins1 > 1 or (abs(count_x1 - count_o1) >= 2):
        print("Impossible")
        return True


fight_place(a)
new_list = [x for x in a]
for i in range(3):
    line_1.append(new_list[i])
    line_2.append(new_list[i + 3])
    line_3.append(new_list[i + 6])
# game
while True:
    b = input()
    cords = b.split()
    coordinates_x = int(cords[0])
    coordinates_y = int(cords[1])
    if (3 >= coordinates_y >= 1) and (3 >= coordinates_x >= 1):
        if coordinates_x == 1:
            if new_list[coordinates_y - 1] == " ":
                if number_of_moves % 2 == 1:
                    new_list[coordinates_y - 1] = "X"
                elif number_of_moves % 2 == 0:
                    new_list[coordinates_y - 1] = "O"
                fight_place(new_list)
                counter_of += 1
                number_of_moves += 1
                win_check(new_list)
                if win_check(new_list):
                    break
                else:
                    continue
            elif new_list[coordinates_y - 1] == "X" or new_list[coordinates_y - 1] == "O":
                print("This cell is occupied! Choose another one!")
                continue
        elif coordinates_x == 2:
            if new_list[coordinates_y + 2] == " ":
                if number_of_moves % 2 == 1:
                    new_list[coordinates_y + 2] = "X"
                elif number_of_moves % 2 == 0:
                    new_list[coordinates_y + 2] = "O"
                fight_place(new_list)
                counter_of += 1
                number_of_moves += 1
                win_check(new_list)
                if win_check(new_list):
                    break
                else:
                    continue
            elif new_list[coordinates_y + 2] == "X" or new_list[coordinates_y + 2] == "O":
                print("This cell is occupied! Choose another one!")
                continue
        elif coordinates_x == 3:
            if new_list[coordinates_y + 5] == " ":
                if number_of_moves % 2 == 1:
                    new_list[coordinates_y + 5] = "X"
                elif number_of_moves % 2 == 0:
                    new_list[coordinates_y + 5] = "O"
                fight_place(new_list)
                counter_of += 1
                number_of_moves += 1
                win_check(new_list)
                if win_check(new_list):
                    break
                else:
                    continue
            elif new_list[coordinates_y + 5] == "X" or new_list[coordinates_y + 5] == "O":
                print("This cell is occupied! Choose another one!")
                continue
    elif (3 < coordinates_y or coordinates_y < 1) or (3 < coordinates_x or coordinates_x < 1):
        print("Coordinates should be from 1 to 3!")
    else:
        try:
            isinstance(coordinates_x, int) and isinstance(coordinates_y, int)
        except ValueError:
            print("You should enter numbers!")
    if counter_of == 9 or wins != 0:
        break
