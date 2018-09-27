def print_board(board):
    printable = ''
    for row in range(6):
        for field in range(7):
            printable = printable + ' | ' + str(board[row][field])
        printable = printable + ' | \n |___|___|___|___|___|___|___|' \
        + ' \n |   |   |   |   |   |   |   | \n'
    printable = '\n  ___________________________ \n' \
    + ' |   |   |   |   |   |   |   | \n' + printable
    print(printable)

def set_token(board, gamer, position):
    for row in reversed(range(6)):
        if type(board[row][position-1]) == int:
            board[row][position-1] = gamer
            break

def check_move(board, position):
    return position in range(1,8) and type(board[0][position-1]) == int

def win(board):
    # horizontal
    for row in range(6):
        for column in range(4):
            if type(board[row][column]) == str \
            and board[row][column] == board[row][column+1] \
            and board[row][column+1] == board[row][column+2] \
            and board[row][column+2] == board[row][column+3]:
                return True
    # vertical
    for row in range(3):
        for column in range(7):
            if type(board[row][column]) == str \
            and board[row][column] == board[row+1][column] \
            and board[row+1][column] == board[row+2][column] \
            and board[row+2][column] == board[row+3][column]:
                return True

    # \
    for row in range(3):
        for column in range(4):
            if board[row][column] == board[row+1][column+1] \
            and board[row+1][column+1] == board[row+2][column+2] \
            and board[row+2][column+2] == board[row+3][column+3]:
                return True
    # /
    for row in range(3,6):
        for column in range(4):
            if board[row][column] == board[row-1][column+1] \
            and board[row-1][column+1] == board[row-2][column+2] \
            and board[row-2][column+2] == board[row-3][column+3]:
                return True

    return False

def gamer_info_string(gamer):
    if gamer == "@":
        return "gracz nr. 1 (@)"
    return "gracz nr. 2 (#)"


if __name__ == "__main__":
    board = [
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        [1, 2, 3, 4, 5, 6, 7],
        ]

    instruction = 'Four in a row to gra dla dwóch osób.\
    \nPierwszy gracz wybiera kolumnę, do której wrzuca swój "żeton" (O albo X).\
    \nŻeton zajmuje najniższą pozycję w kolumnie.\
    \nGracze wrzucają swoje żetony na przemian, aż jeden z nich ułoży cztery żetony\
    \nw poziomie, pionie lub ukosie.\
    \nWygrywa ten gracz, który zrobi to jako pierwszy.\
    \nJeżeli natomiast plansza się zapełni, a nie utworzy się żadna czwórka,\
    \njest remis.'

    print(instruction)

    print_board(board)

    for round_ in range(1, 43):
        if round_ % 2 !=0:
            gamer = "@"
        else:
            gamer = "#"

        print(gamer_info_string(gamer).capitalize())

        try:
            position = int(input("Podaj numer kolumny, do której chcesz wrzucić żeton: "))
        except ValueError:
            position = 0

        while not check_move(board, position):
            try:
                position = int(input("Niepoprawny numer kolumny, spróbuj jeszcze raz: "))
            except ValueError:
                position = 0

        set_token(board, gamer, position)

        print_board(board)

        if round_ > 6 and win(board):
            print("Koniec gry. Wygrywa", gamer_info_string(gamer)+". Gratulacje!" )
            exit()

    print("Koniec gry. Remis!")
