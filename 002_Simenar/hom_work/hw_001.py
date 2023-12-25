# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.
# 5 -> 1 0 1 1 0
# 2
print('______вариант с автотестов__________________________________')

coins = [0, 1, 0, 1, 1, 1]

count_zero = 0
count_one = 0

for coin in coins:
    if coin == 0:
        count_zero += 1
    else:
        count_one += 1

if count_one > count_zero:
    print(count_zero)
else:
    print(count_one)


print('__Вариантv №1 с сименара рабочий_____________')   

coins = [0, 1, 0, 1, 1, 1]

mi = 0 
ma = 0

for i in coins:
    if i == 0 :
        mi = mi + 1
    else:
        ma = ma + 1
print(min(mi, ma))    





print('__Вариантv №2 рабочий_____________')   

import random

num = int(input('Введите ко-во манеток : '))
zero = 0
one = 0

for i in range(num):
    animal = random.randint(0, 1)
    print(animal,end=' ')
    print()       
    if  animal == 1:
        one = one + 1   
          
    else:
        zero = zero + 1
        
if zero > one:
    print('Надо перевернуть ', one, 'орла на решки')
 
elif zero == one:
    print('Ни чья!!! ') 
    
else:
    print('Надо перевернуть ', zero,'решки на орла')
    
    
print('__Вариант с интернета___из группы_____________')      



    
    
print('__Вариант с интернета________________')   
   
N = int(input('Введите количество монет '))
orel = reshka = 0
for i in range(N):
    x = int(input('Орел(1) или решка(0)? '))
    if x == 1:
        orel += 1
    else:
        reshka += 1
if orel < reshka:
    print(f'Переверните {orel} монет с орла на решку, их меньше всего')
elif orel == reshka:
    print(f'Количество орлов и решек одинаково, по {orel} штук')
else:
    print((f'Переверните {reshka} монет с решки на орла, их меньше всего'))
    
    
    
    
print('__Вариантv №1 не очень рабочий_____________')   
coins = [1, 1, 1, 0, 0, 1]

n = len(coins)
rez_1 = 0
rez_2 = 0
for i in range(1, n):
    if n > 1:
        rez_1 = rez_1 + 1
    else:
        rez_2 = rez_2 + 1
if rez_1 > rez_2:
    print(rez_2)
elif  rez_1 == rez_2:   
    print(rez_1) 
else:
    print(rez_1) 
    
    
coins = [0, 1, 0, 1, 1, 0]

n = len(coins)
rez = 0
for i in len(coins):
   if coins[i] != coins[i - 1]:
    rez = rez + 1
print(f'{rez}')   
            