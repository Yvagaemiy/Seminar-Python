# Две старушки идут навстречу друг другу с постоянными скоростями 1V 1 и 2V 2
#   км/ч. Определите, через какое время (в часах) старушки встретятся, если расстояние между ними равно S км.

# v1 = float(input())
# v2 = float(input())
# s = float(input())
# t2 = v1 / (s + v2) # формула бабок
# print(t2)


print('_____________________________________________________________')

# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. 
# Если при этом введённое с клавиатуры число – ноль, 
# то вывести «Обратного числа не существует» (без кавычек).


# a = float(input())
# if a !=0:
#     f = 1/a
#     print(f)
# else: 
#     print('Обратного числа не существует')
print('_____________________________________________________________')

# У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». 
# Напишите программу, которая определяет, какой температуре по шкале Цельсия соответствует
# указанное значение по шкале Фаренгейта.

# Используйте формулу для перевода: C=5/9(F - 32)
# f = float(input())

# c = 5/9*(f-32)

# print(c)



print('_____________________________________________________________')

# На вход программе подается число 
# �
# n – количество собачьих лет. Напишите программу, 
# которая вычисляет возраст собаки в человеческих годах по следующему алгоритму: 
# в течение первых двух лет собачий год равен 
# 10.5
# 10.5 человеческим годам, после этого каждый год собаки равен 
# 4
# 4 человеческим годам.

# n = float(input())

# a = 10.5
# b = 21.0
# c = 4.0

# if n == 1:
#     print(a)
# elif n == 2:
#     print(b)
# else:
#     print(c* (n - 2)+b)

print('_____________________________________________________________')

# Дано положительное действительное число.
# Выведите его первую цифру после десятичной точки.

# Sample Input 1:    3384390.4339
# Sample Output 1:   4


# n = float(input())

# b = int(n * 10)

# c = b % 10

# print(c)

print('_____________________________________________________________')

# Дано положительное действительное число. Выведите его дробную часть.

# Sample Input 1:   44.45
# Sample Output 1:   0.45


# n = float(input())

# b =  n % 1
# print(b)

print('_____________________________________________________________')


# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел.
# Sample Input 1:

# 1
# 2
# 3
# 4
# 5
# Sample Output 1:

# Наименьшее число = 1
# Наибольшее число = 5

# n = float(input())
# n1 = float(input())
# n2 = float(input())
# n3 = float(input())
# n4 = float(input())


# print('Наименьшее число =' ,int(min(n,n1,n2,n3,n4)))
# print('Наибольшее число =' ,int(max(n,n1,n2,n3,n4)))

print('_____________________________________________________________')

# Напишите программу, которая упорядочивает три числа от большего к меньшему.

# Sample Input 1:

# 132
# 129
# 135
# Sample Output 1:

# 135
# 132
# 129

# n1 = int(input())
# n2 = int(input())
# n3 = int(input())
# a = max(n1,n2,n3)
# b = min(n1,n2,n3)
# c = (n1 + n2 + n3) - (a + b)
# print(a, c , b,sep='\n')

print('_____________________________________________________________')

# Назовем число интересным, если в нем разность максимальной
# и минимальной цифры равняется средней по величине цифре. 
# Напишите программу, которая определяет, интересное число или нет.
# Если число интересное, следует вывести «Число интересное»,
# иначе - «Число неинтересное».

# Sample Input 1: 945
# Sample Output 1: Число интересное
# Sample Input 2: 123
# Sample Output 2: Число интересное


# n = 945

# a = n //100
# b = n // 10 % 10
# c = n % 10
# print(a,b,c,sep='\n')
# a1 = max(a, b, c)

# b1 = min(a, b, c)

# c1 = a1 - b1

# if c1 == (a + b + c) - (a1 + b1):
#     print('Число интересное')
# else:
#     print('Число неинтересное')

print('-' *50)


# Напишите программу, которая вычисляет сумму их модулей 



# a1 = 45.5757
# a2 = 0.5675754
# a3 = -34545457
# a4 = -45.5675856
# a5 = 4.656856

# print(abs(a1)+abs(a2)+abs(a3)+abs(a4)+abs(a5))#Очень хитрый abs() если abs(a1)+abs(a2), 
#                                               #то каждое число модуль, а если abs(a1 + a2), то модуль суммы.


# p1 = int(input())
# q1 = int(input())
# p2 = int(input())
# q2 = int(input())

# a = abs(p1 - p2)
# b = abs(q1 - q2)
# print(a + b)

