# Задача №13.
# Уставшие от необычно теплой зимы, жители решили узнать, 
# действительно ли это самая длинная оттепель за всю историю 
# наблюдений за погодой. Они обратились к синоптикам, а те, в 
# свою очередь, занялись исследованиями статистики за 
# прошлые годы. Их интересует, сколько дней длилась самая 
# длинная оттепель. Оттепелью они называют период, в 
# который среднесуточная температура ежедневно превышала 
# 0 градусов Цельсия. Напишите программу, помогающую 
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2




# Вариант с сименара №1

import random

day = int(input('Введите кол-во дней : '))

max_day = 0
count_day = 0

for i in range(day):
    temper = random.randint(-50, 50)
    print(temper, end=' ')
    if temper > 0:
        count_day = count_day + 1
    else:
        if count_day > max_day:
           max_day = count_day
           count_day =0
print()           
print(f'{max_day = }')

print('_____________________________________')
    
 # Вариант с сименара №2
        
import random

days = int(input('Введите кол-во дней : '))

max_days = 0
count_days = 0

for i in range(days):
    temper = int(input('Введите температуру'))
    if temper > 0:
        count_days = count_days + 1
    
        if count_days > max_days:
           max_days = count_days
          
    else:
        count_days =0
            
print()           
print(f'{max_days = }')  


print('_____________________________________') 


 
        
import  random

n = int(input('Ввидите количество дней: '))

print( random.randrange(-1, n))


import random

print("Генерация случайного числа в пределах заданного промежутка")
print(random.randint(-10, 50)) 


import random
 
 
print("Генерация случайного числа в пределах заданного промежутка")
print(random.randrange(10, 50, 5))
print(random.randrange(10, 50, 5))

#import numpy

#random_integer_array = numpy.random.random_integers(1, 10, 5)
#print("1-мерный массив случайных целых чисел \n", random_integer_array,"\n")