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
