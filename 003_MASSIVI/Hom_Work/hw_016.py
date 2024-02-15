# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих 
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
# 5
# 1 2 3 4 5
# 3
# -> 1
print('____Ввариант с Автотестов_________________________')

list_1 = [3, 2, 3, 4, 5]
k = 3

# Введите ваше решение ниже

count = 0
for i in range(len(list_1)):
    if list_1[i] == k:
        count += 1
print(count)




print('____Ввариант МОЙ_________________________')

from random import randint

x = randint(4,6)
print('Введите длену массива: ',x)

# for _ in range(x):
#     array = randint(1, 6)
#     print(array , end= ' ')
nuw_array = [randint(1, 6) for _ in range(x)]
print(nuw_array)

y = randint(1, 6)
print()
print('Проверяем если в массиве: ',y)
count = 0
for i in range(len(nuw_array)):
     if nuw_array[i] == y:
      count = count + 1
res = [1 for i in range(len(nuw_array))  if nuw_array[i] == y ]     
print (f'{res}')

print ()   

print ('Кол-во совподений = ',count)
     
