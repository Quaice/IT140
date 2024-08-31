user_int = int(input("Enter integer (32 - 126):\n"))
user_float = float(input("Enter float:\n"))
user_char = input("Enter character:\n")
user_string = input("Enter string:\n")

print(user_int, user_float, user_char, user_string)
print(user_string, user_char, user_float, user_int)
print(user_int, "converted to a character is", chr(user_int))