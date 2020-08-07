#симулятор пирожка с "сюрпризом"
import random

print('Привет!Это программа симулятор пирожка с "сюрпризом".\nСейчас будет выбран случайный сюрприз!')

surprise = random.randint(1, 5)

if surprise == 1:
	print('\nПоздравляю, вы выиграли автомобиль!')

elif surprise == 2:
	print('\nПоздравляю, вы выиграли 100000 рублей!')

elif surprise == 3:
	print('\nПоздравляю, вы выиграли планшет для рисования!')

elif surprise == 4:
	print('\nПоздравляю, вы выиграли новый Iphone 11 Pro')

elif surprise == 5:
	print('\nПоздравляю, вы выиграли Iphone 11')


input('\n\nНажмите Enter, чтобы выйти.')
