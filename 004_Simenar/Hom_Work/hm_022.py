# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
from random import randint

n_1 = {randint(1 , 20) for _ in range(int(input('Введите 1 множиство: ')))} 
print(n_1) 
print(type(n_1))

 
m_1 = {randint(1 , 20) for _ in range(int(input('Введите 2 множиство: ')))}     
print(m_1) 
print(type(m_1)) 

print()

res = n_1.intersection(m_1)
print(*res)