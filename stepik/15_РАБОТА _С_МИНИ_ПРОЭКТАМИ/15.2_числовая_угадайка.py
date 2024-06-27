

# Тимур загадал число от 1 до n (включительно). 
# За какое наименьшее количество вопросов (на которые Тимур отвечает                       
# "больше" или "меньше") Руслан может гарантированно угадать число Тимура?

# import random


# print('Добро пожаловать в числовую угадайку')

# def  is_valid(num):
#     while num < 1 or num > 100 :
        
#             print('вы ввели не правельное число')
#             num = int(input('загадайте число: '))

# n = int(input('загадайте число: '))
# is_valid(n)


# left = 1
# riqht = 100

# x = random.randint(left, riqht)
# print('рандомное число х = ',x)

# middel = (left + riqht) // 2
# count = 0
# while middel != x:
      

#     if middel > x:
#       print('Ваше число меньше загаданного, попробуйте еще разок')
#       riqht = middel - 1
#       middel = (left + riqht) // 2
#       count+=1

#     if middel < x:
#       print('Ваше число больше загаданного, попробуйте еще разок')
#       left = middel + 1
#       middel = (left + riqht) // 2
#       count+=1

   
# print('Количество попыток = ',count)

# my_bool = True
# my_num = 7gghrt
# print( my_num + my_bool)

# spis = {}

# a_1 = input('первый ключ: ')
# a_2 = input('первае значение: ')

# spis[a_1] = [a_2]
# print(spis)

# b_1 = input('второй ключ: ')
# b_2 = input('второе значение: ')

# spis[b_1] = [b_2]
# print(spis)

# c_1 = input('третий ключ: ')
# c_2 = input('третье значение: ')


# spis[c_1] = [c_2]
# print(spis)


from math import *

n = int(input())

print(ceil(log (n, 2)))