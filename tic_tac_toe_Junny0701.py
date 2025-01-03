tic_tac_toe_list = [' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '\n',
                    ' ', ' ', '7', ' ', ' ', '|', ' ', ' ', '8', ' ', ' ', '|', ' ', ' ', '9', ' ', ' ', '\n', # Index: 20, 26, 32
                    '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '\n',
                    ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '\n',
                    ' ', ' ', '4', ' ', ' ', '|', ' ', ' ', '5', ' ', ' ', '|', ' ', ' ', '6', ' ', ' ', '\n', # Index: 74, 80, 86
                    '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '|', '_', '_', '_', '_', '_', '\n',
                    ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '\n', 
                    ' ', ' ', '1', ' ', ' ', '|', ' ', ' ', '2', ' ', ' ', '|', ' ', ' ', '3', ' ', ' ', '\n', # Index: 128, 134, 140
                    ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '\n'
                    ]
available_coordinates = ['1','2','3','4','5','6','7','8','9']
user_coordinates = []
computer_coordinates = []
winning_combinations = [
        ['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'],  # Rows
        ['1', '4', '7'], ['2', '5', '8'], ['3', '6', '9'],  # Columns
        ['1', '5', '9'], ['3', '5', '7']              # Diagonals
        ]

def draw_user_input(user_choice):
    for char in tic_tac_toe_list:
        if char == user_choice:
            tic_tac_toe_list[tic_tac_toe_list.index(user_choice)] = 'X'
            available_coordinates.remove(user_choice)
            user_coordinates.append(user_choice)

    for char in tic_tac_toe_list:
        if char.isnumeric():
            print(' ', end='')
            continue
        print(char, end = '')

def draw_computer():
    found = False
    if len(user_coordinates) == 1:
        if '5' in available_coordinates:
            tic_tac_toe_list[tic_tac_toe_list.index('5')] = 'O'
            available_coordinates.remove('5')
            computer_coordinates.append('5')
            found = True
        elif '7' in available_coordinates:
            tic_tac_toe_list[tic_tac_toe_list.index('7')] = 'O'
            available_coordinates.remove('7')
            computer_coordinates.append('7')
            found = True
    elif not found:
        for coord in user_coordinates:
            for sublist in winning_combinations:
                n = 0
                if coord in sublist:
                    for coor in user_coordinates:
                        if coor in sublist:
                            n += 1
                        if n == 2:
                            for win_coor in sublist:
                                if win_coor in available_coordinates:
                                    tic_tac_toe_list[tic_tac_toe_list.index(win_coor)] = 'O'
                                    available_coordinates.remove(win_coor)
                                    computer_coordinates.append(win_coor)
                                    found = True
                                    break
                        if found:
                            break
                if found:
                    break
            if found:
                break
    if not found:
        for coor in available_coordinates:
            if coor == '2':
                tic_tac_toe_list[tic_tac_toe_list.index('2')] = 'O'
                available_coordinates.remove('2')
                computer_coordinates.append('2')
                found = True
                break
            elif coor == '4':
                tic_tac_toe_list[tic_tac_toe_list.index('4')] = 'O'
                available_coordinates.remove('4')
                computer_coordinates.append('4')
                found = True
                break
            elif coor == '6':
                tic_tac_toe_list[tic_tac_toe_list.index('6')] = 'O'
                available_coordinates.remove('6')
                computer_coordinates.append('6')
                found = True
                break
            elif coor == '8':
                tic_tac_toe_list[tic_tac_toe_list.index('8')] = 'O'
                available_coordinates.remove('8')
                computer_coordinates.append('8')
                found = True
                break

    if not found and 2 <= len(user_coordinates):
        tic_tac_toe_list[tic_tac_toe_list.index(available_coordinates[0])] = 'O'
        computer_coordinates.append(available_coordinates[0])
        available_coordinates.remove(available_coordinates[0])


    print("Computer's turn: ")
    for char in tic_tac_toe_list:
        if char.isnumeric():
            print(' ', end='')
            continue
        print(char, end='')

def check_winner():
    for sublist in winning_combinations:
        user = 0
        for coor in user_coordinates:
            if coor in sublist:
                user += 1
        if user == 3:
            return 'user'

    for sublist in winning_combinations:
        computer = 0 
        for coord in computer_coordinates:
            if coord in sublist:
                computer += 1
        if computer == 3:
            return 'computer'

def tic_tac_toe():
    print('Welcome to tic tac toe game!')
    for char in tic_tac_toe_list:
        print(char, end='')

    while True:
        user_input = input('Chose your coordinate (a number): ').strip()
        if not user_input.isnumeric() or not 0 < int(user_input) < 10:
            print('Invalid input')
            continue
        draw_user_input(user_input)
            
        if check_winner() == 'user':
            print('You win!')
            break
        elif len(available_coordinates) == 0:
            print('Draw')
            print("good game")
            break

        draw_computer()
        if check_winner() == 'computer':
            print('Computer win!')
            print("good game")
            break

if __name__ == "__main__":
    tic_tac_toe()