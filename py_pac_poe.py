# Py Pac Poe

# variables

player = ""

boardDictionary = {
    "a1": "", "a2": "", "a3": "",
    "b1": "", "b2": "", "b3": "",
    "c1": "", "c2": "", "c3": ""
}

# functions

def startGame():

    global player

    print('''
    ----------------------
    Let's play Py Pac Poe!
    ----------------------
    ''')
    playerChoice = input("Choose your player (X or O): ")
    player = playerChoice

def board():

    global boardDictionary

    print(f'''
       A   B   C
    1) {boardDictionary["a1"]}  |  {boardDictionary["b1"]} |  {boardDictionary["c1"]}
    -------------
    2) {boardDictionary["a2"]}  | {boardDictionary["b2"]}  | {boardDictionary["c2"]}
    -------------
    3) {boardDictionary["a3"]}  | {boardDictionary["b3"]}  | {boardDictionary["c3"]}
    ''')
