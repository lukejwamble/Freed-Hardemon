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

    # Gets player's Hardemons
    player1_hardemon = hardemons_class.tjkirk
    player2_hardemon = hardemons_class.davidshannon

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
        print(f'{first.name}\'s Available Moves: {first.moves[0]} | {first.moves[1]} | {first.moves[2]} | {first.moves[3]}')
        first_action = input()
        if first_action == "Tackle":
            first_move = moves.Tackle
        elif first_action == "Punch":
            first_move = moves.Punch
        elif first_action == "Kick":
            first_move = moves.Kick
        else:
            first_move = moves.Special

        # Second Player Move Selection
        print(f'\nPick your move!')
        print(f'{second.name}\'s Available Moves: {second.moves[0]} | {first.moves[1]} | {first.moves[2]} | {first.moves[3]}')
        second_action = input()
        if second_action == "Tackle":
            second_move = moves.Tackle
        elif second_action == "Punch":
            second_move = moves.Punch
        elif first_action == "Kick":
            second_move = moves.Kick
        else:
            second_move = moves.Special
            

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

        # Reiterates the loop until battlen_ended = True
        continue
            