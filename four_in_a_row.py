board = [
    ['1A', '2B', '3C', '4D', '5E', '6F', '7G'],
    ['1A', '2B', '3C', '4D', '5E', '6F', '7G'],
    ['1A', '2B', '3C', '4D', '5E', '6F', '7G'],
    ['1A', '2B', '3C', '4D', '5E', '6F', '7G'],
    ['1A', '2B', '3C', '4D', '5E', '6F', '7G'],
    ['1A', '2B', '3C', '4D', '5E', '6F', '7G'],
    ]

def print_board(board):
    printable = ''
    for line in range(len(board)):
        for field in range(len(board[line])):
            printable = printable + ' | ' + board[line][field]
        printable = printable + ' | \n |____|____|____|____|____|____|____| \n |    |    |    |    |    |    |    | \n'
    printable = '\n  __________________________________ \n |    |    |    |    |    |    |    | \n' + printable
    print(printable)

print_board(board)
