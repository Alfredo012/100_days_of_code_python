import random

#python password generator
letters = ['a', 'b ', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'x', 'y', 'z', 'A', 'B ', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would yopu like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#   Easy version: Generate the password in secuence. Letters, then symbols, then numbers.
password = ""

# for character in range(1, nr_letters + 1):
#     password = password + random.choice(letters)

# for symbol in range(1, nr_symbols + 1):
#     password = password + random.choice(symbols)

# for number in range(1, nr_numbers + 1):
#     password = password + random.choice(numbers)

# print(f"Your password is: {password}")

# -------------------------------------------------------------------------
#   Hard version: Generate the password in a complety random order.

password_list = []

for character in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for symbol in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for number in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")

