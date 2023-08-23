import math

PLAYER_X = "X"
PLAYER_O = "O"
EMPTY = " "

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    return all([cell != EMPTY for row in board for cell in row])

def evaluate(board):
    if check_winner(board, PLAYER_X):
        return 1
    elif check_winner(board, PLAYER_O):
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing, alpha, beta):
    if check_winner(board, PLAYER_X):
        return 1
    elif check_winner(board, PLAYER_O):
        return -1
    elif is_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_X
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = EMPTY
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == EMPTY:
                    board[i][j] = PLAYER_O
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = EMPTY
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_eval = -math.inf
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                board[i][j] = PLAYER_X
                move_eval = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = EMPTY
                if move_eval > best_eval:
                    best_eval = move_eval
                    best_move = (i, j)
    return best_move

def main():
    board = [[EMPTY for _ in range(3)] for _ in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    
    while True:
        print_board(board)

        row, col = find_best_move(board)
        board[row][col] = PLAYER_X

        if check_winner(board, PLAYER_X):
            print_board(board)
            print("AI wins!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

        print_board(board)

        user_row = int(input("Enter row (0, 1, 2): "))
        user_col = int(input("Enter column (0, 1, 2): "))
        while board[user_row][user_col] != EMPTY:
            print("Cell already taken. Try again.")
            user_row = int(input("Enter row (0, 1, 2): "))
            user_col = int(input("Enter column (0, 1, 2): "))
        board[user_row][user_col] = PLAYER_O

        if check_winner(board, PLAYER_O):
            print_board(board)
            print("You win!")
            break
        elif is_full(board):
            print_board(board)
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
