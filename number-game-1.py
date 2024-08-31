# Complete the following program

tens = 4 #int(input("Enter the tens digit: "))
ones = 3 #int(input("Enter the ones digit: "))
num = tens * 10 + ones
product = num * 11

print("You entered", num)
print(num, " * 11 is", product)

product_hundreds = product // 100
product_tens = product // 10 % 10
product_ones = product % 10

print("An easy mental way to find the answer is:")
print(tens, ',', tens, '+', ones, ',', ones)

output = product_hundreds * 100 + product_tens * 10 + product_ones
print(output)
