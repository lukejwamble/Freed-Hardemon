import damage
import hardemons_class

battle_ended = False

def Begin():
    #Introduction
    print("It's time to play: Freed-Hardemon!!! \n    Player 1, what is your name?")
    player1 = input()
    print(f'\nExcellent! Player 2, what is your name?')
    player2 = input()
    print(f'\nToday\'s battlers will be: \n    {player1} vs. {player2}')
    Selection(player1, player2)

def Selection(player1, player2):
    #Hardemon Selection
    p1team = []
    p2team = []
    hardemonlist = ["David Shannon", "TJ Kirk", "Lacy Crowell", 
                    "Kenan Casey", "Lisa Raine", "Jared Collins", 
                    "David Tidwell", "Doug Burleson", "Donnie DeBord",
                    "Jim Gardner"]
    
    print("\nThe Hardemon available for battle include:\n")
    for i in hardemonlist:
        print(i)
    print("\n")

    print(f'{player1}, pick your first Hardemon! Then {player2}, pick your first Hardemon!')
    p1first = input()
    p2first = input()
    p1team.append(p1first)
    hardemonlist.remove(p1first)
    p2team.append(p2first)
    hardemonlist.remove(p2first)
    print("\nThe remaining Hardemon available for battle include:\n")
    for i in hardemonlist:
        print(i)
    print("\n")

    print(f'{player2}, pick your second Hardemon! Then {player1}, pick your second Hardemon!')
    p2second = input()
    p1second = input()
    p2team.append(p2second)
    hardemonlist.remove(p2second)
    p1team.append(p1second)
    hardemonlist.remove(p1second)
    print("\nThe remaining Hardemon available for battle include:\n")
    for i in hardemonlist:
        print(i)
    print("\n")

    print(f'{player1}, pick your final Hardemon! Then {player2}, pick your final Hardemon!')
    p1third = input()
    p2third = input()
    p1team.append(p1third)
    hardemonlist.remove(p1third)
    p2team.append(p2third)
    hardemonlist.remove(p2third)

    Battle(player1, player2, p1team, p2team)

def Battle(player1, player2, p1team, p2team):
    pass