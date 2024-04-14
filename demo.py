from termcolor import colored, cprint

print_red_on_cyan = lambda x: cprint(x, "red", "on_cyan")

print_red = lambda x: cprint(x, "red")
print_red("Sup")

print_green = lambda x: cprint(x, "green")
print_green("Sup")

print_yellow = lambda x: cprint(x, "yellow")
print_yellow("Sup")
print_blue = lambda x: cprint(x, "blue")
print_blue("Sup")
print_magenta = lambda x: cprint(x, "magenta")
print_magenta("Sup")
print_cyan = lambda x: cprint(x, "cyan")
print_cyan("Sup")
print_light_red = lambda x: cprint(x, "light_red")
print_light_red("Sup")
print_light_green = lambda x: cprint(x, "light_red", attrs=["bold"])
print_light_green("Bro")