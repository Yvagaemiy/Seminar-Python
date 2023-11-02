# Задача №11. 
# Дано натуральное число A > 1. Определите, каким по 
# счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не 
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

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

print('_______________')

n_0 = 0 #(n-1)
n_1 = 0 #(n-2)
a = 5    #(n-1)+(num-2)
counter = 1
resalt = 0
while (resalt < a):
    n_0 = n_1
    n_1 = resalt
    counter = counter+1
print(resalt) 
if resalt == a:
    print(counter)
else:
    print(-1) 