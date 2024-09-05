# Item.py

from objects.Object import Object

class Item(Object):
    def __init__(self, id, name , description, power):
        super().__init__(id, name, description)
        self.power = power

    def drop(self):
        print()

    def pickup(self):
        print()