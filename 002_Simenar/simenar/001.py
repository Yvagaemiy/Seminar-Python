# Задача №9.
# По данному целому неотрицательному n вычислите 
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех 
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл 
# while
# Input: 5
# Output: 120

print('__Вариант№1_____________')

x = input('Ведите число:  ')

while not x.isdigit() or x == 0:
    print('Вы ввели не цыфру')
    x = input('Ведите число:  ')
    
x = int(x)
fakt = 1
num = 1    

while num <= x:
    fakt = fakt * num
    
    num = num + 1
print(x,'!','=',fakt)

print('__Вариант№2_____________')
fak = 1
  
while x > 1:
       fak = fak * x
       x = x - 1 
          
print(x,"!","=",fak) 
print('__Вариант№3_____________')

n = 5
f = 1
  
while n > 1:
        f = f * n
        n = n - 1 
          
print(n,"!","=",f) 

print('___Вариант№4____________')


n = 5
f = 1

for i in range(1 , n+1):
    f = f * i
    
print(n,"!","=",f) 