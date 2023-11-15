# Задача №11. 
# Дано натуральное число A > 1. Определите, каким по 
# счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не 
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6
print('___Вариант№ 1 ____________')
a = input('Ведите число:  ')

while not a.isdigit() or a == 0 or a ==1:
    print('Вы ввели не цыфру')
    a = input('Ведите число:  ')
    
a = int(a)   #(n-1)+(num-2)
fib_1 = 1     #(n-1)
fib_2 = 1      #(n-2)
pos = 3

while  fib_1 < a  :
    fib_1 = fib_2
    fib_2 = pos
    pos = pos + 1
    
if fib_1 !=a:
    print(-1)
else:        
    print(pos -1) # не понятный эфект


print('___Вариант№ 2 c сименара____________')

a = input('Ведите число:  ')

while not a.isdigit() or a == 0 or a ==1:
    print('Вы ввели не цыфру')
    a = input('Ведите число:  ')
    
a = int(a) 
pos = 3
num_1 = 1
num_2 = 1
while num_1 < a:
    num_1, num_2 = num_1 + num_2 , num_1 # кортеж массива
    pos = pos + 1
if num_1 !=a:
    print(-1)
else:
    print(pos)







print('___Вариант№ 3____________')
n = 5
def Fibo(n):
   if n <=2:
           return 1
   else:
       return Fibo(n-1)+Fibo(n-2)
for i in range(1, n+2):
    print(Fibo(i ))
if n < 0:
    print('-1')

print('___Вариант№ 4__не работает__________')


a = 5    #(n-1)+(num-2)
n_1 = 0  #(n-1)
n_2 = 0  #(n-2)
resalt = 1

while (n_1 < a):
    n_1 = n_2
    n_2 = resalt
    resalt = resalt + 1

if n_1 != a:
    print(-1) 
else:
    print(resalt - 1)  # не понятный эфект