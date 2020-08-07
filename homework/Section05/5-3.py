family = {'Макар': 'Костя', 'Илья': 'Игорь', 'Боруто': 'Наруто'}
chill = ''
dad = ''
choice = ''

print(
	"""
	    --- Меню: ---
	    
	    0 - Выход
		1 - Узнать отца запрашиваемого
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
        chill = input('Введите имя человека, отца которого хотите узнать: ')
        if chill in family:
            print('Его отец: ', family[chill])
        else:
            print('Такого имени не существует')
    elif choice == 2:
        chill = input('Введите имя, которое хотите добавить: ')
        if chill not in family:
            dad = input('Введите имя отца: ')
            family[chill] = dad
        else:
            print('Такое имя уже существует.')
    elif choice == 3:
        chill = input('Введите имя, которое надо заменить: ')
        if chill in family:
            dad = input('Введите новое имя отца: ')
            family[chill] = dad
        else:
            print('Такого имени не существует.')
    elif choice == 4:
        chill = input('Введите имя, которое надо удалить: ')
        if chill in family:
            print('Пара', family.pop(chill), 'удалена')
        else:
            print('Такого имени не существует.')
    elif choice == 5:
        print(family)