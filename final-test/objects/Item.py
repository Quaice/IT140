# Item.py

from objects.Object import Object

class Item(Object):
    items = []

    def __init__(self, id, name , description, power):
        super().__init__(id, name, description)
        self.power = power
        Item.items.append(self)

    def drop(self):
        print()

    def pickup(self):
        print()