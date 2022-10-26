#Дано: 3 случайных числа.
#Задание: написать программу, которая будет вычислять среднее значение этих чисел.
#Пример: (52 + 56 + 60) / 3 = 56

print('Задание 1')

from random import randint

first_number = randint(0, 100)
print("first_number =", first_number)
second_number = randint(0, 100)
print("second_number =", second_number)
third_number = randint(0, 100)
print("third_numberr =", third_number)

average = (first_number+second_number+third_number)/3
print("Average =", '{0:.2f}'.format(average))