completing_the_operation = True
while completing_the_operation:
    first_number = float(input("Введите первое число: "))
    second_number = float(input("Введите второе число: "))
    while completing_the_operation:
        arithmetic_operation = str(input("Введите арифметическое действие для чисел, для выхода введите 0: "))
        if arithmetic_operation == "0":
            completing_the_operation = False
        elif arithmetic_operation == "+":
            sum_numbers = first_number + second_number
            print(f"Сумма чисел равна: {sum_numbers}")
            break
        elif arithmetic_operation == "-":
            subtraction = first_number - second_number
            print(f"Разность чисел равна: {subtraction}")
            break
        elif arithmetic_operation == "/" and second_number == 0:
            print("Деление на ноль невозможно, повторите ввод с самого начала!")
            break
        elif arithmetic_operation == "/":
            division = first_number / second_number
            print(f"Частное этих чисел равно: {division}")
            break
        elif arithmetic_operation == "*":
            composition = first_number * second_number
            print(f"Произведение этих чисел равно: {composition}")
            break
        else:
            print("Вы ввели неверный символ, повторите ввод!")
