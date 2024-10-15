# main.py
# High/Low Game
# https://github.com/Quaice

from Printer import Printer

p = Printer()

while True:

    #p.pretty_box(['Type [_red_]"quit"[_] and', 'press enter to exit the game.'])
    print(p.cprint('Type [_red_]"quit"[_] and press enter to exit the game.'))
    p.pretty_box(['Type [_red_]"quit"[_] and press ENTER', 'to exit the game.'])

    uip = input("")

    if uip == "quit":
        exit()