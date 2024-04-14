import hardemons_class
import damage
import moves
from termcolor import colored, cprint

def Begin():
    battle_ended = False

    # Gets player names
    print('\nPlayer 1, what is your name?')
    player1 = colored(input(), "red")
    print('Player 2, what is your name?')
    player2 = colored(input(), "cyan")
    print("")

    # Gets player's Hardemons
    player1_hardemon = None
    player2_hardemon = None
    # Prints list of available hardemon
    increment = 1
    for i in hardemons_class.hardemon_list:
        print(f'{increment}: {i.name}')
        increment += 1

    # Loop to make sure that player1 selection is valid
    player1_check = False
    while player1_check == False:
        print(f'\n{player1}, select your Hardemon!')
        player1_pick = int(input())
        if player1_pick > 0 and player1_pick <= 10:
            for i in hardemons_class.hardemon_list:
                if player1_pick == i.id:
                    player1_hardemon = i
                    player1_check = True
        else:
            continue

    # Loop to make sure that player2 selection is valid
    player2_check = False
    while player2_check == False:
        print(f'\n{player2}, select your Hardemon!')
        player2_pick = int(input())
        if player2_pick > 0 and player2_pick <= 10:
            for i in hardemons_class.hardemon_list:
                if player2_pick == i.id:
                    player2_hardemon = i
                    player2_check = True
        else:
            continue

    print(f'\nToday\'s fighters are {player1} and {player2}. \n')
    print(f'{player1} will be fighting with {player1_hardemon.name}. {player2} will be fighting with {player2_hardemon.name}.')
    
    while battle_ended == False:

        # Determines which player will go first
        if player1_hardemon.speed > player2_hardemon.speed:
            first = player1_hardemon
            second = player2_hardemon
        else:
            first = player2_hardemon
            second = player1_hardemon

        # Prints health at the start of each turn
        print(f'\nIn Battle: \n{first.name} | Health: {first.health}/{first.max_health} \n{second.name} | Health: {second.health}/{second.max_health}')

        # First Player Move Selection
        print(f'\nPick your move!')
        print(f'{first.name}\'s Available Moves: {first.moves[0].name} | {first.moves[1].name} | {first.moves[2].name} | {first.moves[3].name}')
        first_action = input()

        for i in first.moves:
            if i.name == first_action:
                first_move = i
     
        # Second Player Move Selection
        print(f'\nPick your move!')
        print(f'{second.name}\'s Available Moves: {second.moves[0].name} | {first.moves[1].name} | {first.moves[2].name} | {first.moves[3].name}')
        second_action = input()
        for i in second.moves:
            if i.name == second_action:
                second_move = i
            

        # First Player Damage Calculation
        damage.damageCalc(player1_hardemon, player2_hardemon, first_move)
        if second.health <= 0:
            print(f'\nPlayer 1 Wins!!!')
            battle_ended = True
        
        # Second Player Damage Calculation
        else:
            damage.damageCalc(player2_hardemon, player1_hardemon, second_move)
            if first.health <= 0:
                print(f'\nPlayer 2 Wins!!!')
                battle_ended = True

        # Reiterates the loop until battle_ended = True
        continue
            