def print_board(board):
    printable = ''
    for line in range(len(board)):
        for field in range(len(board[line])):
            printable = printable + ' | ' + str(board[line][field])
        printable = printable + ' | \n |___|___|___|___|___|___|___| \n |   |   |   |   |   |   |   | \n'
    printable = '\n  ___________________________ \n |   |   |   |   |   |   |   | \n' + printable
    print(printable)

def set_token(board, gamer, position):
    for i in reversed(range(6)):
        if type(board[i][position-1]) == int:
            board[i][position-1] = gamer
            break
    return board

def check_move(board, position):
    return position in range(1,8) and type(board[0][position-1]) == int

def win(board):
    # horizontal
    for i in range(6):
        for j in range(4):
            if type(board[i][j]) == str and board[i][j] == board[i][j+1] and board[i][j+1] == board[i][j+2] and board[i][j+2] == board[i][j+3]:
                return True
    # vertical
    for i in range(3):
        for j in range(7):
            if type(board[i][j]) == str and board[i][j] == board[i+1][j] and board[i+1][j] == board[i+2][j] and board[i+2][j] == board[i+3][j]:
                return True

    l = []
    for i in range(6):
        l += board[i]

    # \
    for i in range(18):
        if l[i] == l[i+8] and l[i+8] == l[i+16] and l[i+16] == l[i+24]:
            return True
    # /
    for i in range(24):
        if l[i] == l[i+6] and l[i+6] == l[i+12] and l[i+12] == l[i+18]:
            return True

    return False

def which_gamer(gamer):
    if gamer == "@":
        return "gracz nr. 1"
    return "gracz nr. 2"

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

for round in range(1, 43):
    if round % 2 !=0:
        gamer = "@"
        print('Gracz nr. 1 (@)')
    else:
        gamer = "#"
        print('Gracz nr. 2 (#)')

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

    if round > 6 and win(board):
        print("Koniec gry. Wygrywa", which_gamer(gamer)+". Gratulacje!" )
        exit()

print("Koniec gry. Remis!")
