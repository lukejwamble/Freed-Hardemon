import moves
from termcolor import colored, cprint

class Hardemon():
    def __init__(self):
        self.name = "Unknown"
        self.id = 0
        self.max_health = 0
        self.health = 0
        self.attack = 0
        self.defense = 0
        self.speed = 0
        self.moves = []

davidshannon = Hardemon()
davidshannon.name = colored("David Shannon", "red")
davidshannon.id = 1
davidshannon.max_health = 95
davidshannon.health = 95
davidshannon.attack = 95
davidshannon.defense = 95
davidshannon.speed = 115
davidshannon.moves = [moves.Tackle, moves.Punch, moves.Kick, moves.Day_of_Giving]

tjkirk = Hardemon()
tjkirk.name = colored("TJ Kirk", "black")
tjkirk.id = 2
tjkirk.max_health = 140
tjkirk.health = 140
tjkirk.attack = 60
tjkirk.defense = 150
tjkirk.speed = 50
tjkirk.moves = [moves.Tackle, moves.Punch, moves.Kick, moves.Gano_Menu]


lacycrowell = Hardemon()
lacycrowell.name = colored("Lacy Crowell", "green")
lacycrowell.id = 3
lacycrowell.max_health = 125
lacycrowell.health = 125
lacycrowell.attack = 175
lacycrowell.defense = 75
lacycrowell.speed = 25
lacycrowell.moves = [moves.Tackle, moves.Punch, moves.Kick, moves.Black_Belt]

kenancasey = Hardemon()
kenancasey.name = colored("Kenan Casey", "yellow")
kenancasey.id = 4
kenancasey.max_health = 90
kenancasey.health = 90
kenancasey.attack = 120
kenancasey.defense = 105
kenancasey.speed = 85
kenancasey.moves = [moves.Tackle, moves.Punch, moves.Kick, moves.Meme]

lisaraine = Hardemon()
lisaraine.name = colored("Lisa Raine", "magenta")
lisaraine.id = 5
lisaraine.max_health = 85
lisaraine.health = 85
lisaraine.attack = 120
lisaraine.defense = 78
lisaraine.speed = 117
lisaraine.moves = [moves.Tackle, moves.Punch, moves.Kick, moves.No_Move_Given]

jaredcollins = Hardemon()
jaredcollins.name = colored("Jared Collins", "blue")
jaredcollins.id = 6
jaredcollins.max_health = 100
jaredcollins.health = 100
jaredcollins.attack = 110
jaredcollins.defense = 55
jaredcollins.speed = 135
jaredcollins.moves = [moves.Tackle, moves.Punch, moves.Kick, moves.Dry_Erase_Marker]

davidtidwell = Hardemon()
davidtidwell.name = colored("David Tidwell", "cyan")
davidtidwell.id = 7
davidtidwell.max_health = 100
davidtidwell.health = 100
davidtidwell.attack = 85
davidtidwell.defense = 160
davidtidwell.speed = 55
davidtidwell.moves = [moves.Tackle, moves.Punch, moves.Kick, moves.Horrible_Test_Answer]

dougburleson = Hardemon()
dougburleson.name = colored("Doug Burleson", "white")
dougburleson.id = 8
dougburleson.max_health = 120
dougburleson.health = 120
dougburleson.attack = 75
dougburleson.defense = 120
dougburleson.speed = 75
dougburleson.moves = [moves.Tackle, moves.Punch, moves.Kick, moves.Greek_Translation]

donniedebord = Hardemon()
donniedebord.name = colored("Donnie DeBord", "light_yellow")
donniedebord.id = 9
donniedebord.max_health = 75
donniedebord.health = 75
donniedebord.attack = 120
donniedebord.defense = 75
donniedebord.speed = 120
donniedebord.moves = [moves.Tackle, moves.Punch, moves.Kick, moves.Right_Doctrine]

jimgardner = Hardemon()
jimgardner.name = colored("Jim Gardner", "red", attrs=["bold"])
jimgardner.id = 10
jimgardner.max_health = 25
jimgardner.health = 25
jimgardner.attack = 150
jimgardner.defense = 25
jimgardner.speed = 200
jimgardner.moves = [moves.Tackle, moves.Punch, moves.Kick, moves.Dog_Attack]

hardemon_list = [davidshannon, tjkirk, lacycrowell,
                 kenancasey, lisaraine, jaredcollins, 
                 davidtidwell, dougburleson, donniedebord, 
                 jimgardner]