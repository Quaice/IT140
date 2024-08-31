# display.py
import os

class Display:
    pattern = {
        '0': ['***', '* *', '* *', '* *', '***'],
        '1': [' * ', ' * ', ' * ', ' * ', ' * '],
        '2': ['***', '  *', '***', '*  ', '***'],
        '3': ['***', '  *', ' **', '  *', '***'],
        '4': ['* *', '* *', '***', '  *', '  *'],
        '5': ['***', '*  ', '***', '  *', '***'],
        '6': ['*  ', '*  ', '***', '* *', '***'],
        '7': ['***', '  *', '  *', '  *', '  *'],
        '8': ['***', '* *', '***', '* *', '***'],
        '9': ['***', '* *', '***', '  *', '  *'],
        ':': [' ', '*', ' ', '*', ' ']
    }

    styles = {
        "block": u"\u2588", # █
        "dotted": u"\u2593" # ▓
    }

    # Constructor
    def __init__(self, style = "block"):
        self.style = style

    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def printdigits(self, digits):
        print()
        for x in range(5):
            print('  ', end='')
            for digit in digits:
                for ch in self.pattern[digit][x]:
                    if ch == '*':
                        print(Display.styles[self.style], end='')
                    else:
                        print(' ', end='')
                print(' ', end='')
            print()
