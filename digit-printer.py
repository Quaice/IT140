numbers = {
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
}

digits = input("Enter a four(4) digit number: ")

for x in range(5):
    for digit in digits:
        print(numbers[digit][x], end=' ')
    print()