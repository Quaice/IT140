# J. Aaron Blevins
# IT-140
# Professor Nikhil Agarwal
# September 5, 2024

from controllers.GameController import GameController

if __name__ == '__main__':                  # If this file was run
    if game := GameController():
        game.game_loop()                    # and start the game loop