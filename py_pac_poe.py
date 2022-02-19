# Py Pac Poe

# variables

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
    player_choice = input("Choose your player (X or O): ")
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

def round():

    global player
    global board_dictionary

    board()

    player_cell = input(f'Player {player}, choose your cell on the board (ex: B2): ').lower()
    board_dictionary[player_cell] = player

