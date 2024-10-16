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
    # This dict gives the name of a room and list the other rooms it connects to and in which direction
    rooms: dict = {
        'Foyer': {'north': 'Hall', 'item': 'nothing of value'},
        'Hall': {'south': 'Foyer', 'west': 'Master Bedroom', 'east': 'Library', 'north': 'Kitchen', 'item': 'nothing of value'},
        'Library': {'west': 'Hall', 'item': 'Relicarium Arcanum'},
        'Master Bedroom': {'east': 'Hall', 'item': 'Pewter Bear Necklace'},
        'Kitchen': {'south': 'Hall', 'east': 'Cellar', 'west': 'Conservatory', 'north': 'Lounge', 'item': 'Sceptre of Light'},
        'Conservatory': {'east': 'Kitchen', 'north': 'Laboratory', 'item': 'Twelve Leaf Clover'},
        'Lounge': {'south': 'Kitchen', 'item': 'Spirit of the Lion'},
        'Cellar': {'west': 'Kitchen', 'item': 'Gold Skeleton Key'},
        'Laboratory': {'south': 'Conservatory', 'north': 'Exit', 'item': 'Wizard'},
        'Exit': {}
    }

    # Initialize the current room and set the starting room
    current_room = 'Foyer'
    inventory = []

    def show_state() -> None:
        exits = rooms[current_room].copy()
        del exits['item']
        exits = list(exits.keys())
        print()
        print(f"You are in the \033[32m\033[1m {current_room}\033[0m. You see the \033[35m\033[1m{rooms[current_room]['item']}\033[0m.")
        print(f'There are exits to the \033[36m\033[1m{exits}\033[0m.')
        print('----------------------')
        print(f'Inventory: {inventory}')
        print('----------------------')

    def get_new_state(_direction, _current_room):
        nonlocal current_room
        if _direction in rooms[_current_room]:
            current_room = rooms[_current_room][_direction]
        else:
            print_warning("I hope you brought an axe because that's a wall...")

    def print_warning(text: str) -> None:
        print(f"\033[1m\033[31m{text}!\033[0m")

    # Game Loop
    show_instructions()
    while True:
        if current_room == 'Laboratory' and len(inventory) == 6:  # If the player is in the boss room and all the items haven't been collected, game over
            exit("You encountered the ghost of the manor wizard unprepared! Game over!")
        if current_room == 'Laboratory' and len(inventory) < 6:  # If the player is in the boss room and all the items have been collected, you win.
            exit("You confront the ghost of the manor wizard and dispel him with your artifacts. You win!")

        show_state()

        cmd = input("> ").lower().split()
        if cmd[0] == 'exit':
            exit("Not all are brave enough to face the last true wizard...")
        elif cmd[0] == 'help':
            show_instructions()
        elif cmd[0] == 'move':
            _valid_directions: list = ['north', 'south', 'east', 'west']
            if len(cmd) > 1 and cmd[1] in _valid_directions:
                get_new_state(cmd[1], current_room)
            else:
                print_warning("Invalid direction!")
        elif cmd[0] == 'collect':
            if rooms[current_room]['item'] != 'nothing of value':
                _item = rooms[current_room]['item']
                inventory.append(_item)
                print(f'You collected the \033[35m\033[1m{_item}\033[0m!')
                rooms[current_room]['item'] = 'nothing of value'
            else:
                print_warning("There is nothing here to collect!")
        else:
            print_warning("Invalid input. Enter the 'help' command for a list of available commands.")


if __name__ == '__main__':
    main()