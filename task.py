
# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.

# *Пример:*

# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8 


def power(first_num, second_num):
    if second_num == 1:
        return first_number
    if second_number == 0:
        return 1

    return int(first_num) * power(int(first_num), int(second_num) -1)

first_number = int(input("введите число: "))
second_number = int(input("Введите в какую степень требуеться возвести: "))
    
print(f"A = {first_number}; b = {second_number} => {power(first_number, second_number)}")







############################


