# Кто твой папа?
who_u_dad = {'Anton': 'Konstantin V', 'Polina': 'Kostya Melkiy', 'Olesia': 'Vladimir K.'}

print("""
    Игра - Кто твой Папа!
    Вы можете выбрать имя из списка,
    чтобы узнать кто отец или добавить свои вариант пары значений:
    """)

while True:

    print("""\t===Меню===
    0. Выход из программы.
    1. Вывести список всех имен
    2. Ввести имя, чтобы узнать Отца.
    3. Добавить свой вариант 
    """)

    choice = input('Ваш выбор: ')

    if choice == '1':
        print('Досутпны слудующие именя:', list(who_u_dad.keys()))
    elif choice == '2':
        name = input('Ввидите имя: ')
        if name in who_u_dad:
            print(name, 'отец -', who_u_dad[name])
        else:
            print('Такого имени нет в словаре... Попробуйте еще раз.')
    elif choice == '3':
        name = input('Ввидите имя сына: ')
        if name not in who_u_dad:
            father_name = input('Ввидите имя отца: ')
            who_u_dad[name] = father_name
        else:
            print('Такое имя уже есть в словарие, попробуйте еще раз.')
    elif choice == '0':
        break
    else:
        print('Упс...! Такого пунтка меня нет, попробуйте еще раз.')

print('Все возможные варианты -', list(who_u_dad.items()))
input('Нажмитие "Enter", чтобы выйти из игры...')