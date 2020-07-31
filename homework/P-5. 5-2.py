# Создать словарь
# Написать меню действий
# Выполнять программу, пока ответ пользователя не будет "выход" и не закончатся очки
# Для каждого действия в меню создать цикл с пользовательским вводом

print('Генератор персонажей игры\n',
	"""
		'У вас есть 30 зарядов, которые можно распределить на: 

		1 - Strength
		2 - Health
		3 - Wisdom
		4 - Sleight
	"""
	)
score = 30
new_score = ''
board = {'Strength': 0,
		'Health': 0, 
		'Wisdom': 0, 
		'Sleight': 0}
overall_choice = None
choice = None

while overall_choice != 0:
	print(
		"""
		Что вы хотите сделать?

		0 - Выход
		1 - Добавить очки к любой характеристике на выбор
		2 - Удалить очки из характеристики
		3 - Закончить распределение очков
		"""
	)
	overall_choice = int(input('Ваш выбор: '))
	if overall_choice == '0':
		print('До свидания!')
	elif overall_choice == '1' and score > 0:
		print(
		"""
		Куда вы хотите добавить очки?:

		1 - Strength
		2 - Health
		3 - Wisdom
		4 - Sleight
		"""
		)
		choice = int(input('Ваш выбор: '))
		if choice == '1':
			new_score = (input('Сколько очков вы хотите добавить?: '))
			if new_score <= score:
				board['Strength'] += int(new_score)
			else:
				print('Недостаточное количество очков.')
		elif choice == '2':
			new_score = (input('Сколько очков вы хотите добавить?: '))
			if new_score <= score:
				board['Health'] += int(new_score)
			else:
				print('Недостаточное количество очков.')
		elif choice == '3':
			new_score = (input('Сколько очков вы хотите добавить?: '))
			if new_score <= score:
				board['Wisdom'] += int(new_score)
			else:
				print('Недостаточное количество очков.')
		elif choice == '4':
			new_score = (input('Сколько очков вы хотите добавить?: '))
			if new_score <= score:
				board['Sleight'] += new_score
			else:
				print('Недостаточное количество очков.')
	elif overall_choice == '2' and score > 0:
		print(
		"""
		Из какой характеристики вы хотите убрать очки?:

		1 - Strength
		2 - Health
		3 - Wisdom
		4 - Sleight
		"""
		)
		choice = int(input('Ваш выбор: '))
		if choice == '1':
			new_score = (input('Сколько очков вы хотите убрать?: '))
			if new_score >= 0 and (['Strength'] - new_score) >= 0:
				board['Strength'] -= new_score
			else:
				print('Недостаточное количество очков.')
		if choice == '2':
			new_score = (input('Сколько очков вы хотите убрать?: '))
			if new_score >= 0 and (['Health'] - new_score) >= 0:
				board['Health'] -= new_score
			else:
				print('Недостаточное количество очков.')
		if choice == '3':
			new_score = (input('Сколько очков вы хотите убрать?: '))
			if new_score >= 0 and (['Wisdom'] - new_score) >= 0:
				board['Wisdom'] -= new_score
			else:
				print('Недостаточное количество очков.')
		if choice == '4':
			new_score = (input('Сколько очков вы хотите убрать?: '))
			if new_score >= 0 and (['Sleight'] - new_score) >= 0:
				board['Sleight'] -= new_score
			else:
				print('Недостаточное количество очков.')
		elif overall_choice == '3':
			if score == 0:
				break
			else:
				print('Используйте оставшиеся очки!')