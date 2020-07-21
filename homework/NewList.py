import random


# 1. Создать список слов и пустой список
# 2. Выполнять программу, пока не кончится список
# 		- случайным образом выбрать слово из списка
# 		- присвоить это слово в конец нового списка
# 		- создать срез последовательности в списке
# 3. Ввести на экран новый список

list = ['Лето', 'Солнце', 'Жара', 'Танцы', 'Музыка']
new_list = []

while list: 
	position = random.randrange(len(list))
	new_list.append(list[position])
	list = list[:position] + list[(position + 1):]
print(new_list)