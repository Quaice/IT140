#inventory

class Inventory:
    def __init__(self):
        self.items = []

    def AddItem(self, item):
        self.items.append(item)

    def RemoveItem(self, item, room):
        room.AddItem(item)
        self.items.remove(item)

    def GetItems(self):
        return self.items