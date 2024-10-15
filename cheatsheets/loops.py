letters = "ABCDEFG"
for letter in letters:
    print(letter, end=' ')
else:
    print("... That's all the letters I know!")

for (index, value) in enumerate(letters):
    print(index, value, end=' ')
print()

x=1
while x<=3:
    print(x, end=' ')
    x+=1
else:
    print("... And that's how you count to three!")

