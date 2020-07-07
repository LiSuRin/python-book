#Автодиллер

car_cost = input('Введите стоймость автомобиля:')
print(car_cost)

#Доп.суммы

tax = (int(car_cost) * 0.1)
registration_fee = (int(car_cost) * 0.1)
agency_fee = 10000
shipping_cost = 56000

final_price = (tax + registration_fee + agency_fee + shipping_cost + int(car_cost))

print('\n' + str(tax) + '\n' + str(registration_fee) + '\n' + str(agency_fee) + '\n' + str(shipping_cost) +'\n' + str(car_cost))
print(final_price)

input("\n\nНажмите Enter, чтобы выйти.")