# Function to print the board
def print_board(board):
    print("-------------")
    for row in range(3):
        print("|", board[row][0], "|", board[row][1], "|", board[row][2], "|")
        print("-------------")

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in range(3):
        if all([board[row][col] == player for col in range(3)]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check if the board is full (for tie game)
def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Function for player input
def player_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Cell already taken, try again!")
        except (ValueError, IndexError):
            print("Invalid move, please enter a number between 1 and 9.")

# Main game function
def play_game():
    # Initialize the empty board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    # Game loop
    while True:
        print_board(board)
        player_move(board, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
if __name__ == "__main__":
    play_game()
