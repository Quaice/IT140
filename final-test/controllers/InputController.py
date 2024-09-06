# InputController.py

class InputController:
    def __init__(self):
        InputController.input = self
        self.commands = {
            'commands': self.commands,
            'quit': self.quit,
            'look': self.look, 'l': self.look,
            'inspect': self.inspect, 'ins': self.inspect,
            'north': self.north, 'n': self.north,
            'south': self.south, 's': self.south,
            'east': self.east, 'e': self.east,
            'west': self.west, 'w': self.west,
            'take': self.take, 'drop': self.drop,
            'inventory': self.inventory, 'i': self.inventory, 'inv': self.inventory,
            'attack': self.attack, 'a': self.attack
        }

    def commands(self, commands):
        print()

    def quit(self):
        quit()

    def look(self):
        print()

    def inspect(self):
        print()

    def north(self):
        print()

    def south(self):
        print()

    def east(self):
        print()

    def west(self):
        print()

    def take(self):
        print()

    def drop(self):
        print()

    def inventory(self):
        print()

    def attack(self):
        print()

    # uinput: Input from the user, typed into the console
    def handle_input(self, uinput: str):
        parts = uinput.lower().split(" ")
        command = parts[0]
        args = parts[1:]

        action = self.commands.get(command)
        if action:
            if len(args) > 0:
                action(args)
            else:
                action()
        else:
            self.unknown_command(command)