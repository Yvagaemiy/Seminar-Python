# Задача №41. Общее обсуждение
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая в данном массиве определит
# количество элементов, у которых два соседних и, при
# этом, оба соседних элемента меньше данного. Сначала
# вводится число N — количество элементов в массиве 
# Далее записаны N чисел — элементы массива. Массив
# состоит из целых чисел.
# Ввод: 5            Ввод:5 
# 
# 1 2 3 4 5              1 5 1 5 1
# Вывод:0            Вывод: 2



from random import randint
# def arrya(numbers):
#     res = []
#     for i in range(numbers):
#         res.append(randint(1, 9))
#     return res
num = int(input('введите длину массива: '))  
arra = [randint(1,9) for i in range(num)]
print(arra)
count = 0
for num in range(len(arra)):
    if (arra[num - 1]) < arra[num] > (arra[num + 1]):
        count+=1
      
#print(arrya(num))
print(count)
print(sum([1 for num in range(len(arra)) if (arra[num - 1]) < arra[num] > (arra[num+ 1])]))