# num = int(input())
# has_seven = False  # сигнальная метка

# while num != 0:
#     last_digit = num % 10
#     if last_digit == 7:
#         has_seven = True
#     num = num // 10

# if has_seven == True:
#     print('YES')
# else:
#     print('NO')



print('-1-'*30)

# Дано натуральное число. Напишите программу,
# которая выводит его цифры в столбик в обратном порядке.

# n = int(input())

# totl = 0

# while n !=0:
#     nuw_n = n %10
#     totl = nuw_n
#     n = n //10
#     print(totl)

# n = int(input())
# totl = 0
# while n!= 0:
#     nuw_n = n % 10
#     totl = nuw_n
#     n = n //10
#     print(totl, end='')


print('-2-'*30)


# totl = 0
# max1 = 0
# min1 =900 
# n = int(input())
# while n !=0:
#     nuw_n = n % 10
#     totl = nuw_n
    
#     if totl > max1:
#          max1 = totl
#     else:
#         totl < min1
#         min1 = totl
#     n = n//10
  
# print('Максимальная цифра равна',max1)
# print('Минимальная цифра равна', min1)



print('-3-'*30)

# Дано натуральное число. Напишите программу, которая вычисляет:

# сумму его цифр;
# количество цифр в нем;
# произведение его цифр;
# среднее арифметическое его цифр;
# его первую цифру;
# сумму его первой и последней цифры.


# n = int(input())
# sum1 = 0
# count1 = 0
# proizved = 1
# sred_arif = 0



# num = n % 10# последняя цифра не в теле цикла
# while n != 0:
#     nuw_n = n % 10
    
    
#     first_number = n % 10   # первая цифра в теле цикла 
#     sum1 +=nuw_n
#     count1+=1
#     proizved *= nuw_n
#     n = n //10
   


# print(sum1)
# print(count1)
# print(proizved )
# print(sum1/count1)
# print(first_number)
# print(num + first_number)

print('-4-'*30)
# Дано натуральное число n(n>9). Напишите программу,
# которая определяет его вторую (с начала) цифру.


# n = int(input())

# while n > 9:
        
#         nuw_n = n %10
#         n = n // 10
        
#print(nuw_n) 

print('-5-'*30)



# n = int(input())
# num = n % 10# последняя цифра не в теле цикла
# print(num)
# flag = True

# while n != 0:
    
#     numbers = n % 10   # первая цифра в теле цикла   
#     print(numbers)
#     if  num != numbers:
#         flag = False
#  #       break # брейк нужен что бы цикл остоновился на цыфре не равной текущей
#     n = n // 10
    
# if flag == True :  
#     print('YES')
# else:
#     print('NO')

print('-6-'*30)

# Дано натуральное число. Напишите программу,
# которая определяет, является ли последовательность
# его цифр при просмотре справа налево упорядоченной по неубыванию.



# n = int(input())
# flag = True
# while n >= 10:
#     num_2 = n % 10  # последняя
#     num_1 = n %100//10  # предпоследняя
#     if num_2 > num_1:
#       flag = False
#       break 
#     n = n//10
# if flag == True:
#    print('YES')
# else:
#    print('NO')
