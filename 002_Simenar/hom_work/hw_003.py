# Задача 14:
# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k
# ), не превосходящие числа N.
# 10 -> 1 2 4 8
print('__Вариант с сименара ________________') 
n = 16

a = 0 

while a < n + 1:
    
    print(a)
    a = a * 2



print('__Вариант 0 ________________')        
        
n = 16
x =0 


for i in  range( n ):
    x = 2 ** i
    if x <= n:
       
        print(x,end=' ')


print()
print('__Вариант№ 1________________')

n = 16
x =0


for i in  range(n):
    x = 2 ** i
    if x <= n:
        i = i +1
        print(x,end=' ')
        
print()
print('__Вариант№ 2________________')


num = int(input('Введите число: '))
x = 0
stepn = 2

for i in  range(num):
    x = stepn ** i
    if x <= num:
        print(x , end='-')
        
print()        
print('__Вариант с интернета________________')

N = abs(int(input('Введите число N: ')))
stop = 0
P = 2
for i in range(N):
    if stop != 1:
        P = P ** i
        if P <= N:
            print(P, end=' ')
            P = 2
        else:
            stop = 1
    else:
        i = N
        

               