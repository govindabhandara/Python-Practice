# Game board representation
tic_tac_toe = [
    ["X", "O", " "],
    [" ", "X", " "],
    ["O", " ", "X"]
]

def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")

# you need to call the function to see output
print_board(tic_tac_toe)
