import subprocess as sub
import random

def clear():
    sub.run(["clear"])

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.','.','.'],['.','.','.'],['.','.','.']]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    rows = ['A', 'B', 'C']
    cols = [1, 2, 3]
    cols_str = list(map(str, cols))
    user_input = None
    while user_input is None:
        user_input = input("Give coordinates: ")
        if len(user_input) != 2:
            user_input = None
        elif user_input[0].upper() not in rows or user_input[1] not in cols_str:
            user_input = None
        else:
            row = rows.index(user_input[0].upper())
            col = cols.index(int(user_input[1]))
        
        if board[row][col] == '.':
            return row, col
        else:
            user_input = None
    


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0

    row_len = len(board[0])
    col_len = len(board)

    for mark in ['O', 'X']:
        row_data = {
            'free_cords': [],
            'cords': []
        }
        for row_index in range(row_len):
            for col_index in range(col_len):
                if board[row_index][col_index] == mark:
                    try:
                        if [row_index, col_index - 1] in row_data['cords'] or [row_index, col_index - 1] in row_data['free_cords']:
                            row_data['cords'].append([row_index, col_index])
                        else:
                            row_data['cords'].clear()
                            row_data['free_cords'].clear()
                            row_data['cords'].append([row_index, col_index])
                    except IndexError:
                        row_data['cords'].append([row_index, col_index])
                elif board[row_index][col_index] == '.' and [row_index, col_index - 1] not in row_data['free_cords']:
                    row_data['free_cords'].append([row_index, col_index])
                else:
                    row_data['cords'].clear()
                    row_data['free_cords'].clear()

            if len(row_data['cords']) == 2:
                if len(row_data['free_cords']) > 0:
                    row = row_data['free_cords'][0][0]
                    col = row_data['free_cords'][0][1]
                    return row, col
            else:
                row_data['cords'].clear()
                row_data['free_cords'].clear()

        
        col_data = {
            'free_cords': [],
            'cords': []
        }
        for col_index in range(col_len):
            for row_index in range(row_len):
                if board[row_index][col_index] == mark:
                    try:
                        if [row_index - 1, col_index] in col_data['cords'] or [row_index - 1, col_index] in col_data['free_cords']:
                            col_data['cords'].append([row_index, col_index])
                        else:
                            col_data['cords'].clear()
                            col_data['free_cords'].clear()
                            col_data['cords'].append([row_index, col_index])
                    except IndexError:
                        col_data['cords'].append([row_index, col_index])
                elif board[row_index][col_index] == '.' and [row_index - 1, col_index] not in col_data['free_cords']:
                    col_data['free_cords'].append([row_index, col_index])
                else:
                    col_data['cords'].clear()
                    col_data['free_cords'].clear()

            if len(col_data['cords']) == 2:
                if len(col_data['free_cords']) > 0:
                    row = col_data['free_cords'][0][0]
                    col = col_data['free_cords'][0][1]
                    return row, col
            else:
                col_data['cords'].clear()
                col_data['free_cords'].clear()

        direct = {}
        for i in range(row_len):
            if (row_len - i) > 3 - 1: # 3 - liczba znaków aby wygrać
                try:
                    direct[i].append(1)
                except KeyError:
                    direct[i] = [1]
            if (i + 1) >= 3:
                try:
                    direct[i].append(-1)
                except KeyError:
                    direct[i] = [-1]

        cross_data = {
            'free_cords': [],
            'cords': []
        }
        for col_index in range(col_len):
            try:
                for col_d in direct[col_index]:
                    d = [1, col_d]
                    coord = [0, col_index]
                    while True:
                        try:
                            if board[coord[0]][coord[1]] == mark:
                                try:
                                    if [coord[0] - d[0], coord[1] - d[1]] in cross_data['cords'] or [coord[0] - d[0], coord[1] - d[1]] in cross_data['free_cords']:
                                        cross_data['cords'].append([coord[0], coord[1]])
                                    else:
                                        cross_data['cords'].clear()
                                        cross_data['free_cords'].clear()
                                        cross_data['cords'].append([coord[0], coord[1]])
                                except IndexError:
                                    cross_data['cords'].append([coord[0], coord[1]])
                            elif board[coord[0]][coord[1]] == '.' and [coord[0] - d[0], coord[1] - d[1]] not in cross_data['free_cords']:
                                cross_data['free_cords'].append([coord[0], coord[1]])
                            else:
                                cross_data['cords'].clear()
                                cross_data['free_cords'].clear()
                        except IndexError:
                            break
                        coord[0] += d[0]
                        coord[1] += d[1]
                    if len(cross_data['cords']) == 2:
                        if len(cross_data['free_cords']) > 0:
                            row = cross_data['free_cords'][0][0]
                            col = cross_data['free_cords'][0][1]
                            return row, col
                    else:
                        cross_data['cords'].clear()
                        cross_data['free_cords'].clear()
            except KeyError:
                pass

        cross_data = {
            'free_cords': [],
            'cords': []
        }
        for col_index in range(1, col_len):
            try:
                for col_d in direct[col_index]:
                    d = [1, col_d]
                    coord = [row_len - 1, col_index] # test od ostatniego wiersza i drugiej kolumny
                    while True:
                        try:
                            if board[coord[0]][coord[1]] == mark:
                                try:
                                    if [coord[0] - d[0], coord[1] - d[1]] in cross_data['cords'] or [coord[0] - d[0], coord[1] - d[1]] in cross_data['free_cords']:
                                        cross_data['cords'].append([coord[0], coord[1]])
                                    else:
                                        cross_data['cords'].clear()
                                        cross_data['free_cords'].clear()
                                        cross_data['cords'].append([coord[0], coord[1]])
                                except IndexError:
                                    cross_data['cords'].append([coord[0], coord[1]])
                            elif board[coord[0]][coord[1]] == '.' and [coord[0] - d[0], coord[1] - d[1]] not in cross_data['free_cords']:
                                cross_data['free_cords'].append([coord[0], coord[1]])
                            else:
                                cross_data['cords'].clear()
                                cross_data['free_cords'].clear()
                        except IndexError:
                            break
                        coord[0] += d[0]
                        coord[1] += d[1]
                    if len(cross_data['cords']) == 2:
                        if len(cross_data['free_cords']) > 0:
                            row = cross_data['free_cords'][0][0]
                            col = cross_data['free_cords'][0][1]
                            return row, col
                    else:
                        cross_data['cords'].clear()
                        cross_data['free_cords'].clear()
            except KeyError:
                pass

    if row_len == 3:
        if board[1][1] == '.':
            row = 1
            col = 1
            return row, col
        else:
            for row, col in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                if board[row][col] == '.':
                    return row, col
                else:
                    free_places = get_free_places(board)
                    row, col = free_places[random.randrange(len(free_places))]
                    return row, col
    else:
        free_places = get_free_places(board)
        row, col = free_places[random.randrange(len(free_places))]
        return row, col

def get_free_places(board):
    row_len = len(board[0])
    col_len = len(board)

    free_places = []
    for row_index in range(row_len):
        for col_index in range(col_len):
            if board[row_index][col_index] == '.':
                free_places.append([row_index, col_index])
    return free_places

def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board[row][col] = player['mark']


def has_won_mateusz(board, player):
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

def has_won(board, player):
    row_len = len(board[0])
    col_len = len(board)

    row = []
    for row_index in range(row_len):
        for col_index in range(col_len):
            if board[row_index][col_index] == player['mark']:
                try:
                    if row[-1][0] == row_index and row[-1][1] == col_index - 1:
                        row.append([row_index, col_index])
                    else:
                        row.clear()
                except IndexError:
                    row.append([row_index, col_index])
        if len(row) == 3:
            for cord in row:
                board[cord[0]][cord[1]] = f"\033[32m{player['mark']}\033[0m"
            return True
        row.clear()
    col = []
    for col_index in range(col_len):
        for row_index in range(row_len):
            if board[row_index][col_index] == player['mark']:
                try:
                    if col[-1][0] == row_index - 1 and col[-1][1] == col_index:
                        col.append([row_index, col_index])
                    else:
                        col.clear()
                except IndexError:
                    col.append([row_index, col_index])
        if len(col) == 3:
            for cord in col:
                board[cord[0]][cord[1]] = f"\033[32m{player['mark']}\033[0m"
            return True
        else:
            col.clear()

    direct = {}
    for i in range(row_len):
        if (row_len - i) > 3 - 1: # 3 - liczba znaków aby wygrać
            try:
                direct[i].append(1)
            except KeyError:
                direct[i] = [1]
        if (i + 1) >= 3:
            try:
                direct[i].append(-1)
            except KeyError:
                direct[i] = [-1]

    cross = []
    for col_index in range(col_len):
        try:
            for col_d in direct[col_index]:
                d = [1, col_d]
                coord = [0, col_index]
                while True:
                    try:
                        if board[coord[0]][coord[1]] == player['mark']:
                            cross.append([coord[0], coord[1]])
                        else:
                            cross.clear()
                    except IndexError:
                        break
                    coord[0] += d[0]
                    coord[1] += d[1]
                if len(cross) == 3:
                    for cord in cross:
                        board[cord[0]][cord[1]] = f"\033[32m{player['mark']}\033[0m"
                    return True
                else:
                    cross.clear()
        except KeyError:
            pass

    cross = []
    for col_index in range(1, col_len):
        try:
            for col_d in direct[col_index]:
                d = [1, col_d]
                coord = [row_len - 1, col_index] # test od ostatniego wiersza i drugiej kolumny
                while True:
                    try:
                        if board[coord[0]][coord[1]] == player['mark']:
                            cross.append([coord[0], coord[1]])
                        else:
                            cross.clear()
                    except IndexError:
                        break
                    coord[0] += d[0]
                    coord[1] += d[1]
                if len(cross) == 3:
                    for cord in cross:
                        board[cord[0]][cord[1]] = f"\033[32m{player['mark']}\033[0m"
                    return True
                else:
                    cross.clear()
        except KeyError:
            pass
    
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
    if mode == 'HUMAN-HUMAN':
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
    elif mode == 'HUMAN-AI':
        player_name1 = None
        while player_name1 is None:
            player_name1 = input("Player 1 [X], give your name: ")
            if len(player_name1) < 3:
                print("Your name should be at least three characters long.")
                player_name1 = None
        board = init_board()
        player1 = {}
        player1['name'] = player_name1
        player1['mark'] = 'X'
        computer = {}
        computer['name'] = 'computer'
        computer['mark'] = 'O'
        # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
        loop = True
        while loop:
            #clear()
            print_board(board)
            row, col = get_move(board, 1)
            mark(board, player1, row, col)
            if has_won(board, player1):
                winner = 'X'
                #clear()
                print_board(board)
                print_result(winner)
                loop = False
                continue
            elif is_full(board):
                winner = 'tie'
                #clear()
                print_board(board)
                print_result(winner)
                loop = False
                continue
            #clear()
            print_board(board)
            output = get_ai_move(board, computer)
            print(output)
            row, col = output
            mark(board, computer, row, col)
            if has_won(board, computer):
                winner = 'O'
                #clear()
                print_board(board)
                print_result(winner)
                loop = False
                continue
            elif is_full(board):
                winner = 'tie'
                #clear()
                print_board(board)
                print_result(winner)
                loop = False
                continue

def main_menu():
#    tictactoe_game('HUMAN-HUMAN')
    tictactoe_game('HUMAN-AI')


if __name__ == '__main__':
    main_menu()


#print(has_won(init_board(), {'mark': 'X'}))