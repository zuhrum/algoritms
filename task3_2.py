def func(number):
    if number // 10 == 0:
        return f"{number}"

    if number // 10 != 0:
        return f"{number % 10}{func(number // 10)}"


number_entered = int(input("Введите число: "))
print(int(func(number_entered)))
