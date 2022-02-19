# Py Pac Poe

# variables

from re import X


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
