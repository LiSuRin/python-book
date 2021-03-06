import random


"""
Создайте игру, в которой компьютер выбирает какое-то слово, а игрок должен отгадать. Компьютер сообщает игроку, 
сколько букв в слове, и дает 5 попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать 
только "да" и "нет". Вслед за этим игрок должен попробовать отгадать слово. 

1. Поприветстовать игрока при входе в игру и объяснить правила игры
2. Создадим список слов, из которого случайно выберем слово
3. Выполнять программу, пока попытки не будут больше или равны 1 или человек не угадает слово (while, or)
	- запросить пользовательский ввод
    - если буква есть в слове
        - сообщаем "Да" 
    - если буквы нет в слове
        - сообщаем "нет"
    - отнимаем 1 попытку
    - если слово равно ориг.слову
	    - поздравить пользователя и прервать цикл
4. Сообщить пользователю о его проигрыше
"""

print(
    """
        Добро пожаловать в игру 'Угадай слово'!
        Вы можете попробовать угадать слово, на это дано 5 попыток. 
        Вы можете проверять, есть ли буква в слове.
    """
)
WORDS = ('Корея', 'Школа', 'Компьютер', 'Черешня')
word = random.choice(WORDS)
tries = 4
response = input('Попробуйте угадать слово из ' + str(len(word)) + ' букв:')

while tries >= 1 and response != word:
    if response in word:
        print('Да!')
    else:
        print('Нет!')
    tries -= 1
    response = input('Попробуйте угадать слово из ' + str(len(word)) + ' букв:')
    if response == word:
        print('Поздравляю, вы выиграли!')
        break
else:
    print('Вы проиграли, попробуйте снова!')
