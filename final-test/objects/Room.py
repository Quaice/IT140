# Room.py
from objects.Object import Object
from controllers.InventoryController import InventoryController

class Room(Object):
    rooms = []

    def __init__(self, id, name, description, exits, mobs):
        super().__init__(id, name, description)
        self.inventory = InventoryController()
        self.exits = exits
        self.mobs = mobs
        self.explored = False
        Room.rooms.append(self)


Room.rooms.append(Room(
    1,
    "Bottom of cistern",
    "The dank and acrid stench of mildew and rust assaults your nose and eyes. The light from the open portal above struggles to reach down this far.",
    ['north'],
    []
))