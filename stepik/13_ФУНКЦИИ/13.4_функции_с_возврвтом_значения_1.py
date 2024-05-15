print('-1-'*30)

# Напишите функцию convert_to_miles(km), которая принимает в 
# качестве аргумента расстояние в километрах и возвращает 
# расстояние в милях. Формула для преобразования: мили = километры * 0.6214.

# def convert_to_miles(km):
#     mili = km * 0.6214
#     return mili

# # считываем данные
# num = int(input())

# # вызываем функцию
# print(convert_to_miles(num))

print('-2-'*30)
# Напишите функцию get_days(month),
# которая принимает в качестве аргумента 
# номер месяца и возвращает количество дней в данном месяце.


# def get_days(month):
#     if month == 1:
#         return 31 
#     if month == 2:
#         return 28
#     if month == 3:
#         return 31 
#     if month == 4:
#         return 30
#     if month == 5:
#         return 31 
#     if month == 6:
#         return 30
#     if month == 7:
#         return 31 
#     if month == 8:
#         return 31
#     if month == 9:
#         return 30 
#     if month == 10:
#         return 31
#     if month == 11:
#         return 30 
#     else:   
#         return 31

# # считываем данные
# num = int(input())

# # вызываем функцию
# print(get_days(num))

print('-3-'*30)

# Напишите функцию get_factors(num), принимающую
# в качестве аргумента натуральное число и возвращающую
# список всех делителей данного числа.

# def get_factors(num):
      
#     a = [int(num / i) for i in range(num,0,-1) if num % i == 0]
#     return a 
# # считываем данные
# n = int(input())
# # вызываем функцию
# print(get_factors(n))

#вариант 2
# def get_factors(num):     
#     a = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             a.append(i)
#     return a 
# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_factors(n))

print('-3-'*30)
# Напишите функцию number_of_factors(num), принимающую в
# качестве аргумента число и возвращающую количество делителей данного числа.

# def number_of_factors(num):
#     a = 0
#     for i in range(1, num +1):
#         if num % i == 0:          
#             a +=1
#     return a
# # считываем данные
# n = int(input())
# # вызываем функцию
# print(number_of_factors(n))

print('-4-'*30)

# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку target 
# и символ symbol и возвращает список, содержащий все местоположения этого символа в строке.



# def find_all(target, symbol):
#     s_1 = []
#     for i in range(len(target)):
#         if target[i] == symbol:
#             s_1.append(i)
#     return s_1
# # считываем данные
# s = input()
# char = input()

# # вызываем функцию
# print(find_all(s, char))


print('-5-'*30)
# Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два отсортированных по 
# возрастанию списка, состоящих из целых чисел, и объединяет их в один отсортированный список.


# def merge(list1, list2):
   
#     list3 = list1 + list2 
#     list3.sort()
#     return sorted(list3)
# # считываем данные
# numbers1 = [int(c) for c in input().split()]
# numbers2 = [int(c) for c in input().split()]

# # вызываем функцию
# print(merge(numbers1, numbers2))


print('-5-'*30)

# На вход программе подается натуральное число n, а затем 
# n строк, содержащих целые числа в порядке возрастания, разделенные символом пробела.




def quick_merge(list1, list2):
    result = []

    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]
    return result
list1 = []
for _ in range(int(input())):
    list2 = [int(i) for i in input().split()]
    result = quick_merge(list1, list2)
    list1 = result
print(*result)    