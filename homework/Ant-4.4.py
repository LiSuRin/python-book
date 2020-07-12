import random

WORDS = ('Apple', 'Microsoft', 'Google', 'Telegram')
word = random.choice(WORDS)
tries = 0

guess = input('Отгадайте слово из '+str(len(word))+' букв:')
while guess != word and tries <= 5:
    if guess in word:
        print('Да, такая буква есть, попробуйте отнадать слово...')
    else:
        print('Нет такой буквы в слове')
    guess = input('Отгадайте слово из ' + str(len(word)) + ' букв:')
    tries += 1
    if guess == word:
        print('Поздравляю, вы выграли!!!')
        break
else:
    print('Вы проиграли, ваши попытки закончились.')
