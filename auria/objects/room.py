#room.py

class Room():
    def __init__(self, id, name, description, shortDescription, items, exits):
        self.id = id
        self.name = name
        self.description = description
        self.shortDescription = shortDescription
        self.items = items
        self.exits = exits

    def AddItem(self, item):
        self.items.append(item)

    def RemoveItem(self, item):
        self.items.remove(item)

    def UpdateDescription(self, description):
        self.description = description

    def GetName(self):
        return self.name

    def GetDescription(self):
        return self.description

    def GetExits(self, dir):
        for exit in self.exits:
            for key in exit:
                if dir == key:
                    return exit[key]
        return None