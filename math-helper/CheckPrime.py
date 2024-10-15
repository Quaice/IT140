# CheckPrime.py
import math

class CheckPrime:
    def __init__(self):
        self.mode = 'cp'

    def IsPrime(self, n:int) -> bool:
        if n > 1:
            largest_divisor = math.floor(math.sqrt(n))
            for i in range(2, largest_divisor):
                if n % i == 0:
                     return False
            return True
        return False

    def loop(self):
        while True:
            n = input("Enter a Natural number > 1: ")
            if n == 'q':
                exit("Program terminated.")
            if n == 'e':
                return
            print(self.IsPrime(int(n)))