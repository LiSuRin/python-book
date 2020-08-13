# Дорабоать функцию ask_number(), добавив новый параметр - шаг. Шаг должен быть = 1.


def ask_number(question, low, high, step):
    response = None
    while response not in range(low, high, step):
        response = int(input(question).lower())
    return response


ask_number(question='Введите число: ', low=0, high=9, step=1)