# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
#  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9
print('____вариант с автотестов______')
arr = [5, 8, 6, 4, 9, 2, 7, 3]
arr_count = list()
for i in range(len(arr) - 1):
    arr_count.append(arr[i - 1] + arr[i] + arr[i + 1])
arr_count.append(arr[-2] + arr[-1] + arr[0])

# Вывод максимальной урожайности, которую может собрать собирающий модуль
print(max(arr_count))


#from random import randint
# n = int(input('Введите количество кустов: '))
# res = 0
# while n != 0 :
#     res = res + n
#     n = n - 1
#     print(n, end=' ')


# from random import randint
# list_1 = list(randint(1, 5) for i in range(int(input("Введите кол-во кустов: "))))

# #list_1 = [1,2,3,4,6,8,7,5,9,5,3,2,4]
# print(list_1)
# #a = 4
# a = int(input('Введите № куста: '))
# res = 0


# if a == len(list_1):
#     res = list_1[-1] + list_1[-2] + list_1[-3]
#     print(res)
# elif a == 1:
#     res = list_1[0] + list_1[1] + list_1[-1]
#     print(res)

# else:
#     res = list_1[a-1] + list_1[a-2] + list_1[a]
#     print(res)
# print(res, 'ягод')


from random import randint

list_1 = list(randint(1,9) for i in range(int(input("Введите количество кустов: "))))
print(list_1)

a = int(input("Введите номер куста: "))
res = 0
for i in list_1:
 #   print(list_1)
    if len(list_1) == 3:
        res = list_1[0] + list_1 [1] + list_1 [2]
    elif len(list_1) >=4 or len(list_1) <=1000:
        res = list_1[a-1]+ list_1[a-2]+ list_1[a-3]
#        print(res)
    else:
        print("кустов больше 1001")
print(res)