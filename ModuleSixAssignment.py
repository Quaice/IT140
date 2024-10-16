# ModuleSixAssignment.py
# J. Aaron Blevins
# IT-140
# Professor Agarwal
# October 10, 2024

# A dictionary for the simplified dragon text game
# This dict gives the name of a room and list the other rooms it connects to and in which direction
rooms: dict = {
    'Foyer': {'north': 'Hall'},
    'Hall': {'south': 'Foyer', 'west': 'Master Bedroom', 'east': 'Library', 'north': 'Kitchen'},
    'Library': {'west': 'Hall'},
    'Master Bedroom': {'east': 'Hall'},
    'Kitchen': {'south': 'Hall', 'east': 'Cellar', 'west': 'Conservatory', 'north': 'Lounge'},
    'Conservatory': {'east': 'Kitchen', 'north': 'Laboratory'},
    'Lounge': {'south': 'Kitchen'},
    'Cellar': {'west': 'Kitchen'},
    'Laboratory': {'south': 'Conservatory', 'north': 'Exit'},
    'Exit': {}
}

# A dictionary for the items in the game.
# This dict gives the name and location of the items
items: dict = {
    'Library': 'Relicarium Arcanum',
    'Master Bedroom': 'Pewter Bear Necklace',
    'Kitchen': 'Sceptre of Light',
    'Conservatory': 'Twelve Leaf Clover',
    'Lounge': 'Spirit of the Lion',
    'Cellar': 'Golden Skeleton Key'
}

# A list of possible directions the player might move
directions: list = ['north', 'south', 'east', 'west']

# A list of possible commands the player can use
# This will make input validation easier (for me)
commands: list = ['move', 'collect', 'i', 'inventory', 'list', 'exit', 'help']

# Initial setup
current_room: str = 'Foyer'  # this string stores the name of the current room
inventory: list = []  # this list stores the items in the player's inventory

# FUNCTIONS
# Check to see if the current state of the game calls for ending the game
# This function checks to see if all the items have been collected before encountering the boss
def check_for_end_state(_current_room):
    if _current_room == 'Laboratory' and len(items) != 0: # If the player is in the boss room and all the items haven't been collected, game over
        exit("You encountered the ghost of the manor wizard unprepared! Game over!")
    if _current_room == 'Laboratory' and len(items) == 0: # If the player is in the boss room and all the items have been collected, you win.
        exit("You confront the ghost of the manor wizard and dispel him with your artifacts. You win!")

# Get a list of exits for the current room
def get_exits(_room):
    _exits = "" # Initialize _exits as an empty string
    for x in rooms[_room]: # Iterate over rooms dictionary
        _exits += x.upper() + ", " # Add each exit in the room to the _exits string and convert it to uppercase
    return _exits # return the string of exits

# A function that prints a list of items in the player's inventory
def print_inventory():
    if len(inventory) == 0: # If nothing is in the inventory
        print("You are not carrying anything.")
    else: # If something is in the inventory
        print("In your inventory you see: ")
        for i in inventory:
            print(i, end=', ')
            print()

# A function that prints a list of items the player must collect
def print_list():
    if 'Relicarium Arcanum' in inventory: # If the player is carrying the book of relics, list the items that have yet to be collected
        print("You still need to collect: ")
        for i in items.values():
            print(i, end=', ')
            print()
    else: # The player doesnt have the book of relics
        print("You need to acquire the Relicarium Arcanum from the library first!")

# A function that prints the introduction to the game
def print_intro():
    print('''
    You, a fatalist explorer, have learned of an old manor house once occupied by a now-deceased eccentric autodidact 
    rumored to have been the last true wizard to exist. The local lore suggests that the wizard possessed artifacts of 
    significant power and value but that due to a maleficent curse, no soul has set foot in the manor since the 
    owner’s death. Your research has led you to believe you can enter the house, collect these artifacts, dispel the 
    curse, and safely leave. To do this, you plan to first collect the Relicarium Arcanum from the Library. This book 
    should explain the nature of the artifacts, how to use them and where in the manor you might find them.
    ''')

# A function that prints the instructions for the player
def print_help():
    print("### INSTRUCTIONS ###")
    print("To move, use the command 'move' followed by a space and the directions you wish to move.")
    print("You may move north, south, east, or west")
    print("If you see an item in a room, you can enter 'collect' to add it to your inventory.")
    print("To see a list of items in your inventory, you can enter 'inventory' or 'i'.")
    print('''
Once you've collected the Relicarium Arcanum from the library, you can see the list of items you must collect
by entering the 'list' command.
    ''')
    print("To see these instructions again, enter 'help'.")
    print("To quit the game, enter 'exit'")
    print()

# This function moves the player with only a single letter input of n, s, e, or w.
# This function is for making testing easier. You're welcome.
def short_move(d, cr):
    dirs = {'n': 'north', 's': 'south', 'e': 'east', 'w': 'west'}
    if d in dirs and dirs[d] in rooms[cr]:
        return rooms[cr][dirs[d]]

if __name__ == '__main__':
    print_intro()
    print("Enter 'help' to see a list of commands.")
    while True:
        check_for_end_state(current_room)  # Check to see if the current state of the game calls for ending the game
        print()
        print(f"You are in the {current_room} and you see exits to the {get_exits(current_room)}.")
        if current_room in items and items[current_room] not in inventory:
            print(f"You see the {items[current_room]} here.")
        else:
            print("You see nothing of value here.")

        command = input("> ")
        command = command.lower().split(' ') # Change the command to lowercase and split out any arguments

        # Short move for easier testing...
        if len(command[0]) == 1:
            current_room = short_move(command[0], current_room) if short_move(command[0], current_room) is not None else current_room

        if len(command) == 1 and command[0] in commands:
            if command[0] == 'exit':
                exit("Not all are brave enough to face the last true wizard...")

            if command[0] == 'help':
                print_help()

            if command[0] == 'i' or command[0] == 'inventory':
                print_inventory()

            if command[0] == 'move':
                print("You must specify a direction!")

            if command[0] == 'list':
                print_list()

            if command[0] == 'collect':
                if current_room in items and items[current_room] not in inventory:
                    inventory.append(items[current_room]) # Add the item to the player inventory
                    print(f"You collected the {items[current_room]}!")
                    del items[current_room] # Mark the item off the list of collectibles
                else:
                    print("There is nothing here to collect...")

        elif len(command) == 2 and command[0] == 'move' and command[1] in directions:
            direction = command[1]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("I hope you brought an axe because that's a wall...")
        else:
            print("Invalid command. Enter 'help' for a list of commands.")