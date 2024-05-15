
print('-1-'*30)

# Заменил второй элемент списка на 17;
# Добавил числа 4, 5 и 6 в конец списка;
# Удалил первый элемент списка;
# Удвоил список;
# Вставил число 25 по индексу 3;
# Вывел список, с помощью функции print()

numbers = [8, 9, 10, 11]

numbers[1]= 17
numbers.insert(9,4)
numbers.insert(9,5)
numbers.insert(9,6)
numbers.pop(0)
numbers = numbers*2
numbers.insert(3, 25)
print(numbers)

print('-2-'*30)


# На вход программе подается строка текста, содержащая различные натуральные числа.
# Вам необходимо переставить максимальный и минимальный элементы местами и вывести измененную строку.

# spis = '2 3 4 5 6'.split()
# #spis = []
# # for i in st:
# #     spis.append(int(i))


# st_min = min(spis)
# st_max = max(spis)

# st_min_indix = spis.index(st_min)
# st_max_indix = spis.index(st_max)  

# spis[st_min_indix],spis[st_max_indix] = spis[st_max_indix],spis[st_min_indix] 
# print(*spis)

print('-3-'*30)

# spis = 'A William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful, and were enjoyed both by the common people of London and also by the rich and famous. In addition to his plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today.'.split()

# count = 0
# for i in spis:
  
#     if 'a' ==i.lower() or  'an' ==i.lower() or  'the' ==i.lower():
#         count+=1
# print('Общее количество артиклей:',count)

print('-4-'*30)

# n = input()

# n = int(n[1:])

# for _ in range(n):
#     x = input()
#     if '#' in x:
#         x = x[: x.find('#')]
#     print(x.rstrip())

print('-5-'*30)

# На вход программе подается строка текста,
# содержащая целые числа. Из данной строки формируется список чисел. 
# Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, 
# а затем по убыванию. 
# вариант1
# st = [5 ,3 ,7 ,29 ,1]
# st.sort()
# st1 = st.copy()
# st1.sort(reverse=True)
# print(*st)
# print(*st1)
#Вариант2
# st = '5 3 7 29 1'.split()
# sp1 = []
# for i in st:
#     print(i)
#     sp1.append(int(i))
# sp1.sort()
# print(sp1)
# sp1.sort(reverse=True)
# print(sp1)
