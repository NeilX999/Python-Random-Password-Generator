#!/usr/bin/python
import random

# Random Password Generator

def password_generator(password_length):

    # Different sort of password characters
    alphabets_and_numbers = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    special_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "_", "-", "+", "=", ":", ";", "|", "<", ">", ",", ".", "?", "~"]

    # Converts each element from 'numbers' list and cast them to <class 'str'>
    numbers = [i for i in range(0, 10)]
    for num in numbers:
        num = str(num)
        alphabets_and_numbers.append(num)

    # Final password will be store here
    password = []

    """
    Sets a range from the given input.
    Picks random character from the list above (password_characters).
    Appends to 'password' list and join all elements
    """
    for i in range(1, password_length + 1):
        if len(password) != password_length:
            password.append(random.choice(alphabets_and_numbers))
            password.append(random.choice(special_characters))
    x = ''.join(password)
    print(x)
    print(" ")


"""
Main loop
Input from user
"""
while True:
    try:
        password_length = int(input("How long do you want your password to be: "))
        print(" ")
        if password_length < 6 or password_length > 60:
            print("Password length specified is too short or long")
            print(" ")
            continue

        elif password_length >= 6 or password_length <= 60:
            password_generator(password_length)
            break

    except ValueError:
        print(" ")
        print("Cannot to a alphabets. Must be a number")
        print(" ")
        continue
