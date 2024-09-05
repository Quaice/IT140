# GameController.py
from objects.Player import Player

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
    def __init__(self):
        self.player = Player()    # Create a new player
        self.input = ''     # Create a new input handler

        self.current_room = None    # A reference to the room that the player is currently in

    def game_loop(self):
        if self.player.name == '':
            self.player.name = validate_player_name()
        while True:
            user_input = input("> ")

