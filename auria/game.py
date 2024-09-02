#game.py
from auria.objects.inventory import Inventory
from auria.utils.inputhandler import InputHandler
from auria.utils.printer import Printer
from auria.utils.loadlevels import loadLevels
from auria.utils.loaditems import loadItems

class Game:
    def __init__(self):
        self.score = 0
        self.inputHandler = InputHandler()
        self.playerInventory = Inventory()
        self.printer = Printer()
        self.rooms = []
        self.items = []
        self.currentRoom = None
        self.post_init()

    def post_init(self):
        intro()
        self.rooms = loadLevels()
        self.items = loadItems()
        self.LoadLevelItems()
        self.LoadRoom(self.rooms[0])

    def LoadRoom(self, room):
        self.currentRoom = room
        self.printer.PrintRoom(room)

    def AddRoom(self, room):
        self.rooms[room.name] = room

    def ParseInput(self, uinput):
        self.inputHandler.ParseInput(self, uinput, self.currentRoom, self.playerInventory)

    def GetRoom(self, id):
        for room in self.rooms:
            if room.id == id:
                return room
        return None

    def GetItem(self, id):
        for item in self.items:
            if item.id == id:
                return item
        return None

    def LoadLevelItems(self):
        for room in self.rooms:
            putItems = []
            for rItem in room.items:
                for item in self.items:
                    if rItem == item.name:
                        putItems.append(item)
            room.items = putItems

    def Move(self, dir):
        print(dir)
        if self.currentRoom.GetExits(dir):
            room = self.GetRoom(self.currentRoom.GetExits(dir))
            self.LoadRoom(room)
        else:
            print("...how?".format(dir))


############################################################################
############################################################################
############################################################################

def intro():
        print(
'''
 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 

               By: J. Aaron Blevins (Quaice)
                 http://github.com/Quaice

Type '/help' for help
Type '/commands' for a list of possible commands
'''
        )