
# Модуль math – один из наиважнейших в Python. 
# Этот модуль предоставляет обширный функционал
# для проведения вычислений с вещественными числами (числами с плавающей точкой


import math

num1 = math.sqrt(2)     # вычисление квадратного корня из двух
num2 = math.ceil(3.8)   # округление числа вверх
num3 = math.floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

from math import *#При таком способе подключения, импортируются абсолютно все функции модуля math.

num1 = sqrt(2)     # вычисление корня квадратного из двух
num2 = ceil(3.8)   # округление числа вверх
num3 = floor(3.8)  # округление числа вниз

print(num1)
print(num2)
print(num3)

print(' 1 ' *30)


# from math import *

# x1 = float(input('x1'))
# y1 = float(input('y1'))
# x2 = float(input('x2'))
# y2 = float(input('y2'))
# num1 = (x1 - x2)**2
# num2 = (y1 - y2)**2
# num3 = num1 + num2
# p = sqrt(num3)
# print(p)

print(' 2 ' *30)


# from math import *

# a = 1.0
# b = 2.0
# num1 = (a ** 2 +  b ** 2) / 2
# print((a + b ) / 2 )
# print(sqrt(a * b))
# print((2*a*b) / (a + b))
# print(sqrt(num1))

print(' 3 ' *30)

# Напишите программу, вычисляющую значение тригонометрического выражения
# sin + cos +tan 2 sinx+cosx+tan 2 x


# from math import *

# x = radians(float(input()))

# print(sin(x) + cos(x) + tan(x)**2)



# x = float(input())

# adians_1 = (x * pi) / 180 # это тоже самое что функция radians()

# print(sin(adians_1 ) + cos(adians_1 ) + tan(adians_1 )**2)

print(' 4 ' *30)

# Напишите программу, вычисляющую значение 
# ⌈x⌉ + ⌊x⌋     ⌈x⌉ +⌊x⌋ по заданному вещественному числу x.

# from math import *
# x = float(input())

# num1 = ceil(x)   # округление числа вверх
# num2 = floor(x)  # округление числа вниз

# print(num1 + num2)


print(' 5 ' *30)

# from math import *

# a = float(input())
# b = float(input())
# c = float(input())

# diskrim = b**2 - 4*a*c
# if diskrim > 0:
#     x1 = (-b + sqrt(diskrim)) / (2*a)
#     x2 = (-b - sqrt(diskrim)) / (2*a)
#     min1 = min(x1,x2)
#     max1 = max(x1,x2)
#     print(min1)
#     print(max1)
    
# elif diskrim == 0:
#     x3 = -b/ (2*a)
#     print(x3)
# else:
#     print('Нет корней')

print(' 6 ' *30)

# Правильный многоугольник — выпуклый многоугольник,
# у которого равны все стороны и все углы между смежными сторонами. 
# Площадь правильного многоугольника с длиной стороны 
# �
# a и количеством сторон n вычисляется по формуле: 


# from math import *

# n = 3
# a = 2.0

# num1 = n * (a**2)
# num2 = 4*tan(pi / n)
# s = num1 / num2

# print(s)
