from colorama import Style
from colorama import Fore

red = Fore.LIGHTRED_EX
blue = Fore.LIGHTBLUE_EX
style = Style.RESET_ALL


def init_board():
    """Returns an empty 3-by-3 board (with .).""" 
    
    board = [[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."],[".",".",".",".","."], [".",".",".",".","."]]

    return board


#def get_move(board, player):
def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    rows = ['A', 'B', 'C', 'D', 'E']
    cols_str = ['1', '2', '3', '4', '5']

    player_input = None
    while player_input == None:
        player_input = input("Provide coordinates: ").upper()
        if player_input[0] not in rows or player_input[1] not in cols_str:
            player_input = None
            continue
        elif len(player_input) != 2:
            player_input = None
            continue  
        else:
            row = rows.index(player_input[0])
            col = cols_str.index(player_input[1])
            if board[row][col] == ".":
                return row, col
            else:
                player_input = None


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col

def mark(board, player, row, col):
#def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""

    board[row][col] = player

    
    #pass


def has_won(board, player):
    """Returns True if player has won the game."""

    row_len = len(board[0])
    col_len = len(board)

    cross_template = [['00', '11', '22'],['02','11', '20']]
    in_col = [0, 0, 0, 0, 0]
    cross = [0, 0]
    for row in range(row_len):
        in_row = 0
        for col in range(col_len):
            if board[row][col] == player:
                in_row += 1
                in_col[col] += 1
                if f"{row}{col}" in cross_template[0]:
                    cross[0] += 1
                if f"{row}{col}" in cross_template[1]:
                    cross[1] += 1
            if in_row == 3:
                    return True
            elif 3 in in_col or 3 in cross:
                    return True
            elif board[row][col] != player:
                in_row = 0
                in_col[col] = 0
    
    return False

          


def is_full(board):
    """Returns True if board is full."""
    for row in board:
        for item in row:
            if item == ".":
                return False
    else:
        print("BOARD FULL")
        return True


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    row_len = len(board[0])
    col_len = len(board)

    letter = ['A', 'B', 'C', 'D', 'E']
    number = ['1', '2', '3', '4', '5']
    current_row = 0
    lines = []
    for line in range(col_len):
        lines.append("---")
        



    for i in range(row_len):
        print("   " f"{number[i]}", end="")
    print()
    for row in board:
        print(letter[current_row], end="  ")
        print(" | ".join(row))
        current_row += 1
        if current_row <= col_len - 1:
            print(" ", "+".join(lines))

    #pass


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == "tie":
        print("It's a tie")
    else:
        print(f"{winner} has won!")


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()
    print_board(board)
    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    #print_board(board)
    while not is_full(board) and not has_won(board, f"{red}O{style}") and not has_won(board, f"{blue}X{style}"):
        row, col = get_move(board, f"{blue}X{style}")
        mark(board, f"{blue}X{style}", row, col)
        print_board(board)
        if not is_full(board) and not has_won(board, f"{red}O{style}") and not has_won(board, f"{blue}X{style}"):
            row, col = get_move(board, f"{red}O{style}")
            mark(board, f"{red}O{style}", row, col)
            print_board(board)
    if is_full(board):
        winner = "tie"
    if has_won(board, f"{blue}X{style}"):
        winner = f"{blue}X{style}"
    else:
        winner = f"{red}O{style}"
    print_result(winner)


def main_menu():
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
