


# # объявление функции
# def draw_triangle(fill, base):
 
#     for i in range(base//2+2):
        
#             print(fill * i)
   
    
#     for j in range(base//2, 0,-1):
       
#             print(fill *j)



# # считываем данные
# fill = input()
# base = int(input())

# # вызываем функцию
# draw_triangle(fill, base)


# def print_fio(name, surname, patronymic):

#         print(name[0].capitalize()+ surname[0].upper()+ patronymic[0].upper())
   
# # считываем данные
# name, surname, patronymic = 'Aлександр', 'Иванов', 'Дмитреевич'

# # вызываем функцию
# print_fio(name, surname, patronymic)


# def print_digit_sum(num):
#     count =0
#     while num > 0:
#         sum_1 = num % 10 
#         count += sum_1
#         num = num // 10
#     print(count)
    
# # считываем данные
# n = int(input())
# print_digit_sum(n)



# n = 123
# count =0
# while n > 0:
#     sum_1 = n % 10 
#     count += sum_1
#     n = n // 10
# print(count)

# n = 123
# for i in range(1,n+1):
#     print(i)

x = 5

def add():
    global x
    x = 3
    x = x + 5
    print(x)

add()
print(x)