print('-1-'*30)



# Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает 
# в качестве аргументов координаты концов отрезка 
#  и возвращает координаты точки являющейся серединой данного отрезка.

# def get_middle_point(x1, y1, x2, y2):
#     x = (x1 + x2) / 2
#     y = (y1 + y2) / 2
#     return x , y

# # считываем данные
# x_1, y_1 = int(input()), int(input())
# x_2, y_2 = int(input()), int(input())

# # вызываем функцию
# x, y = get_middle_point(x_1, y_1, x_2, y_2)
# print(x, y)

print('-2-'*30)
#С=2πr, S=πr*2


# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и возвращает
# два значения: длину окружности и площадь круга, ограниченного данной окружностью.


# from math  import pi

# def get_circle(radius):
#     С = 2 * pi * radius
#     S = pi * (radius**2)
#     return С, S

# # считываем данные
# r = float(input())

# # вызываем функцию
# length, square = get_circle(r)
# print(length, square)



print('-3-'*30)
# Напишите функцию solve(a, b, c), которая принимает в качестве 
# аргументов три целых числа a, b, c – коэффициенты квадратного уравнения 
# +bx+c=0 и возвращает его корни в порядке возрастания.
#   ax**2 + bx + c = 0
# from math import *
# def solve(a, b, c):
#     D = b**2 - 4 * a  * c
  
#     x_1 = (-b + sqrt(D)) / (2 * a)
#     x_2 = (-b - sqrt(D))/ (2 * a)
#     if D == 0:
#         return x_1, x_2
#     else:
#         if x_1 >= x_2:
#             return  x_2,x_1
#         else:
#             return x_1, x_2


# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# x1, x2 = solve(a, b, c)
# print(x1, x2)