# приветствие
#правила игры
#сказать компьютеру отгадать число
#загадать число от 1 до 100
#компьютер должен начать угадывать число
#я должна сказать, какое должно быть число: больше, меньше или то, которое я загадала
#указать количество попыток

import random

# Приветствие
print('Добро пожаловать в игру "Угадай число"')

# Правила игры
print('Компьютер должен угадать число, загаданное человеком. Количество попыток - 10.')

# начальные значения
# my_number = int(input('Мое число: '))
my_number = 60
min = 1
max = 100
mac_number = 0
tries = 0
number_list = []

while mac_number != my_number:
    mac_number = random.randrange(min, max)
    if mac_number in number_list:
        continue
    number_list.append(mac_number)
    print(number_list)
    print(mac_number)
    if mac_number < my_number:
        min = mac_number
    else:
        max = mac_number
    tries += 1

   
print('Вы угадали за', tries, "попыток!\n")


# input("\n\nPress the enter key to exit.")
