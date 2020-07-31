# представить список слов
# выводить в случайном порядке и без повторений

import random

words = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
while words:
    print(words.pop(words.index(random.choice(words))))
