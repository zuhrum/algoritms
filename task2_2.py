number_entered = int(input("Введите число: "))
number = number_entered
count_even_number = 0
count_odd_number = 0
while number > 0:
    remainder_of_division = number % 10
    integer_division = number // 10
    number = integer_division
    if remainder_of_division % 2 == 0:
        count_even_number += 1
    else:
        count_odd_number += 1

print(f"В числе {number_entered}, {count_even_number} чётных чисел(а) и {count_odd_number} нечётных чисел(а)")
