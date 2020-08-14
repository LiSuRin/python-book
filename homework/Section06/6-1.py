# Дорабоать функцию ask_number(), добавив новый параметр - шаг. Шаг должен быть = 1.


def ask_number(question, low=None, high=None, step=1):
    response = None
    while response not in range(low, high, step):
        response = int(input(question))
    return response


print(ask_number(question='Сделайте ход в промежутке от 0 до 8: ', low=0, high=8))