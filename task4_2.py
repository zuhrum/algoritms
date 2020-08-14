def func(first_number, n):
    if n == 1:
        return first_number

    else:
        return func(first_number + 1 / ((-2) ** (n - 1)), n - 1)


quantity = int(input("Введите количество элементов последовательности: "))
print(func(1, quantity))
