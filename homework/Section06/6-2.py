import random

print(
    """
        Добро пожаловать в игру 'Угадай слово'!
        Вы можете попробовать угадать слово, на это дано 5 попыток. 
        Вы можете проверять, есть ли буква в слове.
    """
)
WORDS = ('Корея', 'Школа', 'Компьютер', 'Черешня')
word = random.choice(WORDS)


def ask_number(low=0, high=5):
    tries = 0
    while tries in range(low, high):
        response = input('Попробуйте угадать слово из ' + str(len(word)) + ' букв:')
        tries += 1
        if response in word:
            print('Да!')
        else:
            print('Нет!')
    response = input('Попробуйте угадать слово из ' + str(len(word)) + ' букв:')
    if response == word:
        print('Поздравляю, вы выиграли!')
        break
    return response
ask_number()
if response != word:
    print('Вы проиграли, попробуйте еще раз!')