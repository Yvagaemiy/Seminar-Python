
print('-1-'*30)

# Дополните приведенный код, так чтобы он вывел сумму квадратов элементов списка numbers.



# numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]
# summa = 0
# for i in numbers:
#     num = i **2
#     summa+=num
# print(summa)


print('-2-'*30)

# На вход программе подается натуральное число n, а затем 
# n целых чисел. Напишите программу, которая для каждого введенного числа 
# x выводит значение функции () f(x)=x ** 2+2x+1, каждое на отдельной строке.

# n = int(input())
# fun = []
# for i in range(n):
#     num = int(input())
#     print(num,sep='\n')
#     nuw_num = num ** 2 + 2 * num + 1
#     fun.append(nuw_num)
# print()
# print(*fun, sep='\n')


print('-3-'*30)


# На вход программе подается натуральное число n, а затем 
# n различных натуральных чисел. Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел,
# а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

# n = int(input())
# spis = []
# spis_1 =[]
# for i in range(n):
#     num = int(input())
#     spis.append(num)

# for j in spis:
#     if j != min(spis) and j != max(spis):
#         spis_1.append(j)
# print(*spis_1, sep='\n')  

print('-4-'*30) 


# На вход программе подается натуральное число n, а затем 
# n строк. Напишите программу, которая выводит только уникальные строки, 
# в том же порядке, в котором они были введены.

# num = int(input())
# spis = []
# #spis_1 = []
# for i in range(num):
#     wold = input()
    
#     if wold not in spis:
#         spis.append(wold)
# print(*spis, sep='\n')



print('-5-'*30)     

# На вход программе подается натуральное число n, затем 
# n строк, затем еще одна строка — поисковый запрос. Напишите программу, 
# которая выводит все введенные строки, в которых встречается поисковый запрос.


# num = int(input())
# spis = []

# for i in range(num):
#     word = input()
#     spis.append(word)
    
# word_2 = input() 
# for j in spis:
#    if word_2.lower() in j.lower() :
       
#     print(j)

print('-6-'*30) 

# На вход программе подается натуральное число n, затем n строк, затем число 
# k — количество поисковых запросов, затем k строк — поисковые запросы. Напишите программу,
# которая выводит все введенные строки, в которых встречаются одновременно все поисковые запросы.


# n = int(input())
# spis = []
# zapros = []
# counter = 0
# for _ in range(n):
#     spis.append(input())

# k = int(input())
# for _ in range(k):
#     zapros.append(input())

# for i in spis:
#     for j in zapros:
#           if j.lower() in i.lower():
#                 counter+=1
#     if counter == k:
#         print(i)
#     counter = 0
         
print('-7-'*30)            
#  На вход программе подается натуральное число n, а затем 
# n целых чисел. Напишите программу, которая сначала выводит все отрицательные числа,
# затем нули, а затем все положительные числа, каждое на отдельной строке. 
# Числа должны быть выведены в том же порядке, в котором они были введены.       

# n = int(input())
# sp_1 = []
# sp_2 = []
# sp_3 = []
# for i in range(n):
#    num = int(input())
#    if num < 0:
#       sp_1.append(num)
#    if num ==0:
#       sp_2.append(num)
#    if num > 0:
#       sp_3.append(num)

# print(*sp_1,sep='\n')
# print(*sp_2,sep='\n')
# print(*sp_3,sep='\n')









