# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8


num = int(input('Введите число: '))
x = 0
stepn = 2

for i in  range(num):
    x = stepn ** i
    if x < num:
        print(x , end='-')
