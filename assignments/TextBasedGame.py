# TextBasedGame.py

# J. Aaron Blevins
# IT-140
# Professor Agarwal
# October 10, 2024

def show_intro():
    print('''
You, a fatalist explorer, have learned of an old manor house once occupied by a now-deceased eccentric autodidact 
rumored to have been the last true wizard to exist. The local lore suggests that the wizard possessed artifacts of 
significant power and value but that due to a maleficent curse, no soul has set foot in the manor since the 
owner’s death. Your research has led you to believe you can enter the house, collect these artifacts, dispel the 
curse, and safely leave. To do this, you plan to first collect the Relicarium Arcanum from the Library. This book 
should explain the nature of the artifacts, how to use them and where in the manor you might find them.
''')

def show_instructions():
    print('''
MOVING:
To move between rooms, use the command 'move' followed by a direction. E.X.: 'move north'
You can move north, south, east, or west if the direction is availbale in your current room.

ITEMS:
If you see a valuable item in a room, you can enter 'collect' to add it to you inventory.

INVENTORY:
To see a list of items in your inventory, enter 'inventory' or simply 'i'.

OBJECTIVES:
Once you obtain the Relicarium Arcanum from the library, you may see a list of relics you must collect before
confronting the wizard by entering the 'list' command.

HELP
To see these instruction again, enter the 'help' command.
To quit the game, enter the 'exit' command.
''')

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
def get_current_room() -> str:
    return current_room
def set_current_room(room):
    global current_room
    current_room = room

inventory: list = []  # this list stores the items in the player's inventory

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

def get_status(_current_room):
    print()
    print(f'{get_current_room().upper()}:')
    print(f"You are in the {current_room} and you see exits to the {get_exits(current_room)}.")
    if current_room in items and items[current_room] not in inventory:
        print(f"You see the {items[current_room]} here.")
    else:
        print("You see nothing of value here.")

# This function moves the player with only a single letter input of n, s, e, or w.
# This function is for making testing easier. You're welcome.
def short_move(d, cr):
    dirs = {'n': 'north', 's': 'south', 'e': 'east', 'w': 'west'}
    if d in dirs and dirs[d] in rooms[cr]:
        return rooms[cr][dirs[d]]

# A function that prints a list of items in the player's inventory
def show_inventory():
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

def move(_current_room, direction):
    if direction in rooms[_current_room]:
        set_current_room(rooms[_current_room][direction])
    else:
        print("I hope you brought an axe because that's a wall...")

def collect(cr):
    if get_current_room() in items and items[get_current_room()] not in inventory:
        inventory.append(items[get_current_room()])  # Add the item to the player inventory
        print(f"You collected the {items[get_current_room()]}!")
        del items[get_current_room()]  # Mark the item off the list of collectibles
    else:
        print("There is nothing here to collect...")

def parse_command(command):
    if len(command[0]) == 1:
        cr = get_current_room()
        ncr = short_move(command[0], cr) if short_move(command[0], cr) is not None else cr
        set_current_room(ncr)
    if len(command) == 1 and command[0] in commands:
        if command[0] == 'exit':
            exit("Not all are brave enough to face the last true wizard...")

        if command[0] == 'help':
            print(show_instructions())

        if command[0] == 'i' or command[0] == 'inventory':
            show_inventory()

        if command[0] == 'move':
            print("You must specify a direction!")

        if command[0] == 'list':
            print_list()

        if command[0] == 'collect':
            collect(get_current_room())

    elif len(command) == 2 and command[0] == 'move' and command[1] in directions:
        move(get_current_room(), command[1])
    else:
        print("Invalid command. Enter 'help' for a list of commands.")

def main():
    show_intro()
    show_instructions()

    # Game Loop
    while True:
        check_for_end_state(current_room)
        get_status(current_room)

        command = input("> ").lower().split(' ')
        parse_command(command)


if __name__ == '__main__':
    main()
