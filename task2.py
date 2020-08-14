input_information = int(input("Введите время в секундах: "))
seconds = input_information % 60
minutes = input_information // 60 % 60
hours = input_information // 3600 % 24
print(f"Время: {hours}:{minutes}:{seconds}")
