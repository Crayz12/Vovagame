# УГАДАЙ ЧИСЛО =)
from cmath import pi
import random
import time
from colorama import init
from colorama import Fore, Back, Style
init()
# Чит-код для игры
# Попытки и время
# Кнопка СТОП
tries = 0
random_number = random.randint(1, 100)


def get_user_number():
    while True:
        try:
            print(Fore.YELLOW)
            return int(input("The program randomly selected a number from 1 to 100, your task is to guess this number with small hints. Please enter a number:"))
        except ValueError:
            print(Fore.BLACK)
            print("Invalid input. Please try again!")
            
            
resulting_user_number = get_user_number()
print(f"Thanks! You entered: {resulting_user_number}")
user_number = resulting_user_number


def get_user_number2():
        while True:
            try:
                if int(user_number) > random_number:
                    print(Fore.GREEN)
                    print(f"Hidden number is lower than {user_number}")
                    print(Fore.YELLOW)
                    return int(input("Choose the number from 1 to 100: "))
                elif int(user_number) < random_number:
                    print(Fore.RED)
                    print(f"Hidden number is BIGGER than {user_number}")
                    print(Fore.YELLOW)
                    return int(input("Choose the number from 1 to 100: "))
            except ValueError:
                print(Fore.BLACK)
                print("Invalid input. Please try again!")  

while True:
    if tries != 11:
        if int(user_number) == random_number:
            print(Fore.CYAN)
            print(f"You are correct!!!, your number is {random_number} \nYou are correct!!!, your number is {random_number} \nYou are correct!!!, your number is {random_number}")    
            print(Fore.MAGENTA)
            print(tries)
            break
        else: 
            tries +=1
            user_number = get_user_number2()
    else:
        print(Fore.LIGHTRED_EX)
        print("You are out of tries.")
        break
