WHITE = "\033[0m"
RED = "\033[31m"
YELLOW = "\033[33m"
BLUE = "\033[34m"


def main_menu(clear):
    board_props = {
        'size': 3,
        'num': 3
    }
    game_mode = 'HUMAN-AI'
    user_input = None
    game_mode_dict = {
        'HUMAN-AI': 'Human vs. Computer',
        'AI-HUMAN': 'Computer vs. Human',
        'HUMAN-HUMAN': 'Human vs. Human',
        'AI-AI': 'Computer vs. Computer'
    }
    msg = ""
    while user_input is None:
        clear()
        print("MENU")
        print(f"1. Board properties: {board_props['size']}x{board_props['size']}")
        print(f"2. Game mode: {game_mode_dict[game_mode]}")
        print("3. Next step")
        print(msg)
        msg = ""
        user_input = input("> ")
        if user_input == 'quit':
            print("Good bye!")
            exit()
        elif not user_input.isdigit():
            msg = "Please, input a digit: 1, 2, or 3"
            user_input = None
            continue
        elif int(user_input) not in [1, 2, 3]:
            msg = "Please, input a digit: 1, 2, or 3"
            user_input = None
            continue
        elif user_input == '1':
            board_properties(clear, board_props)
            user_input = None
        elif user_input == '2':
            game_mode = get_game_mode(clear)
            user_input = None
        elif user_input == '3':
            player1, player2 = game_properties(game_mode, clear)
    return board_props, game_mode, player1, player2


def get_board_size(clear, board_props):
    board_size = None
    msg = ""
    while board_size is None:
        clear()
        print("MENU->Board size")
        print("Please, input a single digit from 3 to 9 that corresponds to the number of rows and columns.")
        print("Example: user input: 3 corresponds to the board size: 3x3")
        print(msg)
        msg = ""
        board_size = input("> ")
        if board_size == 'quit':
            print("Good bye!")
            exit()
        elif not board_size.isdigit():
            msg = "Please, input a digit within a range from 3 to 9"
            board_size = None
        elif int(board_size) not in range(3, 10):
            msg = "Please, input a digit within a range from 3 to 9"
            board_size = None
    board_props['size'] = int(board_size)

def board_properties(clear, board_props):
    user_input = None
    msg = ""
    while user_input is None:
        clear()
        print("MENU->Board properties")
        print(f"1. Board size: {board_props['size']}x{board_props['size']}")
        print(f"2. Number of marks to win: {board_props['num']}")
        print("3. Back")
        print(msg)
        msg = ""
        user_input = input("> ")
        if user_input == 'quit':
            print("Good bye!")
            exit()
        elif not user_input.isdigit():
            msg = "Please, input a digit (1 or 2)."
            user_input = None
        elif int(user_input) not in range(1, 4):
            msg = "Please, input a digit (1 or 2)."
            user_input = None
        elif user_input == '1':
            get_board_size(clear, board_props)
            user_input = None
        elif user_input == '2':
            get_number_marks(clear, board_props)
            user_input = None
        elif user_input == '3':
            pass

def get_number_marks(clear, board_props):
    user_input = None
    msg = ""
    min = 3
    max = (board_props['size'] - min) + min
    while user_input is None:
        clear()
        print("MENU->Board properties->Number of marks")
        print(msg)
        user_input = input(f"Number of marks to win (choose between {min}-{max}): ")
        if user_input == 'quit':
            print("Good bye!")
            exit()
        elif not user_input.isdigit():
            msg = f"Please, input a digit (choose between {min}-{max})."
            user_input = None
        elif int(user_input) not in range(min, max + 1):
            msg = f"Please, input a digit (choose between {min}-{max})."
            user_input = None
    board_props['num'] = int(user_input)

def get_game_mode(clear):
    game_mode_dict = {
        '1': 'HUMAN-HUMAN',
        '2': 'HUMAN-AI',
        '3': 'AI-HUMAN',
        '4': 'AI-AI'
    }
    get_game_mode = None
    msg = ""
    while get_game_mode is None:
        clear()
        print("MENU->Game mode")
        print("Please, input a digit (1, 2, 3 or 4) that corresponds to the chosen game mode.")
        print("1. Human vs. Human")
        print("2. Human vs. Computer")
        print("3. Computer vs. Human")
        print("4. Computer vs. Computer")
        print(msg)
        msg = ""
        get_game_mode = input("> ")
        if get_game_mode == 'quit':
            print("Good bye!")
            exit()
        elif not get_game_mode.isdigit():
            msg = "Please, input a digit: 1, 2, 3 or 4"
            get_game_mode = None
        elif int(get_game_mode) not in range(1, 5):
            msg = "Please, input a digit: 1, 2, 3 or 4"
            get_game_mode = None
    return game_mode_dict[get_game_mode]


def game_properties(game_mode, clear):
    
    if game_mode == 'HUMAN-HUMAN':
        player1 = {
            'name': 'Player1',
            'mark': 'X',
            'color': WHITE,
            'points': 0
        }
        player2 = {
            'name': 'Player2',
            'mark': 'O',
            'color': WHITE,
            'points': 0
        }
        user_input = None
        msg = ""
        while user_input is None:
            clear()
            print("MENU->Game properties")
            print("Please, input a digit (1, 2, 3 or 4) that corresponds to the chosen setting that you want change.")
            print(f"1. Player1 settings: {player1['name']} {player1['color']}{player1['mark']}{WHITE}")
            print(f"2. Player2 settings: {player2['name']} {player2['color']}{player2['mark']}{WHITE}")
            print("3. Back to menu")
            print("4. Start game")
            print(msg)
            msg = ""
            user_input = input("> ")
            if user_input == 'quit':
                print("Good bye!")
                exit()
            elif not user_input.isdigit():
                msg = "Please, input a digit: 1, 2, 3 or 4"
                user_input = None
                continue
            elif int(user_input) not in range(1, 5):
                msg = "Please, input a digit: 1, 2, 3 or 4"
                user_input = None
                continue
            elif user_input == '1':
                get_player_prop('Player1', player1, clear)
                user_input = None
            elif user_input == '2':
                get_player_prop('Player2', player2, clear)
                user_input = None
            elif user_input == '3':
                main_menu(clear)
                user_input = None
            elif user_input == '4':
                return player1, player2
    elif game_mode == 'HUMAN-AI' or game_mode == 'AI-HUMAN':
        player = {
            'name': 'Player',
            'mark': None,
            'color': WHITE,
            'points': 0
        }
        computer = {
            'name': 'Computer',
            'mark': None,
            'color': WHITE,
            'level': 'Medium',
            'points': 0
        }
        if game_mode == 'HUMAN-AI':
            player['mark'] = 'X'
            computer['mark'] = 'O'
        else:
            player['mark'] = 'O'
            computer['mark'] = 'X'
        
        user_input = None
        msg = ""
        while user_input is None:
            clear()
            print("MENU->Game properties")
            print("Please, input a digit (1, 2, 3 or 4) that corresponds to the chosen setting that you want change.")
            print(f"1. Player settings: {player['name']} {player['color']}{player['mark']}{WHITE}")
            print(f"2. Computer settings: {computer['name']} {computer['color']}{computer['mark']}{WHITE}")
            print("3. Back to menu")
            print("4. Start game")
            print(msg)
            msg = ""
            user_input = input("> ")
            if user_input == 'quit':
                print("Good bye!")
                exit()
            elif not user_input.isdigit():
                msg = "Please, input a digit: 1, 2, 3 or 4"
                user_input = None
                continue
            elif int(user_input) not in range(1, 5):
                msg = "Please, input a digit: 1, 2, 3 or 4"
                user_input = None
                continue
            elif user_input == '1':
                get_player_prop('Player', player, clear)
                user_input = None
            elif user_input == '2':
                get_player_prop('Computer', computer, clear)
                user_input = None
            elif user_input == '3':
                main_menu(clear)
                user_input = None
            elif user_input == '4':
                if game_mode == 'HUMAN-AI':
                    return player, computer
                else:
                    return computer, player
                
    elif game_mode == 'AI-AI':
        computer1 = {
            'name': 'Computer1',
            'mark': 'X',
            'color': WHITE,
            'level': 'Medium',
            'points': 0
        }
        computer2 = {
            'name': 'Computer2',
            'mark': 'O',
            'color': WHITE,
            'level': 'Medium',
            'points': 0
        }
        user_input = None
        msg = ""
        while user_input is None:
            clear()
            print("MENU->Game properties")
            print("Please, input a digit (1, 2, 3 or 4) that corresponds to the chosen setting that you want change.")
            print(f"1. Computer1 settings: {computer1['name']} {computer1['color']}{computer1['mark']}{WHITE}")
            print(f"2. Computer2 settings: {computer2['name']} {computer2['color']}{computer2['mark']}{WHITE}")
            print("3. Back to menu")
            print("4. Start game")
            print(msg)
            msg = ""
            user_input = input("> ")
            if user_input == 'quit':
                print("Good bye!")
                exit()
            elif not user_input.isdigit():
                msg = "Please, input a digit: 1, 2, 3 or 4"
                user_input = None
                continue
            elif int(user_input) not in range(1, 5):
                msg = "Please, input a digit: 1, 2, 3 or 4"
                user_input = None
                continue
            elif user_input == '1':
                get_player_prop('Computer1', computer1, clear)
                user_input = None
            elif user_input == '2':
                get_player_prop('Computer2', computer2, clear)
                user_input = None
            elif user_input == '3':
                main_menu(clear)
                user_input = None
            elif user_input == '4':
                return computer1, computer2


def get_player_prop(player_type, player, clear):
    user_input = None
    msg = ""
    if 'Player' in player_type:
        while user_input is None:
            clear()
            print(f"MENU->Game properties->{player_type} settings")
            print(f"1. {player_type}'s name: {player['name']}")
            print(f"2. {player_type}'s mark color: {player['color']}{player['mark']}{WHITE}")
            print("3. Back")
            print(msg)
            msg = ""
            user_input = input("> ")
            if user_input == 'quit':
                print("Good bye!")
                exit()
            elif not user_input.isdigit():
                msg = "Please, input a digit: 1, 2 or 3"
                user_input = None
            elif int(user_input) not in range(1, 4):
                msg = "Please, input a digit: 1, 2 or 3"
                user_input = None
            elif user_input == '1':
                player['name'] = get_player_name(clear)
                user_input = None
            elif user_input == '2':
                player['color'] = get_player_color(clear)
                user_input = None
            elif user_input == '3':
                pass
    elif 'Computer' in player_type:
        while user_input is None:
            clear()
            print(f"MENU->Game properties->{player_type} settings")
            print(f"1. {player_type}'s mark color: {player['color']}{player['mark']}{WHITE}")
            print(f"2. Level: {player['level']}")
            print("3. Back")
            print(msg)
            msg = ""
            user_input = input("> ")
            if user_input == 'quit':
                print("Good bye!")
                exit()
            elif not user_input.isdigit():
                msg = "Please, input a digit: 1, 2 or 3"
                user_input = None
            elif int(user_input) not in range(1, 4):
                msg = "Please, input a digit: 1, 2 or 3"
                user_input = None
            elif user_input == '1':
                player['color'] = get_player_color(clear)
                user_input = None
            elif user_input == '2':
                player['level'] = get_player_level(clear)
                user_input = None
            elif user_input == '3':
                pass


def get_player_level(clear):
    levels = {
        '1': 'Easy',
        '2': 'Medium',
        '3': 'Hard'
    }
    level = None
    msg = ""
    while level is None:
        clear()
        print("MENU->Game mode")
        print("Please, input a digit (1, 2, 3 or 4) that corresponds to the chosen game mode.")
        print("1. Easy")
        print("2. Medium")
        print("3. Hard")
        print(msg)
        msg = ""
        level = input("> ")
        if level == 'quit':
            print("Good bye!")
            exit()
        elif not level.isdigit():
            msg = "Please, input a digit: 1, 2 or 3"
            level = None
        elif int(level) not in range(1, 4):
            msg = "Please, input a digit: 1, 2 or 3"
            level = None
    return levels[level]

def get_player_name(clear):
    user_input = None
    msg = ""
    while user_input is None:
        clear()
        print("MENU->Game properties->Player1 settings->Name")
        print(msg)
        msg = ""
        user_input = input("Player's name: ")
        if user_input == 'quit':
            print("Good bye!")
            exit()
        elif len(user_input) < 3:
            msg = "Player's name should be at least 3-characters long"
            user_input = None
    return user_input

def get_player_color(clear):
    user_input = None
    msg = ""
    colors = {
        '1': RED,
        '2': BLUE,
        '3': YELLOW,
        '4': WHITE
    }
    while user_input is None:
        clear()
        print("MENU->Game properties->Player1 settings->Color")
        print(f"1. {RED}Red{WHITE}")
        print(f"2. {BLUE}Blue{WHITE}")
        print(f"3. {YELLOW}Yellow{WHITE}")
        print("4. White")
        print(msg)
        msg = ""
        user_input = input("Player's mark color: ")
        if user_input == 'quit':
            print("Good bye!")
            exit()
        elif not user_input.isdigit():
            msg = "Please, input a digit: 1, 2, 3 or 4"
            user_input = None
            continue
        elif int(user_input) not in range(1, 5):
            msg = "Please, input a digit: 1, 2, 3 or 4"
            user_input = None
            continue
    return colors[user_input]
