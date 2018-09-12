board = [
    ['1', '2', '3', '4', '5', '6', '7'],
    ['1', '2', '3', '4', '5', '6', '7'],
    ['1', '2', '3', '4', '5', '6', '7'],
    ['1', '2', '3', '4', '5', '6', '7'],
    ['1', '2', '3', '4', '5', '6', '7'],
    ['1', '2', '3', '4', '5', '6', '7'],
    ]

def print_board(board):
    printable = ''
    for line in range(len(board)):
        for field in range(len(board[line])):
            printable = printable + ' | ' + board[line][field]
        printable = printable + ' | \n |___|___|___|___|___|___|___| \n |   |   |   |   |   |   |   | \n'
    printable = '\n  ___________________________ \n |   |   |   |   |   |   |   | \n' + printable
    print(printable)

print_board(board)
