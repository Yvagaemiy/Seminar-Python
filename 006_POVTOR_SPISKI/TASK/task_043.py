# адача №43. Решение в группах
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:         Вывод:
# 1 2 3 2 3       2
from random import randint

size = int(input('Введите длену массива: '))

arra = [randint(1, 9) for _ in range(size)]
print(arra)

count = 0
for i in range(size - 1):
    for j in range(i + 1 ,size):
        if arra[i] == arra[j]:
            count+=1

print(count)

print('_______вариант 2_________________')

count = 0

for num in set(arra):
    count_num = arra.count(num)
    count = count + count_num * (count_num - 1) //2

print(num)