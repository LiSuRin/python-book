# Игра распределение характеристик персонажа

print(
    """
    Распределение характеристик персонажа:
        - У вас 30 очков характеристик
        - Вы можете распределять их между Силой, Здоровьем, Мудростью и Локвостью
    """
)

stat_points = 30
characteristics = {'power': 0, 'health': 0, 'intellect': 0, 'agility': 0}

while stat_points:
    print(
        """
                --Меню--
        Выберете один из пунктов:
        0. Выход из игры
        1. Вывод общего списка характеристик
        2. Добавить очки характеристики
        3. Отнять очки характеристики
        """
    )
    choice = input('Ваш выбор: ')

    if choice == '0':
        break
    elif choice == '1':
        print('\nВсего доступных очков:', stat_points)
        print('Вы распределили очки следующим образом:', list(characteristics.items()))
    elif choice == '2':
        print('\nхарактеристики - ', list(characteristics.keys()))
        char = input('Выберите характеристику: ')
        points = int(input('Выберите количество очков: '))
        if char in characteristics and points <= stat_points:
            characteristics[char] += points
            stat_points -= points
        else:
            print('Такой характеристики нет или у вас недостаточно очков.')
    elif choice == '3':
        print('характеристики - ', list(characteristics.keys()))
        char = input('Выберете характеристику: ')
        points = int(input('Выберете количество очков: '))
        if char in characteristics and points <= characteristics[char]:
            characteristics[char] -= points
            stat_points += points
        else:
            print('Такой характеристики нет или у вас недостаточно очков.')
    else:
        print('Такого пункта меню нет. Попробуйте еще раз.')

print('Вы распределили очки следующим образом:\n\t', list(characteristics.items()))
input('Нажмитие "Enter", чтобы выйти из игры...')
