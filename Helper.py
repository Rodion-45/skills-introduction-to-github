from math import *
from random import *
from time import *
from smtplib import *
from os import *
today = []
tommorow = []
other = []
def eng():
    def hlp():
        print('/coms - Displays the list of commands;')
        print('/tasks - Opens the task manager')
        print('    /addtask - Adds a task')
        print('    /deletetask - Deletes a task')
        print("/calc - Starts calculator")
        print("    -, +, *, / - Arithmetic operations")
        print("    % - Remainder from division")
        print("    // - Integer division")
        print("/signinen")
        print('/stop - Ends session')

    def tasks():
        while True:
            print('Welcome to the task manager!')
            com = str(input('Enter command: '))
            if com == "/addtask":
                t_list = str(input('''
                Choose task list:
                    1) Today
                    2) Tomorrow
                    3) Others
                '''))
                if t_list == "1":
                    today.append(input("Enter task: "))
                elif t_list == "2":
                    tommorow.append(input("Enter task: "))
                elif t_list == "3":
                    other.append(input("Enter task: "))
                else:
                    print("Unknown list.")
            elif com == "/deletetask":
                t_list = str(input('''
                Choose task list:
                    1) Today
                    2) Tomorrow
                    3) Others
                '''))
                if t_list == "1":
                    del today[int(input("Enter number of task you want to delete: ")) - 1]
                elif t_list == "2":
                    del tommorow[int(input("Enter number of task you want to delete: ")) - 1]
                elif t_list == "3":
                    del other[int(input("Enter number of task you want to delete: ")) - 1]
                else:
                    print("Unknown list.")
            elif com == "/menu":
                break

    def calc():
        print("Welcome to the calculator!")
        while True:
            com = input("Enter a mathematical operation or /menu to exit: ")
            if com == '/menu':  # If the exit command is entered
                print("Exiting application...")
                break  # Break out of the loop
            elif com == '+':
                a = int(input("Enter the first addend: "))
                b = int(input("Enter the second addend: "))
                print(f"The result of the expression {a}+{b}={a + b}")
            elif com == '-':
                a = int(input("Enter the minuend: "))
                b = int(input("Enter the subtrahend: "))
                print(f"The result of the expression {a}-{b}={a - b}")
            elif com == '*':
                a = int(input("Enter the first factor: "))
                b = int(input("Enter the second factor: "))
                print(f"The result of the expression {a}*{b}={a * b}")
            elif com == '/':
                a = float(input("Enter the dividend: "))
                b = float(input("Enter the divisor: "))
                if b != 0:
                    print(f"The result of the expression {a}/{b}={a / b}")
                else:
                    print("Error! Division by zero is not possible.")
            elif com == '%':
                a = int(input("Enter the dividend: "))
                b = int(input("Enter the divisor: "))
                if b != 0:
                    print(f"The result of the expression {a}%{b}={a % b}")
                else:
                    print("Error! It is impossible to find the remainder when dividing by zero.")
            elif com == '//':
                a = int(input("Enter the dividend: "))
                b = int(input("Enter the divisor: "))
                if b != 0:
                    print(f"The result of the expression {a}//{b}={a // b}")
                else:
                    print("Error! It is impossible to perform integer division by zero.")
            elif com == "/menu":
                break
            else:
                print("Unknown command.")

    def sign_in():
        with open('sign_in.txt', 'a+') as f:
            print("Registration.")
            global user_name
            user_name= input("Enter username: ")
            f.write(user_name)
            global password
            password = input("Enter password: ")
            f.write(password)
            pass_check = input("Repeat password: ")
            if password == pass_check:
                print("Password accepted!")
            else:
                print("Password entry error.")

    # def log_in():

    def coms():
        if com == '/coms':
            hlp()
        elif com == '/tasks':
            tasks()
        elif com == "/calc":
            calc()
        elif com == "/signin":
            sign_in()
        elif com == '/stop':
            print('Goodbye!')
            quit()
        elif com == "/clear":
            system('clear')
        else:
            print("Unknown command.")

    print('This is your personal assistant.')
    print('To see the list of commands, type "/coms"')

    while True:
        com = str(input('Enter command: '))
        coms()

def rus():
    def hlp():
        print('/coms - Выводит список команд;')
        print('/tasks - Открывает менеджер задач')
        print('    /addtask - Добавляет задачу')
        print('    /deletetask - Удаляет задачу')
        print("/calc - Запускает калькулятор")
        print("    -, +, *, / - Арифметические действия")
        print("    % - Остаток от деления")
        print("    // - Целочисленное деление")
        print("/signin")
        print('/stop - Завершает сессию')

    def tasks():
        while True:
            print('Добро пожаловать в менеджер задач!')
            com = str(input('Введите команду: '))
            if com == "/addtask":
                t_list = str(input('''Выберите список задач:
                                     1)Сегодня
                                     2)Завтра
                                     3)Остальные
                                     '''))
                if t_list == "1":
                    today.append(input("Введите задачу: "))
                elif t_list == "2":
                    tommorow.append(input("Введите задачу: "))
                elif t_list == "3":
                    other.append(input("Введите задачу: "))
                else:
                    print("Неизвестный список.")
            elif com == "/deletetask":
                t_list = str(input('''Выберите список задач:
                                    1)Сегодня
                                    2)Завтра
                                    3)Остальные
                                    '''))
                if t_list == "1":
                    del other[int(input("Введите номер задачи, которую вы хотите удалить: ")) - 1]
                elif t_list == "2":
                    del other[int(input("Введите номер задачи, которую вы хотите удалить: ")) - 1]
                elif t_list == "3":
                    del other[int(input("Введите номер задачи, которую вы хотите удалить: ")) - 1]
                else:
                    print("Неизвестный список.")
            elif com == "/menu":
                break

    def calc():
        print("Добро пожаловать в калькулятор!")
        while True:
            com = input("Введите математическую операцию или /menu для выхода: ")
            if com == '/menu':  # Если ввели команду выхода
                print("Выход из приложения...")
                break  # Прерывание цикла
            elif com == '+':
                a = int(input("Введите первое слагаемое: "))
                b = int(input("Введите второе слагаемое: "))
                print(f"Результат выражения {a}+{b}={a + b}")
            elif com == '-':
                a = int(input("Введите уменьшаемое: "))
                b = int(input("Введите вычитаемое: "))
                print(f"Результат выражения {a}-{b}={a - b}")
            elif com == '*':
                a = int(input("Введите первый множитель: "))
                b = int(input("Введите второй множитель: "))
                print(f"Результат выражения {a}*{b}={a * b}")
            elif com == '/':
                a = float(input("Введите делимое: "))
                b = float(input("Введите делитель: "))
                if b != 0:
                    print(f"Результат выражения {a}/{b}={a / b}")
                else:
                    print("Ошибка! Деление на ноль невозможно.")
            elif com == '%':
                a = int(input("Введите делимое: "))
                b = int(input("Введите делитель: "))
                if b != 0:
                    print(f"Результат выражения {a}%{b}={a % b}")
                else:
                    print("Ошибка! Невозможно найти остаток от деления на ноль.")
            elif com == '//':
                a = int(input("Введите делимое: "))
                b = int(input("Введите делитель: "))
                if b != 0:
                    print(f"Результат выражения {a}//{b}={a // b}")
                else:
                    print("Ошибка! Невозможно выполнить целочисленное деление на ноль.")
            elif com == "/menu":
                break
            else:
                print("Неизвестная команда.")

    def sign_in():
        with open('sign_in.txt', 'a+') as f:
            print("Регистрация.")
            global user_name
            user_name = input("Введите имя пользователя: ")
            f.write(user_name)
            global password
            password = input("Введите пароль: ")
            f.write(password)
            pass_check = input("Повторите пароль: ")
            if password == pass_check:
                print("Пароль принят!")
            else:
                print("Ошибка ввода пароля.")

    # def log_in():

    def coms():
        if com == '/coms':
            hlp()
        elif com == '/tasks':
            tasks()
        elif com == "/calc":
            calc()
        elif com == "/signin":
            sign_in()
        elif com == '/stop':
            print('До свидания!')
            quit()
        else:
            print("Неизвестная команда.")

    print('Это ваш персональный помощник.')
    print('Для того, чтобы узнать список команд, введите "/coms"')
    while True:
        com = str(input('Введите команду: '))
        coms()
while True:
    print("Choose language")
    com = input("ru or en: ")
    if com.lower() == "ru":
        rus()
    elif com.lower() == "en":
        eng()
    else:
        print("Unknown language. Try again.")
        error()