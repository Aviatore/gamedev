import subprocess as sub

def clear():
    sub.run(["clear"])

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.','.','.'],['.','.','.'],['.','.','.']]
    return board

def please_do_something():
    #doing things
    pass


    


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player['mark']


def has_won(board, player):
    if board[0][0] == player['mark'] and board[0][1] == player['mark'] and board[0][2] == player['mark']:
        return True
    elif board[1][0] == player['mark'] and board[1][1] == player['mark'] and board[1][2] == player['mark']:
        return True
    elif board[2][0] == player['mark'] and board[2][1] == player['mark'] and board[2][2] == player['mark']:
        return True
    elif board[0][0] == player['mark'] and board[1][0] == player['mark'] and board[2][0] == player['mark']:
        return True
    elif board[0][1] == player['mark'] and board[1][1] == player['mark'] and board[2][1] == player['mark']:
        return True
    elif board[0][2] == player['mark'] and board[1][2] == player['mark'] and board[2][2] == player['mark']:
        return True
    
    elif board[0][0] == player['mark'] and board[1][1] == player['mark'] and board[2][2] == player['mark']:
        return True
    elif board[2][0] == player['mark'] and board[1][1] == player['mark'] and board[0][2] == player['mark']:
        return True

    else: 
        return False

def has_won_(board, player):
    """Returns True if player has won the game."""
    row_len = len(board[0])
    col_len = len(board)
    
    cross_template = [['00', '11', '22'], ['02', '11', '20']]
    cross = [0, 0]
    in_col = [0, 0, 0]
    for row in range(row_len):
        in_row = 0
        for col in range(col_len):
            if board[row][col] == player['mark']:
                in_row += 1
                in_col[col] += 1
                if f"{row}{col}" in cross_template[0]:
                    cross[0] += 1
                if f"{row}{col}" in cross_template[1]:
                    cross[1] += 1
        if in_row == 3:
            return True
    if 3 in in_col or 3 in cross:
        return True
    else:
        return False


def is_full(board):
    """Returns True if board is full."""
    row_len = len(board[0])
    col_len = len(board)
    empty = 0
    for row in range(row_len):
        for col in range(col_len):
            if board[row][col] == '.':
                empty += 1
    if empty == 0:
        return True
    else:
        return False


def print_board(board):
    letter = ["A", "B", "C"]
    current_row = 0

    
    print("   1   2   3   ")
    print()
    for row in board:
        print(letter[current_row], end="  ")
        print(row[0], row[1], row[2], sep = " | " )
        current_row += 1
        if current_row <= 2:
            print("  ---+---+---") 

def print_board_(board):
    """Prints a 3-by-3 board on the screen with borders."""
    row_len = len(board[0])
    col_len = len(board)
    rows = ['A', 'B', 'C']
    cols = [1, 2, 3]
    cols_str = list(map(str, cols))
    line = []
    for i in range(row_len):
        line.append("---")
    
    print("  ", "   ".join(cols_str))
    for index in range(col_len):
        print(f"{rows[index]}  {' | '.join(board[index])}")
        if index < row_len - 1:
            print(" ", "+".join(line))
    

def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == "tie":
        print("It's a tie!")
    else:
        print(f"{winner} has won!")


def tictactoe_game(mode='HUMAN-HUMAN'):
    player_name1 = None
    while player_name1 is None:
        player_name1 = input("Player 1 [X], give your name: ")
        if len(player_name1) < 3:
            print("Your name should be at least three characters long.")
            player_name1 = None
    player_name2 = None
    while player_name2 is None:
        player_name2 = input("Player 2 [O], give your name: ")
        if len(player_name2) < 3:
            print("Your name should be at least three characters long.")
            player_name2 = None
    board = init_board()
    player1 = {}
    player1['name'] = player_name1
    player1['mark'] = 'X'
    player2 = {}
    player2['name'] = player_name2
    player2['mark'] = 'O'
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    loop = True
    while loop:
        clear()
        print_board(board)
        row, col = get_move(board, 1)
        mark(board, player1, row, col)
        if has_won(board, player1):
            winner = 'X'
            clear()
            print_board(board)
            print_result(winner)
            loop = False
            continue
        elif is_full(board):
            winner = 'tie'
            clear()
            print_board(board)
            print_result(winner)
            loop = False
            continue
        clear()
        print_board(board)
        row, col = get_move(board, 1)
        mark(board, player2, row, col)
        if has_won(board, player2):
            winner = 'O'
            print_board(board)
            print_result(winner)
            loop = False
            continue
        elif is_full(board):
            winner = 'tie'
            clear()
            print_board(board)
            print_result(winner)
            loop = False
            continue

def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()


#print(has_won(init_board(), {'mark': 'X'}))