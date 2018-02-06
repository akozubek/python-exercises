

board = [[" ", " ", " "],
         [" ", " ", " "], 
         [" ", " ", " "]]

"""
Pythonic one-liner for multiline array
def print_board(b): 
    print("\n-+-+-\n".join([ '|'.join(line) for line in b ]))
"""

"""
Mozliwa struktura (latwiejsza): tablica 0..10, 1-9 odpowiadaja miejscom
na tablicy.
"""
def naive_print_board(board):
    print(board[0][0] + '|' + board[0][1] + '|' + board[0][2])
    print('-+-+-')
    print(board[1][0] + '|' + board[1][1] + '|' + board[1][2])
    print('-+-+-')
    print(board[2][0] + '|' + board[2][1] + '|' + board[2][2])

print_board(board)

print("Naive:")
naive_print_board(board)

