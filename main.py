# УГАДАЙ ЧИСЛО =)
import random
import time
from colorama import init
from colorama import Fore, Back, Style
init()
# Чит-код для игры
# Попытки и время
random_number = random.randint(1, 100)


def get_user_number():
    while True:
        try:
            print(Fore.YELLOW)
            return int(input("The program randomly selected a number from 1 to 100, your task is to guess this number with small hints. Please enter a number:"))
        except ValueError:
            print(Fore.BLACK)
            print("Invalid input. Please try again!")


user_number = get_user_number()
print("Thanks! You entered: {0:d}".format(user_number))

while user_number != random_number:

    try:

    if int(user_number) > random_number:
        print(Fore.GREEN)
        print(f"Hidden number is lower than {user_number}")
        print(Fore.YELLOW)
        user_number = input("Choose the number from 1 to 100: ")

    elif int(user_number) < random_number:
        print(Fore.RED)
        print(f"Hidden number is BIGGER than {user_number}")
        print(Fore.YELLOW)
        user_number = input("Choose the number from 1 to 100: ")



    else:
        print(Fore.CYAN)
        print(f"You are correct!!!, your number is {random_number} \nYou are correct!!!, your number is {random_number} \nYou are correct!!!, your number is {random_number}")
        break
