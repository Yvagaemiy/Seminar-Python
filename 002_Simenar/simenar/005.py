# Задача №15.
#  Иван Васильевич пришел на рынок и решил 
# купить два арбуза: один для себя, а другой для тещи. 
# Понятно, что для себя нужно выбрать арбуз 
# потяжелей, а для тещи полегче. Но вот незадача: 
# арбузов слишком много и он не знает как же выбрать 
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9
 
import random
 
weight_3  = int(input('Введите количество арбузов : '))
min_x = weight_3  # необходимо поставить либо  weight либо от 10-до безконечности что бы можно было сравнивать для нахождения минимального  числа
max_x = 0

for i in range( weight_3 ):
    weight_3 = random.randint(3, 10)
    print( weight_3 , end =' ')
    
    if  weight_3 > max_x:
       max_x = weight_3
       
    if  weight_3 < min_x:
        min_x = weight_3
    
print()
print ('Min = ',min_x,',','Max = ' ,max_x )   
 
 
print('_Вариант №2 с сименара_____________________________')

from random import randint
num_1 = randint(1, 15)
print('Кол-во арбузов = ',num_1) 
min_z = weight_3
max_z = weight_3

for _ in range(num_1 -1):# нижнее подчеркивание если переменная i не будет использоваться в коде
        weight_3 = randint (3, 10) 
        print(weight_3, end='  ') 
        
        if  weight_3 > max_z:
           max_z = weight_3
           
        if  weight_3 < min_z:
           min_z = weight_3 
           
print()
print ('Min = ',min_z,',','Max = ' ,max_z ) 



print('_Вариант №3 с сименара___функция vin and max___________________') 
  
from random import randint

num_1 = randint(1, 15)
print('Кол-во арбузов = ',num_1)
 
min_z = weight_3
max_z = weight_3

for _ in range(num_1 ):# нижнее подчеркивание если переменная i не будет использоваться в коде
        weight_3 = randint (3, 10) 
        print(weight_3, end='  ') 
        min_z = min(min_z , weight_3)
        max_z = max(max_z , weight_3)
           
print()
print ('Min = ',min_z,',','Max = ' ,max_z )    