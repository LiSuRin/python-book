family = {'Макар': ['Костя', 'Владимир'], 'Илья': ['Игорь', 'Леонид'], 'Боруто': ['Наруто', 'Минато']}
chill = ''
dad = ''
grandpa = ''
choice = ''

print(
    """
        --- Меню: ---

        0 - Выход
        1 - Узнать отца и деда запрашиваемого
        2 - Добавить данные
        3 - Изменить данные
        4 - Удалить данные
        5 - Вывести результат
    """)
while choice != 0:
    choice = int(input('Введите ваш выбор: '))
    if choice == 0:
        print('До свидания!')
    elif choice == 1:
        chill = input('Введите имя человека, отца и деда которого хотите узнать: ')
        if chill in family:
            adult = input('Введите "Отец" или "Дед", чтоб продолжить:')
            if adult == 'Отец':
                print('Его отец: ', family[chill])
            else:
                print('Его дед: ', family[chill][1])
        else:
            print('Такого имени не существует')
    elif choice == 2:
        chill = input('Введите имя, которое хотите добавить: ')
        if chill not in family:
            dad = input('Введите имя отца: ')
            grandpa = input('Введите имя деда: ')
            family[chill] = [dad, grandpa]
        else:
            print('Такое имя уже существует.')
    elif choice == 3:
        chill = input('Введите имя, которое надо заменить: ')
        if chill in family:
            dad = input('Введите новое имя отца: ')
            grandpa = input('Введите новое имя деда: ')
            family[chill] = [dad, grandpa]
        else:
            print('Такого имени не существует.')
    elif choice == 4:
        chill = input('Введите имя, которое надо удалить: ')
        if chill in family:
            print('Пара', chill, family[chill], 'удалена')
            del family[chill]
        else:
            print('Такого имени не существует.')
    elif choice == 5:
        print(family)