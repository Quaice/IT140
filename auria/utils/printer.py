#printer.py

import textwrap
import os

try:
    window_size = os.get_terminal_size()
except OSError:
    window_size = 70

class Printer:
    def printRoomName(self, name):
        print("┏━", end='')
        for i in name:
            print("━", end='')
        print("━┓")
        print("┃", name, "┃")
        print("┗━", end='')
        for i in name:
            print("━", end='')
        print("━┛")

    def printDescription(self, text):
        desc = textwrap.wrap(text, window_size)
        for line in desc:
            print(line)

    def printItems(self, room):
        if len(room.items) > 0:
            print("In the room you see: ", end='')
            for i in range(len(room.items)):
                if len(room.items) == 1:
                    print("A {}".format(room.items[i].name))
                    return
                if i == 0:
                    print("A {}, ".format(room.items[i].name), end='')
                elif i == len(room.items) - 1:
                    print("and a {}".format(room.items[i].name))
                else:
                    print("a {}, ".format(room.items[i].name), end='')

    def printExits(self, room):
        print("You see an exit to the ", end='')
        for i in range(len(room.exits)):
            if len(room.exits) == 1:
                for key in room.exits[i]:
                    print("{}.".format(key))
                    return
            if i == 0:
                for key in room.exits[i]:
                    print("{}, ".format(key), end='')
            elif i == len(room.exits) - 1:
                for key in room.exits[i]:
                    print("and {}.".format(key))
            else:
                for key in room.exits[i]:
                    print("{}, ".format(key), end='')




    def PrintRoom(self, room):
        self.printRoomName(room.name)
        self.printDescription(room.description)
        self.printItems(room)
        self.printExits(room)
