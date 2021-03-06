import subprocess as sub
import random
import time
import menu

GREEN = "\033[32m"
WHITE = "\033[0m"

def clear():
    sub.run(["clear"])

def init_board(size):
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    for row in range(size):
        board.append(('. '*size).split(" ")[:-1])
    return board


def get_move(board, player, board_props=None):
    """Returns the coordinates of a valid move for player on board."""
    row_len = len(board[0])
    col_len = len(board)
    rows_template = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    cols = []
    for col_index in range(col_len):
        cols.append(col_index + 1)
    cols_str = list(map(str, cols))
    rows = []
    for row_index in range(row_len):
        rows.append(rows_template[row_index])

    user_input = None
    while user_input is None:
        user_input = input(f"{player['name']}, please give coordinates: ")
        if user_input == 'quit':
            print("Good bye!")
            exit()
        elif len(user_input) != 2:
            user_input = None
            continue
        elif user_input[0].upper() not in rows or user_input[1] not in cols_str:
            user_input = None
            continue
        else:
            row = rows.index(user_input[0].upper())
            col = cols.index(int(user_input[1]))
        
        if board[row][col] == '.':
            return row, col
        else:
            user_input = None
    


def get_ai_move(board, player, board_props):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0

    row_len = len(board[0])
    col_len = len(board)
    if player['level'] == "Easy":
        free_places = get_free_places(board)
        row, col = free_places[random.randrange(len(free_places))]
        return row, col
    elif player['level'] == "Medium" or player['level'] == "Hard":
        best_move = {
            'free_cords': [],
            'num': 0
        }
        for mark in ['O', 'X']:
            

            row_data = {
                'free_cords': [],
                'cords': [],
                'free_num': 0
            }
            for row_index in range(row_len):
                for col_index in range(col_len):
                    if mark in board[row_index][col_index]:
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
                        row_data['free_num'] += 1
                    elif board[row_index][col_index] == '.':
                        row_data['cords'].clear()
                        row_data['free_cords'].clear()
                        row_data['free_cords'].append([row_index, col_index])
                        row_data['free_num'] += 1
                    else:
                        row_data['cords'].clear()
                        row_data['free_cords'].clear()
                    
                    #else:
                    #    row_data['cords'].clear()
                    #    row_data['free_cords'].clear()
                    if (row_len - board_props['num']) >= 1:
                        len_to_react = 2
                    else:
                        len_to_react = 1
                    if len(row_data['cords']) >= board_props['num'] - len_to_react and row_data['free_num'] >= (board_props['num'] - len(row_data['cords'])):
                        if len(row_data['free_cords']) > 0:
                            row = row_data['free_cords'][0][0]
                            col = row_data['free_cords'][0][1]
                            if len(row_data['cords']) > best_move['num']:
                                best_move['free_cords'] = [row, col]
                                best_move['num'] = len(row_data['cords'])
                            #return row, col
                #else:
                row_data['cords'].clear()
                row_data['free_cords'].clear()
                row_data['free_num'] = 0

            
            col_data = {
                'free_cords': [],
                'cords': [],
                'free_num': 0
            }
            for col_index in range(col_len):
                for row_index in range(row_len):
                    if mark in board[row_index][col_index]:
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
                        col_data['free_num'] += 1
                    elif board[row_index][col_index] == '.':
                        col_data['cords'].clear()
                        col_data['free_cords'].clear()
                        col_data['free_cords'].append([row_index, col_index])
                        col_data['free_num'] += 1
                    else:
                        col_data['cords'].clear()
                        col_data['free_cords'].clear()
                    
                    #else:
                    #    col_data['cords'].clear()
                    #    col_data['free_cords'].clear()
                    if (row_len - board_props['num']) >= 1:
                        len_to_react = 2
                    else:
                        len_to_react = 1
                    if len(col_data['cords']) >= board_props['num'] - len_to_react and col_data['free_num'] >= (board_props['num'] - len(col_data['cords'])):
                        if len(col_data['free_cords']) > 0:
                            row = col_data['free_cords'][0][0]
                            col = col_data['free_cords'][0][1]
                            if len(col_data['cords']) > best_move['num']:
                                best_move['free_cords'] = [row, col]
                                best_move['num'] = len(col_data['cords'])
                            #return row, col
                #else:
                col_data['cords'].clear()
                col_data['free_cords'].clear()
                col_data['free_num'] = 0

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
                'cords': [],
                'free_num': 0
            }
            for col_index in range(col_len):
                try:
                    for col_d in direct[col_index]:
                        d = [1, col_d]
                        coord = [0, col_index]
                        while True:
                            try:
                                if mark in board[coord[0]][coord[1]]:
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
                                    cross_data['free_num'] += 1
                                elif board[coord[0]][coord[1]] == '.':
                                    cross_data['cords'].clear()
                                    cross_data['free_cords'].clear()
                                    cross_data['free_cords'].append([coord[0], coord[1]])
                                    cross_data['free_num'] += 1
                                else:
                                    cross_data['cords'].clear()
                                    cross_data['free_cords'].clear()
                                    
                            except IndexError:
                                break
                            coord[0] += d[0]
                            coord[1] += d[1]
                            #print(cross_data)
                            if (row_len - board_props['num']) >= 1:
                                len_to_react = 2
                            else:
                                len_to_react = 1
                            if len(cross_data['cords']) >= board_props['num'] - len_to_react and cross_data['free_num'] >= (board_props['num'] - len(cross_data['cords'])):
                                if len(cross_data['free_cords']) > 0:
                                    row = cross_data['free_cords'][0][0]
                                    col = cross_data['free_cords'][0][1]
                                    if len(cross_data['cords']) > best_move['num']:
                                        best_move['free_cords'] = [row, col]
                                        best_move['num'] = len(cross_data['cords'])
                                    #return row, col
                        #else:
                        cross_data['cords'].clear()
                        cross_data['free_cords'].clear()
                        cross_data['free_num'] = 0
                except KeyError:
                    pass

            cross_data = {
                'free_cords': [],
                'cords': [],
                'free_num': 0
            }
            for col_index in range(1, col_len):
                try:
                    for col_d in direct[col_index]:
                        d = [-1, col_d]
                        coord = [row_len - 1, col_index] # test od ostatniego wiersza i drugiej kolumny
                        while True:
                            try:
                                if mark in board[coord[0]][coord[1]]:
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
                                    cross_data['free_num'] += 1
                                elif board[coord[0]][coord[1]] == '.':
                                    cross_data['cords'].clear()
                                    cross_data['free_cords'].clear()
                                    cross_data['free_cords'].append([coord[0], coord[1]])
                                    cross_data['free_num'] += 1
                                else:
                                    cross_data['cords'].clear()
                                    cross_data['free_cords'].clear()
                            except IndexError:
                                break
                            coord[0] += d[0]
                            coord[1] += d[1]
                            if (row_len - board_props['num']) >= 1:
                                len_to_react = 2
                            else:
                                len_to_react = 1
                            if len(cross_data['cords']) >= board_props['num'] - len_to_react and cross_data['free_num'] >= (board_props['num'] - len(cross_data['cords'])):
                                if len(cross_data['free_cords']) > 0:
                                    row = cross_data['free_cords'][0][0]
                                    col = cross_data['free_cords'][0][1]
                                    if len(cross_data['cords']) > best_move['num']:
                                        best_move['free_cords'] = [row, col]
                                        best_move['num'] = len(cross_data['cords'])
                                    #return row, col
                        #else:
                        cross_data['cords'].clear()
                        cross_data['free_cords'].clear()
                        cross_data['free_num'] = 0
                except KeyError:
                    pass
            
            cross_data = {
                'free_cords': [],
                'cords': [],
                'free_num': 0
            }
            for row_index in range(1, row_len):
                try:
                    for row_d in direct[row_index]:
                        d = [row_d, 1]
                        coord = [row_index, 0]
                        while True:
                            try:
                                if mark in board[coord[0]][coord[1]]:
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
                                    cross_data['free_num'] += 1
                                elif board[coord[0]][coord[1]] == '.':
                                    cross_data['cords'].clear()
                                    cross_data['free_cords'].clear()
                                    cross_data['free_cords'].append([coord[0], coord[1]])
                                    cross_data['free_num'] += 1
                                else:
                                    cross_data['cords'].clear()
                                    cross_data['free_cords'].clear()
                            except IndexError:
                                break
                            coord[0] += d[0]
                            coord[1] += d[1]
                            if (row_len - board_props['num']) >= 1:
                                len_to_react = 2
                            else:
                                len_to_react = 1
                            if len(cross_data['cords']) >= board_props['num'] - len_to_react and cross_data['free_num'] >= (board_props['num'] - len(cross_data['cords'])):
                                if len(cross_data['free_cords']) > 0:
                                    row = cross_data['free_cords'][0][0]
                                    col = cross_data['free_cords'][0][1]
                                    if len(cross_data['cords']) > best_move['num']:
                                        best_move['free_cords'] = [row, col]
                                        best_move['num'] = len(cross_data['cords'])
                                    #return row, col                                  

                        #else:
                        cross_data['cords'].clear()
                        cross_data['free_cords'].clear()
                        cross_data['free_num'] = 0
                except KeyError:
                    pass
            
        print(best_move)
        if best_move['num'] > 0:
            return best_move['free_cords'][0], best_move['free_cords'][1]
    
    if player['level'] == "Hard" and row_len == 3:
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
    board[row][col] = f"{player['color']}{player['mark']}{WHITE}"


def has_won(board, player, board_props):
    row_len = len(board[0])
    col_len = len(board)

    row = []
    for row_index in range(row_len):
        for col_index in range(col_len):
            if player['mark'] in board[row_index][col_index]:
                try:
                    if row[-1][0] == row_index and row[-1][1] == col_index - 1:
                        row.append([row_index, col_index])
                    else:
                        row.clear()
                except IndexError:
                    row.append([row_index, col_index])
        if len(row) == board_props['num']:
            for cord in row:
                board[cord[0]][cord[1]] = f"{GREEN}{player['mark']}{WHITE}"
            player['points'] += 1
            return True
        row.clear()
    col = []
    for col_index in range(col_len):
        for row_index in range(row_len):
            if player['mark'] in board[row_index][col_index]:
                try:
                    if col[-1][0] == row_index - 1 and col[-1][1] == col_index:
                        col.append([row_index, col_index])
                    else:
                        col.clear()
                except IndexError:
                    col.append([row_index, col_index])
        if len(col) == board_props['num']:
            for cord in col:
                board[cord[0]][cord[1]] = f"{GREEN}{player['mark']}{WHITE}"
            player['points'] += 1
            return True
        else:
            col.clear()

    direct = {}
    for i in range(row_len):
        if (row_len - i) > board_props['num'] - 1: # 3 - liczba znaków aby wygrać
            try:
                direct[i].append(1)
            except KeyError:
                direct[i] = [1]
        if (i + 1) >= board_props['num']:
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
                        if player['mark'] in board[coord[0]][coord[1]]:
                            cross.append([coord[0], coord[1]])
                        else:
                            cross.clear()
                    except IndexError:
                        break
                    coord[0] += d[0]
                    coord[1] += d[1]
                    if len(cross) == board_props['num']:
                        for cord in cross:
                            board[cord[0]][cord[1]] = f"{GREEN}{player['mark']}{WHITE}"
                        player['points'] += 1
                        return True
                    if coord[0] < 0 or coord[1] < 0:
                        break
                
                cross.clear()
        except KeyError:
            pass

    cross = []
    for col_index in range(1, col_len):
        try:
            for col_d in direct[col_index]:
                d = [-1, col_d]
                coord = [row_len - 1, col_index] # test od ostatniego wiersza i drugiej kolumny
                while True:
                    try:
                        if player['mark'] in board[coord[0]][coord[1]]:
                            cross.append([coord[0], coord[1]])                            
                        else:
                            cross.clear()
                    except IndexError:
                        break
                    coord[0] += d[0]
                    coord[1] += d[1]
                    if len(cross) == board_props['num']:
                        for cord in cross:
                            board[cord[0]][cord[1]] = f"{GREEN}{player['mark']}{WHITE}"
                        player['points'] += 1
                        return True
                    if coord[0] < 0 or coord[1] < 0:
                        break
                
                cross.clear()
        except KeyError:
            pass
    
    cross = []
    for row_index in range(1, row_len):
        try:
            for row_d in direct[row_index]:
                d = [row_d, 1]
                coord = [row_index, 0] # test od ostatniego wiersza i drugiej kolumny
                while True:
                    try:
                        if player['mark'] in board[coord[0]][coord[1]]:
                            cross.append([coord[0], coord[1]])
                            
                        else:
                            cross.clear()
                    except IndexError:
                        break
                    coord[0] += d[0]
                    coord[1] += d[1]
                
                    if len(cross) == board_props['num']:
                        for cord in cross:
                            board[cord[0]][cord[1]] = f"{GREEN}{player['mark']}{WHITE}"
                        player['points'] += 1
                        return True
                    if coord[0] < 0 or coord[1] < 0:
                        break
                cross.clear()
        except KeyError:
            pass
    

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


def print_board_(board):
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

def print_board(board, player1, player2):
    """Prints a 3-by-3 board on the screen with borders."""
    row_len = len(board[0])
    col_len = len(board)
    rows_template = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
    cols = []
    for col_index in range(col_len):
        cols.append(col_index + 1)
    cols_str = list(map(str, cols))
    rows = []
    for row_index in range(row_len):
        rows.append(rows_template[row_index])
    line = []
    for i in range(row_len):
        line.append("---")
    
    board_total_length = (row_len * 3) + (row_len - 1) + 2
    score_names = f"{player1['name']} : {player2['name']}"
    score = f"{str(player1['points']).rjust(len(player1['name']))} : {player2['points']}"
    score_offset = int((board_total_length - len(score_names)) / 2)
    print(" "*score_offset + score_names)
    print(" "*score_offset + score)
    print("")
    print("  ", "   ".join(cols_str))
    for index in range(col_len):
        print(f"{rows[index]}  {' | '.join(board[index])}")
        if index < row_len - 1:
            print(" ", "+".join(line))
    print("")
    

def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == "tie":
        print("It's a tie!")
    else:
        print(f"{winner} has won!")


def tictactoe_game(board_props, mode, player1, player2):
    board = init_board(int(board_props['size']))
    if mode == 'HUMAN-HUMAN':
        # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
        loop = True
        while loop:
            #clear()
            print_board(board, player1, player2)
            row, col = get_move(board, player1)
            mark(board, player1, row, col)
            if has_won(board, player1, board_props):
                winner = player1['mark']
                #clear()
                print_board(board, player1, player2)
                print_result(winner)
                loop = False
                next_game_question(board_props, mode, player1, player2)
                #continue
            elif is_full(board):
                winner = 'tie'
                #clear()
                print_board(board, player1, player2)
                print_result(winner)
                loop = False
                next_game_question(board_props, mode, player1, player2)
                #continue
            #clear()
            print_board(board, player1, player2)
            row, col = get_move(board, player2)
            mark(board, player2, row, col)
            if has_won(board, player2, board_props):
                winner = player2['mark']
                #clear()
                print_board(board, player1, player2)
                print_result(winner)
                loop = False
                next_game_question(board_props, mode, player1, player2)
                #continue
            elif is_full(board):
                winner = 'tie'
                #clear()
                print_board(board, player1, player2)
                print_result(winner)
                loop = False
                next_game_question(board_props, mode, player1, player2)
                #continue
    elif mode == 'HUMAN-AI' or mode == 'AI-HUMAN':
        # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
        loop = True
        if mode == 'HUMAN-AI':
            get_move_first = get_move
            get_move_second = get_ai_move
        else:
            get_move_first = get_ai_move
            get_move_second = get_move

        while loop:
            #clear()
            print_board(board, player1, player2)
            row, col = get_move_first(board, player1, board_props)
            mark(board, player1, row, col)
            if has_won(board, player1, board_props):
                winner = player1['mark']
                #clear()
                print_board(board, player1, player2)
                print_result(winner)
                loop = False
                next_game_question(board_props, mode, player1, player2)
                #continue
            elif is_full(board):
                winner = 'tie'
                #clear()
                print_board(board, player1, player2)
                print_result(winner)
                loop = False
                next_game_question(board_props, mode, player1, player2)
                #continue
            #clear()
            print_board(board, player1, player2)
            output = get_move_second(board, player2, board_props)
            print(output)
            row, col = output
            mark(board, player2, row, col)
            if has_won(board, player2, board_props):
                winner = player2['mark']
                #clear()
                print_board(board, player1, player2)
                print_result(winner)
                loop = False
                next_game_question(board_props, mode, player1, player2)
                #continue
            elif is_full(board):
                winner = 'tie'
                #clear()
                print_board(board, player1, player2)
                print_result(winner)
                loop = False
                next_game_question(board_props, mode, player1, player2)
                #continue
    elif mode == 'AI-AI':
        loop = True
        while loop:
            clear()
            print_board(board, player1, player2)
            row, col = get_ai_move(board, player1, board_props)
            mark(board, player1, row, col)
            if has_won(board, player1, board_props):
                winner = player1['mark']
                clear()
                print_board(board, player1, player2)
                print_result(winner)
                loop = False
                next_game_question(board_props, mode, player1, player2)
                #continue
            elif is_full(board):
                winner = 'tie'
                clear()
                print_board(board, player1, player2)
                print_result(winner)
                loop = False
                next_game_question(board_props, mode, player1, player2)
                #continue
            time.sleep(1)
            clear()
            print_board(board, player1, player2)
            row, col = get_ai_move(board, player2, board_props)
            mark(board, player2, row, col)
            time.sleep(1)
            if has_won(board, player2, board_props):
                winner = player2['mark']
                clear()
                print_board(board, player1, player2)
                print_result(winner)
                loop = False
                next_game_question(board_props, mode, player1, player2)
                #continue
            elif is_full(board):
                winner = 'tie'
                clear()
                print_board(board, player1, player2)
                print_result(winner)
                loop = False
                next_game_question(board_props, mode, player1, player2)
                #continue



def next_game_question(board_props, mode, player1, player2):
    user_input = None
    if user_input is None:
        user_input = input("Next game? [y]yes, [n]no: ")
        if user_input not in ['y', 'n', 'quit']:
            user_input = None
        elif user_input == 'y':
            tictactoe_game(board_props, mode, player1, player2)
        elif user_input == 'n':
            main_menu()
        elif user_input == 'quit':
            print("Good bye!")
            exit()

def main_menu():
#    tictactoe_game('HUMAN-HUMAN')
    board_props, game_mode, player1, player2 = menu.main_menu(clear)
    tictactoe_game(board_props, game_mode, player1, player2)
    #tictactoe_game('HUMAN-AI')


if __name__ == '__main__':
    main_menu()


#print(has_won(init_board(), {'mark': 'X'}))