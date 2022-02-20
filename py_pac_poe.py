# Py Pac Poe

# variables

from re import X


player = ""

board_dictionary = {
    "a1": "", "a2": "", "a3": "",
    "b1": "", "b2": "", "b3": "",
    "c1": "", "c2": "", "c3": ""
}

# functions

def start_game():

    global player

    print('''
    ----------------------
    Let's play Py Pac Poe!
    ----------------------
    ''')
    player_choice = input("Choose your player (X or O): ").upper()
    player = player_choice

def board():

    global board_dictionary

    print(f'''
       A   B   C
    1) {board_dictionary["a1"]}  | {board_dictionary["b1"]}  |  {board_dictionary["c1"]}
    -------------
    2) {board_dictionary["a2"]}  | {board_dictionary["b2"]}  | {board_dictionary["c2"]}
    -------------
    3) {board_dictionary["a3"]}  | {board_dictionary["b3"]}  | {board_dictionary["c3"]}
    ''')

def determine_win():

    global player
    global board_dictionary

    if (board_dictionary["a1"] == player and board_dictionary["b1"] == player and board_dictionary["c1"] == player) or (board_dictionary["a2"] == player and board_dictionary["b2"] == player and board_dictionary["c2"] == player) or (board_dictionary["a3"] == player and board_dictionary["b3"] == player and board_dictionary["c3"] == player) or (board_dictionary["a1"] == player and board_dictionary["a2"] == player and board_dictionary["a3"] == player) or (board_dictionary["b1"] == player and board_dictionary["b2"] == player and board_dictionary["b3"] == player) or (board_dictionary["c1"] == player and board_dictionary["c2"] == player and board_dictionary["c3"] == player) or (board_dictionary["a1"] == player and board_dictionary["b2"] == player and board_dictionary["c3"] == player) or (board_dictionary["a3"] == player and board_dictionary["b2"] == player and board_dictionary["c1"] == player):
        board()
        print(f"{player} wins!")
        return
    else:
        toggle_player()
        round()

    # if (board_dictionary["a1"] == player) and (board_dictionary["b1"] == player) and (board_dictionary["c1"] == player):
    #     print(f"{player} wins!")
    #     return
    # elif (board_dictionary["a2"] == player) and (board_dictionary["b2"] == player) and (board_dictionary["c2"] == player):
    #     print(f"{player} wins!")
    #     return
    # elif (board_dictionary["a3"] == player) and (board_dictionary["b3"] == player) and (board_dictionary["c3"] == player):
    #     print(f"{player} wins!")
    #     return
    # elif (board_dictionary["a1"] == player) and (board_dictionary["a2"] == player) and (board_dictionary["a3"] == player):
    #     print(f"{player} wins!")
    #     return
    # elif (board_dictionary["b1"] == player) and (board_dictionary["b2"] == player) and (board_dictionary["b3"] == player):
    #     print(f"{player} wins!")
    #     return
    # elif (board_dictionary["c1"] == player) and (board_dictionary["c2"] == player) and (board_dictionary["c3"] == player):
    #     print(f"{player} wins!")
    #     return
    # elif (board_dictionary["a1"] == player) and (board_dictionary["b2"] == player) and (board_dictionary["c3"] == player):
    #     print(f"{player} wins!")
    #     return
    # elif (board_dictionary["c1"] == player) and (board_dictionary["b2"] == player) and (board_dictionary["a3"] == player):
    #     print(f"{player} wins!")
    #     return
    # else:
    #     toggle_player()
    #     round()

def round():

    global player
    global board_dictionary

    board()

    player_cell = input(f'Player {player}, choose your cell on the board (ex: B2): ').lower()
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