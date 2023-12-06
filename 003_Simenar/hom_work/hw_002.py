# Задача 18: 
# Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
from random import randint
print('___Вариант с интернета_______________________________________________')
array_1 = [randint(1, 9) for i in range(int(input('Введите размер массива: ')))]
print(array_1)
num = int(input('Введите число Х: '))
if num > max(array_1):
    print(max(array_1))
else:
    print(min(array_1))    

print('___Вариант мой_______________________________________________')

x = randint(4,7)
print('Введите кол_во элементов массива: ',x) 
array = [randint(1, 9) for _ in range(x)]
print(array , end=' ')

print()
num_1 = int(input('Введите число Х: '))


if  num_1 > max(array):
    print(max(array))
else:
    print(min(array))    
        