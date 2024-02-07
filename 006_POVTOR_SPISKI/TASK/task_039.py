# Задача №39. Решение в группах
# Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. Пользователь вводит 
# число N - количество элементов в первом массиве, затем N
# чисел - элементы массива. Затем число M - количество
# элементов во втором массиве. Затем элементы второго массива
# Ввод: Вывод:
# 7 3 3 2 12
# 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1 (каждое число вводится с новой строки)
from random import randint


def get_array(mas):
    # res = []
    # for _ in range(mas):
    #     res.append(randint(1, 10))
    # return []

    return [randint(1,20) for _ in range(mas)]# без [] таких скобок не получалось!!!

def dev_arr(arra_1, arra_2):
    # res = []
    # for num in arra_1:
    #     if num not in arra_2:
    #         res.append(num)
    #     return []
    return[num for num in arra_1 if num not in arra_2]



array_1 = int(input('Введите длину массива 1: '))
array_2 = int(input('Введите длину массива 2: '))

arra_1 = get_array(array_1)
arra_2 = get_array(array_2)

print(arra_1)
print(arra_2)

#res = arra_1.(arra_2)
res_array = dev_arr(arra_1,arra_2)
print(res_array)
