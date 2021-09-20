from IPython.display import clear_output


def display_func(desk):
    clear_output()

    print(str(desk[0]) + "  " + str(desk[1]) + "  " + str(desk[2]))
    print(str(desk[3]) + "  " + str(desk[4]) + "  " + str(desk[5]))
    print(str(desk[6]) + "  " + str(desk[7]) + "  " + str(desk[8]))


def your_choice(desk):

    choice = "String"
    range1 = False
    while choice.isdigit() == False or range1 == False:
        choice = input("Wprowadz liczbę od 1-9: ")
        if choice.isdigit() == False or int(choice) not in range(1,10) or desk[int(choice)-1] != '*':
            print("Błąd")
            continue
        if choice.isdigit() and int(choice) in range(1,10):
            range1 = True
            return int(choice),desk

def algorithm(choice, desk, player):
    if player == 'A':
        desk[choice-1] = 'X'
        if desk[0] == 'X' and desk[1] == 'X' and desk[2] == 'X':
            return True, player
        elif desk[3] == 'X' and desk[4] == 'X' and desk[5] == 'X':
            return True, player
        elif desk[6] == 'X' and desk[7] == 'X' and desk[8] == 'X':
            return True, player
        elif desk[0] == 'X' and desk[3] == 'X' and desk[6] == 'X':
            return True, player
        elif desk[1] == 'X' and desk[4] == 'X' and desk[7] == 'X':
            return True, player
        elif desk[2] == 'X' and desk[5] == 'X' and desk[8] == 'X':
            return True, player
        elif desk[0] == 'X' and desk[4] == 'X' and desk[8] == 'X':
            return True, player
        elif desk[6] == 'X' and desk[4] == 'X' and desk[2] == 'X':
            return True, player
        else:
            return False, player
    elif player == 'B':
        desk[choice-1] = '0'
        if desk[0] == '0' and desk[1] == '0' and desk[2] == '0':
            return True, player
        elif desk[3] == '0' and desk[4] == '0' and desk[5] == '0':
            return True, player
        elif desk[6] == '0' and desk[7] == '0' and desk[8] == '0':
            return True, player
        elif desk[0] == '0' and desk[3] == '0' and desk[6] == '0':
            return True, player
        elif desk[1] == '0' and desk[4] == '0' and desk[7] == '0':
            return True, player
        elif desk[2] == '0' and desk[5] == '0' and desk[8] == '0':
            return True, player
        elif desk[0] == '0' and desk[4] == '0' and desk[8] == '0':
            return True, player
        elif desk[6] == '0' and desk[4] == '0' and desk[2] == '0':
            return True, player
        else:
            return False, player


def space_check(board, position):
    return board[position] == '*'

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i-1):
            return False
    return True

x = False
desk = ['*', '*', '*', '*', '*', '*', '*', '*', '*',]
i = 2
player = 'A'
while x == False:
    if full_board_check(desk):
        display_func(desk)
        print('Remis!')
        break


    if i%2 == 0:
        player = 'A'
    else:
        player = 'B'
    display_func(desk)
    [choice, desk] = your_choice(desk)
    [logic, player] = algorithm(choice, desk, player)
    if logic == True:
        display_func(desk)
        print("Wygrałeś graczu {}".format(player))
        x = True
    i+=1
