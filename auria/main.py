#main.py
# Title: Auria: A text-based adventure
# Description: Auria is a text-based adventure game built for an Intro to Scripting class
# Author: Quaice (https://github.com/Quaice)

from game import Game

def main():
    game = Game()  # The game manager
    while True:
        uinput = input("■▶ ")
        if uinput == 'exit':
            exit("It's okay...\nMost adventurers don't have what it takes to explore Auria.")
        else:
            game.ParseInput(uinput)

if __name__ == '__main__':
    main()