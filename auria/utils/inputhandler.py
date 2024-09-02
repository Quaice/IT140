#inputhandler
from auria.utils.printer import Printer

commands = (
    'help', 'commands',
    'look', 'l',
    'inspect', 'i',
    'take',
    'inv', 'inventory',
    'drop',
    'north', 'south', 'east', 'west', 'n', 's', 'e', 'w'
)

class InputHandler:
    def __init__(self):
        self.printer = Printer()

    def ParseInput(self, game, uinput, room, pi):
        words = uinput.split(" ")
        if words[0] in commands:
            if words[0] == 'look' or words[0] == 'l':
                self.look(room)
                return

            if words[0] == 'inspect' and len(words) > 1:
                self.inspect(room, pi, words[1])
                return

            if words[0] == 'take' and len(words) > 1:
                self.take(room, words[1], pi)
                return

            if words[0] == 'inventory' or words[0] == 'inv':
                self.inv(pi)
                return

            if words[0] == 'drop' and len(words) > 1:
                self.drop(pi, room, words[1])
                return

            if words[0] == 'north' or words[0] == 'n':
                game.Move('north')
                return

            if words[0] == 'south' or words[0] == 's':
                game.Move('south')
                return

            if words[0] == 'east' or words[0] == 'e':
                game.Move('east')
                return

            if words[0] == 'west' or words[0] == 'w':
                game.Move('west')
                return

            if words[0] == 'commands':
                # print commands
                return

        else:
            print("I don't know what that means...")

    def look(self, room):
        self.printer.PrintRoom(room)

    def inspect(self, room, pi, itemName):
        for item in room.items:
            if item.name == itemName:
                print(item.description)
                return
        for item in pi.GetItems():
            if item.name == itemName:
                print(item.description)
                return
        print("I dont see any {}!".format(itemName))

    def take(self, room, itemName, pi):
        for item in room.items:
            if item.name == itemName:
                print("You picked up the {}.".format(item.name))
                pi.AddItem(item)
                room.items.remove(item)
                return
        print("I dont see any {}!".format(itemName))

    def inv(self, pi):
        if len(pi.GetItems()) > 0:
            for i in pi.GetItems():
                print(i.name)
        else:
            print("You aren't carrying anything.")

    def drop(self, pi, room, itemName):
        for item in pi.GetItems():
            if item.name == itemName:
                print("You dropped the {}.".format(item.name))
                pi.RemoveItem(item, room)
                return
        print("You dont have any {}!".format(itemName))

