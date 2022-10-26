#Дано: число с плавающей точкой.
#Задание: написать программу, которая будет округлять заданное число:
#1) 2х знаков после запятой; 2) до целого; 3) дополнять слева столько нулей, сколько не хватает числу до 11 знаков.

print('Задание 3')
import random

random_number = random.uniform(0, 100)
print("random_number =", random_number)

#1) 2х знаков после запятой;
print("rounding to 2 decimal places = ", ('{0:.2f}'.format(random_number)))
#2) до целого;
print("rounding to integer = ", ('{0:.0f}'.format(random_number)))
#3) дополнять слева столько нулей, сколько не хватает числу до 11 знаков.
new_random_number = float('{0:.5}'.format(random_number))
print("zeros to eleven digits 1var = ", f'{new_random_number:011}')
max_width = 11
print("zeros to eleven digits 2var = ", f'{new_random_number:0{max_width}}')

