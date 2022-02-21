# Py Pac Poe

# variables

player = ""

board_dictionary = {
    "a1": "", "a2": "", "a3": "",
    "b1": "", "b2": "", "b3": "",
    "c1": "", "c2": "", "c3": ""
}

last_round = False

# functions

def start_game():

    global player

    print('''
    ----------------------
    Let's play Py Pac Poe!
    ----------------------
    ''')
    player_choice = input("Choose your player (X or O): ").upper()

    if player_choice == "X" or player_choice == "O":
        player = player_choice
    else:
        print(f"{player_choice} is not a valid choice. Please choose X or O.")
        start_game()

def board():

    global board_dictionary

    print(f'''
       A   B   C
    1) {board_dictionary["a1"]}  | {board_dictionary["b1"]}  | {board_dictionary["c1"]}
    -------------
    2) {board_dictionary["a2"]}  | {board_dictionary["b2"]}  | {board_dictionary["c2"]}
    -------------
    3) {board_dictionary["a3"]}  | {board_dictionary["b3"]}  | {board_dictionary["c3"]}
    ''')

def determine_win():

    global player
    global board_dictionary
    global last_round

    if (board_dictionary["a1"] == "X" and board_dictionary["b1"] == "X" and board_dictionary["c1"] == "X") or (board_dictionary["a2"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["c2"] == "X") or (board_dictionary["a3"] == "X" and board_dictionary["b3"] == "X" and board_dictionary["c3"] == "X") or (board_dictionary["a1"] == "X" and board_dictionary["a2"] == "X" and board_dictionary["a3"] == "X") or (board_dictionary["b1"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["b3"] == "X") or (board_dictionary["c1"] == "X" and board_dictionary["c2"] == "X" and board_dictionary["c3"] == "X") or (board_dictionary["a1"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["c3"] == "X") or (board_dictionary["a3"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["c1"] == "X"):
        if (board_dictionary["a1"] == "O" and board_dictionary["b1"] == "O" and board_dictionary["c1"] == "O") or (board_dictionary["a2"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["c2"] == "O") or (board_dictionary["a3"] == "O" and board_dictionary["b3"] == "O" and board_dictionary["c3"] == "O") or (board_dictionary["a1"] == "O" and board_dictionary["a2"] == "O" and board_dictionary["a3"] == "O") or (board_dictionary["b1"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["b3"] == "O") or (board_dictionary["c1"] == "O" and board_dictionary["c2"] == "O" and board_dictionary["c3"] == "O") or (board_dictionary["a1"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["c3"] == "O") or (board_dictionary["a3"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["c1"] == "O"):
                print("There is a tie!")
                return
        else:
            if last_round == True:
                print("X wins!")
                return
            else:
                last_round = True
                toggle_player()
                round()
    elif (board_dictionary["a1"] == "O" and board_dictionary["b1"] == "O" and board_dictionary["c1"] == "O") or (board_dictionary["a2"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["c2"] == "O") or (board_dictionary["a3"] == "O" and board_dictionary["b3"] == "O" and board_dictionary["c3"] == "O") or (board_dictionary["a1"] == "O" and board_dictionary["a2"] == "O" and board_dictionary["a3"] == "O") or (board_dictionary["b1"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["b3"] == "O") or (board_dictionary["c1"] == "O" and board_dictionary["c2"] == "O" and board_dictionary["c3"] == "O") or (board_dictionary["a1"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["c3"] == "O") or (board_dictionary["a3"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["c1"] == "O"):
        if (board_dictionary["a1"] == "X" and board_dictionary["b1"] == "X" and board_dictionary["c1"] == "X") or (board_dictionary["a2"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["c2"] == "X") or (board_dictionary["a3"] == "X" and board_dictionary["b3"] == "X" and board_dictionary["c3"] == "X") or (board_dictionary["a1"] == "X" and board_dictionary["a2"] == "X" and board_dictionary["a3"] == "X") or (board_dictionary["b1"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["b3"] == "X") or (board_dictionary["c1"] == "X" and board_dictionary["c2"] == "X" and board_dictionary["c3"] == "X") or (board_dictionary["a1"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["c3"] == "X") or (board_dictionary["a3"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["c1"] == "X"):
                print("There is a tie!")
                return
        else:
            if last_round == True:
                print("O wins!")
                return
            else:
                last_round = True
                toggle_player()
                round()
    else:
        toggle_player()
        round()

def round():

    global player
    global board_dictionary

    board()

    player_cell = input(f'Player {player}, choose your cell on the board (ex: B2): ').lower()

    if (player_cell not in board_dictionary):
        print(f"{player_cell} is not a valid choice. Please check the board choices and try again.")
        round()
    elif (board_dictionary[player_cell] != ""):
        print(f"{player_cell} is already taken. Please try again.")
        round()
    else:
        board_dictionary[player_cell] = player

    determine_win()

def toggle_player():

    global player

    if player == "X":
        player = "O"
    else:
        player = "X"

start_game()
round()