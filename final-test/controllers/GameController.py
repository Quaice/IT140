# GameController.py
from objects.Player import Player
from objects.Room import Room
from controllers.InputController import InputController

def validate_player_name():
    while True:
        player_name = input('Input a name for your character: ')

        # Check if the name contains only letters
        if not player_name.isalpha():
            print("Error: Name must contain letters only.")
            continue

        # Check if the name is no longer than 13 characters
        if len(player_name) > 13:
            print("Error: Name cannot be longer than 13 characters.")
            continue

        # If both conditions are met, return the valid player_name
        return player_name

class GameController:
    game = None
    def __init__(self):
        self.player = Player()    # Create a new player
        self.input = ''     # Create a new input handler
        self.current_room = 1    # A reference to the room that the player is currently in
        GameController.game = self

    def change_room(self, room_id):
        # Get a reference to the room
        if room := self.get_room(room_id):
            room.describe()

    def get_room(self, id):
        for room in Room.rooms:
            if room.id == id:
                return room
        return None

    def game_loop(self):
        if self.player.name == '':
            self.player.name = validate_player_name()
            self.change_room(1)
        while True:
            InputController.handle_input(input("> "))

