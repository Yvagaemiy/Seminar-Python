# Задача №33. Решение в группах
# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
print('____вариант 1_________________________________________')
from random import randint
import time

list_1 = [randint(1, 5) for _ in range(int(input('Введите количество цифр: ')))]
print(list_1)

start_time = time.time()

min_1 = min(list_1)
max_1 = max(list_1)

for i in range(len(list_1)):#получаем индексы
     if list_1[i] == max_1:
        list_1[i] = min_1
#     if list_1[i] == min_1:
#        list_1[i] = max_1

print(list_1)

end_time = time.time()
print(end_time - start_time)

print('____вариант 2_________________________________________')
from random import randint
import time
list_1 = [randint(1, 5) for _ in range(int(input('Введите количество цифр: ')))]
print(list_1)

start_time = time.time()

min_1 = list_1[0]
max_1 = list_1[0]
list_max_num = [0]
for i in range(1, len(list_1)):#получаем индексы
    if list_1[i] > max_1:
        max_1= list_1[i]
        list_max_num = [i]

    elif list_1[i] == max_1:
        list_max_num.append(i)

    if list_1[i] < min_1:
        min_1 = list_1[i]

for i in list_max_num:
    list_1[i] = min_1

print(list_1)

end_time = time.time()
print(end_time - start_time)