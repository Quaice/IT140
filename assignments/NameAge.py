# J. Aaron Blevins
# IT-140
# Professor Agarwal
# September 10, 2024
user_name = input("What is your name? ") # Get the user's name
user_age = int(input("How old are you? ")) # Get the user's age as an integer type
birth_year = 2024 - user_age # Calculate the user's birth year based on their age and the current year
print("Hello {}! You were born in {}.".format(user_name, birth_year)) # Print the user's name and birth year.