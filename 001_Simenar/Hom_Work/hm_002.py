# Задача 2:
# Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
print('______вариант с автотестов__________________________________')
n = 123

n1 = n // 100 # Нахождение первой цифры числа
n2 = (n % 100) // 10 # Нахождение второй цифры числа
n3 = n % 10 # Нахождение третьей цифры числа
res = n1 + n2 + n3



print('______вариант 1_________________________________')

n = int(input("Введите число: "))
res = 0
while  n != 0:
    p = n % 10 
    res = res + p
    n = n //10
print("Сумма цыфр в числе = ",res)

print('__________________________') 
n = 123
n1 = n // 100 # Нахождение первой цифры числа
print(n1)
n2 = (n % 100) // 10 # Нахождение второй цифры числа
print(n2)
n3 = n % 10 # Нахождение третьей цифры числа
print(n3)
res1 = n1 + n2 + n3
print("Сумма цыфр в числе = ",res1)