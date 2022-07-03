# УГАДАЙ ЧИСЛО =)
import random
import time
from colorama import init
from colorama import Fore
init()
# Чит-код для игры
# Попытки и время
# Кнопка СТОП
creds = 'Я — Что-то делал\nВова — Тоже что-то делал, забайтил меня на эту хуйню, а ещё написал англ на 82 и пиздел что-то про мою математику'


def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    print("Time passed: {0} min {1} sec".format(int(mins),int(sec)))


def get_user_number():
    while True:
        print(Fore.YELLOW)
        user_input = input("The program randomly selected a number in choosen range, your task is to guess this number with small hints. Please enter your number: ")
        try:
            return int(user_input)
        except ValueError:
            if str(user_input) == 'niggers':
                print(Fore.RED)
                print('пшлнх')
                return 'cheat'
            else:
                print(Fore.BLACK)
                print("Invalid input. Please try again!")
            
def dif_choose():
    global max_random
    print(Fore.CYAN)
    max_random = input('Введите максимум для рандомного числа: ')
    try:
        return int(max_random)
    except:
        print('Введите число')
        dif_choose() 


def cont():
    print(Fore.LIGHTMAGENTA_EX)
    if input('Игра окончена или типо того. Введите 1, чтобы вернуться в меню или любое другое значение, чтобы продолжить игру: ') == '1':
        return
    else:
        game()


def game():
    global random_number
    random_number = random.randint(1, int(max_random))
    start_time = time.time()
    tries = 0
    global user_number 
    user_number = get_user_number()
    print(f"Thanks! You entered: {user_number}")
    while True:
        if user_number != 'cheat':
            if tries != 12:
                if int(user_number) == random_number:
                    print(Fore.CYAN)
                    print(f"You are correct!!!, your number is {random_number} \nYou are correct!!!, your number is {random_number} \nYou are correct!!!, your number is {random_number}")    
                    print(Fore.MAGENTA)
                    print(tries)
                    end_time = time.time()
                    time_lapsed = end_time - start_time
                    time_convert(time_lapsed)
                    cont()
                    break
                else: 
                    tries +=1
                    user_number = get_user_number2()
            else:
                print(Fore.LIGHTRED_EX)
                print(f"You are out of tries.\nNumber was {random_number}")
                cont()
                break
        else:
            print(Fore.BLACK)
            print('Ты ввел чит. Доволен, уёбок?')
            cont()
            break


def menu():
    while True:
        print(Fore.LIGHTBLUE_EX)
        print('Welcome! Это игру прямо сейчас делает уёбок, которому лень писать на английском, поэтому часть текса будет на языке агрессора. \nЭто вроде как меню')
        print(Fore.GREEN)
        print('1. New Game \n2. Credits\n3. Exit')
        menu_nav = input('Выберите пункт меню: ')
        try:
            if int(menu_nav) == 1:
                dif_choose()
                game()
            elif int(menu_nav) == 2:
                print(creds)
                time.sleep(15)
            elif int(menu_nav) == 3:
                print('See you later!')
                break
            else:
                print(Fore.LIGHTBLACK_EX)
                print('Неверное значение')
        except ValueError:
            print(Fore.LIGHTBLACK_EX)
            print('Неверное значение')


def get_user_number2():
        while True:
            try:
                if int(user_number) > random_number:
                    print(Fore.GREEN)
                    print(f"Hidden number is lower than {user_number}")
                    print(Fore.YELLOW)
                    return int(input(f"Choose the number from 1 to {max_random}: "))
                elif int(user_number) < random_number:
                    print(Fore.RED)
                    print(f"Hidden number is BIGGER than {user_number}")
                    print(Fore.YELLOW)
                    return int(input(f"Choose the number from 1 to {max_random}: "))
            except ValueError:
                if user_number == "niggers":
                    print("ah ti chiter")
                    break
                else:   
                    print(Fore.BLACK)
                    print("Invalid input. Please try again!")  


if __name__ == '__main__':
    menu()
