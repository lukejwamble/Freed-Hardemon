from termcolor import colored, cprint

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")

print_red = lambda x: cprint(x, "red")
print_red("Sup")