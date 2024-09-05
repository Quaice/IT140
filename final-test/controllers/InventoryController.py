# InventoryController.py

# An InventoryController is used to hold items and allow the player to manipulate them.
class InventoryController:
    def __init__(self):
        self.contents = []

    # Returns true if the inventory contents contains the specified item
    def has_item(self, item):
         return item in self.contents

    # Returns a reference to the specified item if the item is in the contents
    # Return None if the specified item doesn't exist
    def get_item(self, item):
        if self.has_item(item):                         # If in item exists in contents[]
            return item                                 # Return the item
        return None                                     # or else return None

    # Adds an item to the inventory
    def add_item(self, item):
        if not self.has_item(item):                     # If the item is not already in contents[]
            self.contents.append(item)                  # Add the item to contents[]

    # Removes an item from the inventory
    def remove_item(self, item):
        if self.has_item(item):                         # If in item exists in contents[]
            self.contents.remove(item)                  # Remove the item from contents[]

    # Returns the contents list
    # WARNING: Possibly unsafe!!!
    def get_contents(self):
        return self.contents                            # Returns the inventories contents[] list

    # Prints the contents of the inventory for the user
    # TODO: Add comments
    def print_contents(self):
        title = "┃ Inventory ┃"
        maxlen = len(title)
        print("┏" + ("━" * (maxlen - 2)) + "┓")
        print(title)
        print("┣" + ("━" * (maxlen - 2)) + "┛")
        for item in self.contents:
            print("┃ {} ".format(item.name))
        print("┗" + ("━" * (maxlen - 1)))