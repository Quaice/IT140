# get name as a string
# get age as an int
# calculate birth year
# print greeting
user_name = input("What is your name? ")
user_age = input("How old are you? ")
birth_year = 2024 - int(user_age)
print("Hello {}! You were born in {}.".format(user_name, birth_year))