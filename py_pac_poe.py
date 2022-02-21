# Py Pac Poe

# variables

player = ""

board_dictionary = {
    "a1": "", "a2": "", "a3": "",
    "b1": "", "b2": "", "b3": "",
    "c1": "", "c2": "", "c3": ""
}

# determines last round for player when other player already has won (their final chance to tie the game)
# see determines_win function below
last_round = False

# functions

def start_game():

    global player

    print('''
    ----------------------
    Let's play Py Pac Poe!
    ----------------------
    ''')

    # which player will user start with
    player_choice = input("Choose your player (X or O): ").upper()

    if player_choice == "X" or player_choice == "O":
        player = player_choice
    else:
        print(f"{player_choice} is not a valid choice. Please choose X or O.")
        start_game()

def board():

    global board_dictionary

    # visual game board
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

    # if X has won
    if (board_dictionary["a1"] == "X" and board_dictionary["b1"] == "X" and board_dictionary["c1"] == "X") or (board_dictionary["a2"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["c2"] == "X") or (board_dictionary["a3"] == "X" and board_dictionary["b3"] == "X" and board_dictionary["c3"] == "X") or (board_dictionary["a1"] == "X" and board_dictionary["a2"] == "X" and board_dictionary["a3"] == "X") or (board_dictionary["b1"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["b3"] == "X") or (board_dictionary["c1"] == "X" and board_dictionary["c2"] == "X" and board_dictionary["c3"] == "X") or (board_dictionary["a1"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["c3"] == "X") or (board_dictionary["a3"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["c1"] == "X"):
        # if O has also won
        if (board_dictionary["a1"] == "O" and board_dictionary["b1"] == "O" and board_dictionary["c1"] == "O") or (board_dictionary["a2"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["c2"] == "O") or (board_dictionary["a3"] == "O" and board_dictionary["b3"] == "O" and board_dictionary["c3"] == "O") or (board_dictionary["a1"] == "O" and board_dictionary["a2"] == "O" and board_dictionary["a3"] == "O") or (board_dictionary["b1"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["b3"] == "O") or (board_dictionary["c1"] == "O" and board_dictionary["c2"] == "O" and board_dictionary["c3"] == "O") or (board_dictionary["a1"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["c3"] == "O") or (board_dictionary["a3"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["c1"] == "O"):
                board()
                print("There is a tie!")
                return
        else:
            # X has won, and O has chosen a cell that will not tie the game --> X wins
            if last_round == True:
                board()
                print("X wins!")
                return
            # X has won but O has not, so the next round will be O's last chance to tie the game (last_round now equals True)
            else:
                last_round = True
                toggle_player()
                round()
    # if O has won
    elif (board_dictionary["a1"] == "O" and board_dictionary["b1"] == "O" and board_dictionary["c1"] == "O") or (board_dictionary["a2"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["c2"] == "O") or (board_dictionary["a3"] == "O" and board_dictionary["b3"] == "O" and board_dictionary["c3"] == "O") or (board_dictionary["a1"] == "O" and board_dictionary["a2"] == "O" and board_dictionary["a3"] == "O") or (board_dictionary["b1"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["b3"] == "O") or (board_dictionary["c1"] == "O" and board_dictionary["c2"] == "O" and board_dictionary["c3"] == "O") or (board_dictionary["a1"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["c3"] == "O") or (board_dictionary["a3"] == "O" and board_dictionary["b2"] == "O" and board_dictionary["c1"] == "O"):
        # if X has also won
        if (board_dictionary["a1"] == "X" and board_dictionary["b1"] == "X" and board_dictionary["c1"] == "X") or (board_dictionary["a2"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["c2"] == "X") or (board_dictionary["a3"] == "X" and board_dictionary["b3"] == "X" and board_dictionary["c3"] == "X") or (board_dictionary["a1"] == "X" and board_dictionary["a2"] == "X" and board_dictionary["a3"] == "X") or (board_dictionary["b1"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["b3"] == "X") or (board_dictionary["c1"] == "X" and board_dictionary["c2"] == "X" and board_dictionary["c3"] == "X") or (board_dictionary["a1"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["c3"] == "X") or (board_dictionary["a3"] == "X" and board_dictionary["b2"] == "X" and board_dictionary["c1"] == "X"):
                board()
                print("There is a tie!")
                return
        else:
            # O has won, and X has chosen a cell that will not tie the game --> O wins
            if last_round == True:
                board()
                print("O wins!")
                return
            # O has won but X has not, so the next round will be X's last chance to tie the game (last_round now equals True)
            else:
                last_round = True
                toggle_player()
                round()
    # if the board's cells are taken up but no one has won
    elif "" not in board_dictionary.values():
        board()
        print("Game over, try again.")
    # toggle player and continue game
    else:
        toggle_player()
        round()

def round():

    global player
    global board_dictionary

    board()

    # player chooses cell on board (turn)
    player_cell = input(f'Player {player}, choose your cell on the board (ex: B2): ').lower()

    # if player chooses cell that does not exist
    if (player_cell not in board_dictionary):
        print(f"{player_cell} is not a valid choice. Please check the board choices and try again.")
        round()
    # if player chooses a cell that is already taken
    elif (board_dictionary[player_cell] != ""):
        print(f"{player_cell} is already taken. Please try again.")
        round()
    # take player cell choice and put it on the board
    else:
        board_dictionary[player_cell] = player

    # win/tie/game over logic
    determine_win()

# toggles player before each round
def toggle_player():

    global player

    if player == "X":
        player = "O"
    else:
        player = "X"

# start py pac poe
start_game()
round()