print('-1-'*30)

# Напишите функцию draw_triangle(), которая выводит звездный 
# равнобедренный треугольник с основанием и высотой равными 
# 15 и 8 соответственно:

# def draw_triangle():
#     for i in range(8):
#         print(' ' * (8 - 1 -i) + '*' * ( 1 + i * 2))
# # основная программа
# draw_triangle()  # вызов функции

print('-2-'*30)

# Интернет-магазин осуществляет экспресс доставку для 
# своих товаров по цене 1000 рублей за первый товар и 120
#  рублей за каждый последующий товар. Напишите функцию 
# get_shipping_cost(quantity), которая принимает в качестве
# аргумента натуральное число quantity – количество товаров 
# в заказе – и возвращает стоимость доставки.

# def get_shipping_cost(quantity):
#     first = 1000
#     next_erevel = 120
#     if quantity == 1:
#         return first
#     return first + next_erevel * (quantity - 1)
# # считываем данные
# n = int(input())
# # вызываем функцию
# print(get_shipping_cost(n))

print('-3-'*30)

# Напишите функцию compute_binom(n, k), которая принимает
# в качестве аргументов два натуральных числа n и k и возвращает
# значение биномиального коэффициента, равного 

# from math import *

# def compute_binom(n, k):
#     x = factorial(n) // (factorial(k)*(factorial(n - k)))
#     return x
# # считываем данные
# n = int(input())
# k = int(input())

# # вызываем функцию
# print(compute_binom(n, k))


print('-4-'*30)

# Напишите функцию number_to_words(num), которая принимает 
# в качествеаргумента натуральное число num и возвращает 
# его словесное описание на русском языке.

# def number_to_words(num):
#     list_1 = ['один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять','одиннадцать', 'двенадцать', 'тринадцать', 'четырнадцать', 'пятнадцать', 'шестнадцать', 'семнадцать', 'восемнадцать', 'девятнадцать','двадцать',' ']
#     list_2 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

#     if num <= 20:
#         return list_1[num - 1]
#     else:
#          return list_2[num // 10 - 2] +' ' + list_1[num % 10 - 1]

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(number_to_words(n))

print('-5-'*30)

# Напишите функцию get_month(language, number), которая принимает на вход
# два аргумента language – язык ru или en и number – номер месяца 
# (от 1 до 12) и возвращает название месяца на русском или английском языке.

# def get_month(language, number):
#     lng_ru = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

#     lng_en = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december'] 
   
#     if language == 'ru':
#         return lng_ru[number - 1]  
#     return lng_en[number - 1]
# # считываем данные
# lan = input()
# num = int(input())

# # вызываем функцию
# print(get_month(lan, num))

print('-6-'*30)

# Магическая дата – это дата, когда день, умноженный на месяц, равен числу, 
# образованному последними двумя цифрами года.
# Напишите функцию is_magic(date), которая принимает в качестве аргумента 
# строковое представление корректной даты и возвращает 
# значение True, если дата является магической и False - в противном случае.

# def is_magic(date):
#     date = date.split('.')
#     for _ in date:
#         x =int(date[2]) 
#         if int(date[0]) * int(date[1]) == x % 100:
#             return True
#         return False
# # считываем данные
# date = '11.06.1960'
# # вызываем функцию
# print(is_magic(date))


print('-7-'*30)
    
# Панграмма – это фраза, содержащая в себе все буквы алфавита.
# Обычно панграммы используют для презентации шрифтов, 
# чтобы можно было в одной фразе рассмотреть все глифы.
# Напишите функцию, is_pangram(text) которая принимает в
# качестве аргумента строку текста на английском языке и
# возвращает значение True если текст является панграммой 
# и False в противном случае.

# def is_pangram(text):
#     s = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#     text = text.replace(' ','')   # убрали пробелы
#     text = text.lower()           # перевели в нижний регистр
#     for i in s:
#         if i not in  text:
#             return False
#     return True
# # считываем данные
# text = 'jsdfhsadfhkljsad'

# # вызываем функцию
# print(is_pangram(text))



