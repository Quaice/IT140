# Player. py

from controllers.InventoryController import InventoryController

class Player:
    def __init__(self):
        self.name = ''
        self.power = 5
        self.health = 100
        self.inventory = InventoryController()

    # Sets name to the value given by the user
    def set_name(self, name):
        self.name = name