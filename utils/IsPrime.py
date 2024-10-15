# IsPrime.py
import math

# What defines a prime number(n)?
# - n must be a Natural(N) number: n == N
# - n must be greater than 1: n > 1
# - Exactly two(2) divisors, 1 and n
# - Cannot be divided evenly by any Integer(I)
# - The first prime, and only even prime, is two(2)
def IsPrime(n:int) -> bool:
    if n > 1:
        largest_divisor = math.floor(math.sqrt(n))
        print("Largest divisor: {}".format(largest_divisor))
        for i in range(2, largest_divisor):
            if n % i == 0:
                 return False
        return True
    return False
print("-" * 30)
print("This program will accept any Natural number greater than 1 and determine if it is a prime number.")
print("Enter 'quit' to exit the program.")
print("-" * 30)

if __name__ == '__main__':
    while True:
        n = input("Enter a Natural number > 1: ")
        if n == 'quit':
            exit("Program terminated.")
        print(IsPrime(int(n)))