#Дано: 2 случайных числа.
#Задание: написать программу, которая будет печать результат целочисленного деления этих чисел,
# а также остаток от деления первого от второго.

print('Задание 2')
from random import randint

first_number = randint(0, 100)
print("first_number =", first_number)
second_number = randint(0, 100)
print("second_number =", second_number)
#Результат целочисленного деления этих чисел
print("Integer division = ", first_number//second_number)
#Остаток от деления первого от второго
print("Remainder of the division = ", first_number%second_number)
