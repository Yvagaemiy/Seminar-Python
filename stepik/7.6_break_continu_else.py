print('-1-'*30)


# num = int(input())
# flag = True

# for i in range(2, num):
#     if num % i == 0:        #  если исходное число делится на какое-либо отличное от 1 и самого себя
#         flag = False
#         break               # останавливаем цикл если встретили делитель числа        

# if flag:  # эквивалентно if flag == True:
#     print('Число простое')
# else:
#     print('Число составное')



# n = int(input())
# num = n
# flag = True

# while n != 0:
#     nuw_n = n % 10
#     if nuw_n == 7:
#         flag = False
#         break
#     n = n //10
# if flag == True:
#     print('в числе',num,'нет 7')
# else:
#     print('в числе',num,'есть 7')


# for i in range(1, 101):
#     if i == 7 or i == 17 or i == 29 or i == 78:
#         continue  # переходим на следующую итерацию пропускаем 7, 17, 29, 78
#     print(i, end=',')



# for i in range(10):
#     print(i, end='*')
#     if i > 6:
#         break

# i = 100
# while i > 0:
#     if i == 40:
#         break
#     print(i, end='*')
#     i = i - 20


# n = 10
# while n > 0:
#     n -= 1
#     if n == 2:
#         continue
#     print(n, end='*')


# result = 0
# for i in range(10):
#     if i % 2 == 0:
#         continue
#     result += i

# print(result)

# mult = 1
# for i in range(1, 11):
 
#    if i % 2 == 0:
#       continue
#    if i % 9 == 0:
#       break
#    mult *= i
# print(mult)


print('-2-'*30)

# На вход программе подается число 
# n>1. Напишите программу, которая выводит его наименьший отличный от 
# 1 делитель.

# n = int(input())

# for i in range(n+1):
#     i = i + 1
#     if n % i == 0 and i > 1:
#         print(i)
#         break
    

n = int(input())


for i in range(1,n+1):
   if 5<= i <=9 or 78 <= i <=87 or 17 <= i <= 37:
        continue
   print(i)