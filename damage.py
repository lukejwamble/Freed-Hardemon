import hardemons_class
import random

def damageCalc(attacker, defender, attackermove):

    # Accuarcy Check
    attack_hit = False
    accuracy_check = random.randrange(1, 100)
    if accuracy_check > attackermove.accuracy:
        attack_hit = False
    else: attack_hit = True

    # If Miss
    if attack_hit == False:
        print(f'\n{attacker.name}\'s move missed {defender.name}!!!')
    
    # else Hit
    else:
        # Damage calculation
        damage = round(((attackermove.damage * (attacker.attack/defender.defense)) * random.uniform(0.80, 1.00)))
        defender.health -= damage

        # Prints how much damage was dealt
        print(f'\n{attacker.name} did {damage} damage to {defender.name}!!!')



#   Theoretical Damage Calculator

# A = AttackerAttackPoints
# D = DefenderDefensePoints
# M = MoveAttackPoints

# ( M * A/D ) * 0.80~1.00