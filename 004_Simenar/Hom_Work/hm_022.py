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

print('___вариант с автотестов_____')
var1 = '5 4' 
var2 = '1 3 5 7 9' 
var3 = '2 3 4 5' 
mol = [int(x) for x in var1.split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [int(x) for x in var2.split()]
k = set(a)
for i in k:
   set_1.add(i)
b = [int(x) for x in var3.split()]
k1 = set(b)
for i in k1:
   set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
   print(i, end=' ')

print('_______мой вариант________')

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