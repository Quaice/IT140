# str.format has a field width property you can use
# You can pad a string, use it to align text within the field width
# and replace the default space(' ') padding with another fill character

# Create a field {} and assign it a width :17
print("..{:16}..".format("field content"))

# You can name the field
print("..{title:20}..".format(title="Top 100 Books"))

# You can align <^> the string within the padded field {title:<20}
# left align = <, center = ^, right align = >
print("|{title:^20}|".format(title="Short Stories"))

# You can change the character used for padding
print("|{title:-^20}|".format(title="Fiction Novels"))


# There is a precision component as well {:.4f}
# which prints the specified number of decimal places
print("{num:.4f}".format(num=31/7))

# You can also pad and align this component the same way
print("{num:->10.4f}".format(num=5.0))

# Replace a string within a string with .replace
text = "Today is just another day."
text = text.replace(' day', ' Monday')
print(text)

# Find the index of the first occurrence within a string
day = text.find('Monday')
print(text[day:])

x = "This is a longer string, and now we will cut it in half right before your very eyes!"
print(x[:len(x)//2])

my_str = 'http://reddit.com/r/python'
protocol = 'http://'
print(my_str[len(protocol):])

numbers = '0123456789'

print('All numbers: {}'.format(numbers[::]))
print('Every other number: {}'.format(numbers[::2]))
print('Every third number between 1 and 8: {}'.format(numbers[1:9:3]))