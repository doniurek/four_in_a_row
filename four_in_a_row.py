def print_board(board):
    printable = ''
    for line in range(len(board)):
        for field in range(len(board[line])):
            printable = printable + ' | ' + board[line][field]
        printable = printable + ' | \n |___|___|___|___|___|___|___| \n |   |   |   |   |   |   |   | \n'
    printable = '\n  ___________________________ \n |   |   |   |   |   |   |   | \n' + printable
    print(printable)

board = [
    ['1', '2', '3', '4', '5', '6', '7'],
    ['1', '2', '3', '4', '5', '6', '7'],
    ['1', '2', '3', '4', '5', '6', '7'],
    ['1', '2', '3', '4', '5', '6', '7'],
    ['1', '2', '3', '4', '5', '6', '7'],
    ['1', '2', '3', '4', '5', '6', '7'],
    ]

instruction = 'Four in a row to gra dla dwóch osób.\
\nPierwszy gracz wybiera kolumnę, do której wrzuca swój "żeton".\
\nŻeton zajmuje najniższą pozycję w kolumnie.\
\nGracze wrzucają swoje żetony na przemian, aż jeden z nich ułoży cztery żetony\
\nw poziomie, pionie lub ukosie.\
\nWygrywa ten gracz, który zrobi to jako pierwszy.\
\nJeżeli natomiast plansza się zapełni, a nie utworzy się żadna czwórka,\
\njest remis.'

print(instruction)

print_board(board)
