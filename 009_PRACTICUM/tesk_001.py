#вариант 1 мой
num = list(range(1,101))
num_chet = []
num_cub = []
sum_cub = 0
for i in num:
    if i % 2== 0:
        num_chet.append(i**2)
   
for j in num_chet:
#    if j % 3 ==0:
        num_cub.append(j**3)
for k in   num_cub:
     if k % 3 ==0:
         sum_cub +=k       

print(sum_cub )

#Вариант 2
squaret_num = [ i**2   for i in range(2,101,2)]
cubed_num = [ i**3  for i in  squaret_num if i % 3==0 ]
print(sum(cubed_num))