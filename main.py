# угадай число =)
import random
import time
from colorama import init
from colorama import Fore, Back, Style
init()
# Чит-код для игры
# Попытки и время
# удалить брик(кирпич)
random_number = random.randint(1, 100)
input_number = 0


def check_number(input_number):
    input_number = input()
    while True:
        try:
            return int(input_number)
        except ValueError:
            print(Fore.MAGENTA)
            input_number = input("Invalid input. Please try again!\n")
            break
            
            
            
print(Fore.YELLOW)
print("The program randomly selected a number from 1 to 100, your task is to guess this number with small hints. Please enter a number:")
user_number = check_number(input_number)
print(Fore.YELLOW)
print(f"Thanks! You entered: {user_number}")

while user_number != random_number:
    if int(user_number) > random_number:
        print(Fore.GREEN)
        print(f"Hidden number is lower than {user_number}")
        print(Fore.YELLOW)
        print("Choose the number from 1 to 100: ")
        check_number(input_number)

    elif int(user_number) < random_number:
        print(Fore.RED)
        print(f"Hidden number is BIGGER than {user_number}")
        print(Fore.YELLOW)
        print("Choose the number from 1 to 100: ")
        

    else:
        print(Fore.CYAN)
        print(f"You are correct!!!, your number is {random_number} \nYou are correct!!!, your number is {random_number} \nYou are correct!!!, your number is {random_number}")
        break


# Пососи (pososi)