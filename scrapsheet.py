# TextBasedGame.py

# J. Aaron Blevins
# IT-140
# Professor Agarwal
# October 10, 2024

def show_instructions() -> None:
    print('''
The Last True Wizard!
Collect the 6 relics from different rooms in the mansion and confront the wizard.
Move commands: move north, move south, move east, move west.
Quick move: n, s, e, w
Collect items: If you see an item of value in a room, enter 'collect' to put it in your inventory.
Confront the wizard in his laboratory with all of the relics needed to aid you and win the game.
''')

def main():
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

    current_room = 'Foyer'

    def get_current_room() -> str:
        return current_room
    def set_current_room(_room) -> None:
        nonlocal current_room
        current_room = _room

    inventory: list = []  # this list stores the items in the player's inventory
    def get_inventory() -> list:
        return inventory
    def add_to_inventory(item: str) -> None:
        inventory.append(item)

    # A function that prints a list of items the player must collect
    def show_remaining_items() -> None:
        if 'Relicarium Arcanum' in inventory:  # If the player is carrying the book of relics, list the items that have yet to be collected
            if len(items) > 0:
                print("You still need to collect: ")
                for i in items.values():
                    print(i, end=', ')
                    print()
            else:
                print("You've collected all the relics!")
        else:  # The player does not have the book of relics
            print_warning("You need to acquire the Relicarium Arcanum from the library first!")

    def get_room_items(_room: str) -> str:
        if _room in items and items[_room] not in get_inventory():
            return items[_room]
        else:
            return "nothing of value here"

    def move(_current_room, direction) -> None:
        if direction in rooms[_current_room]:
            set_current_room(rooms[_current_room][direction])
        else:
            print_warning("I hope you brought an axe because that's a wall...")

    def get_exits(_room):
        _exits = ""  # Initialize _exits as an empty string
        for x in rooms[_room]:  # Iterate over rooms dictionary
            _exits += x.upper() + ", "  # Add each exit in the room to the _exits string and convert it to uppercase
        return _exits  # return the string of exits

    def get_status(_current_room) -> None:
        if _current_room == 'Laboratory' and len(
                items) != 0:  # If the player is in the boss room and all the items haven't been collected, game over
            exit("You encountered the ghost of the manor wizard unprepared! Game over!")
        if _current_room == 'Laboratory' and len(
                items) == 0:  # If the player is in the boss room and all the items have been collected, you win.
            exit("You confront the ghost of the manor wizard and dispel him with your artifacts. You win!")

        print()
        print(
            f'You are in the \033[32m\033[1m {_current_room}\033[0m. You see the \033[35m\033[1m{get_room_items(_current_room)}\033[0m.')
        print(f'There are exits to the \033[36m\033[1m{get_exits(_current_room)}\033[0m.')
        print('----------------------')
        print(f'Inventory: {get_inventory()}')
        print('----------------------')

    def print_warning(text: str) -> None:
        print(f"\033[1m\033[31m{text}!\033[0m")

    def parse_command(*args) -> None:
        _cmd = args[0]
        _room = get_current_room()
        if _cmd == 'exit':
            exit("Not all are brave enough to face the last true wizard...")
        if _cmd == 'help':
            show_instructions()
            return
        if _cmd == 'list':
            show_remaining_items()
            return
        if _cmd == 'move':
            _valid_directions: list = ['north', 'south', 'east', 'west']
            if len(args) > 1 and args[1] in _valid_directions:
                move(_room, args[1])
                return
            else:
                print_warning("Invalid direction")
                return
        if _cmd == 'collect':
            if _room in items and items[_room] not in get_inventory():
                add_to_inventory(items[_room])
                print(f'You collected the \033[35m\033[1m{items[_room]}\033[0m!')
                del items[_room]
                return
            else:
                print_warning("There is nothing here to collect")
                return
        print_warning("Invalid input. Enter the 'help' command for a list of available commands.")

    show_instructions()

    while True:
        get_status(get_current_room())
        cmd = input("Enter a command:> ").lower().split(' ')
        parse_command(*cmd)


if __name__ == '__main__':
    main()