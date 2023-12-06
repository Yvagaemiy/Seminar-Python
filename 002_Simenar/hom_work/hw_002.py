# Задача 12:
# Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.
# 4 4 -> 2 2
# 5 6 -> 2 3

print('__Вариант № 1 правельное решение_______________')
s = 12
p =27

for x in range(1 , 1000):
    y = s - x
    if x <= y and x* y ==p:
        print(x, y)

print('__Вариант № 2 правельное решение_______________')
s = 12
p =27

for x in range(s):
    for y in range(p):
      
        if x <= y and x*y ==p:
                
            print(f'x равен = "{x}", y равен =  "{y}"') 
            
            
print('__Вариант № 3 правельное решение_______________')

s = 12
p =27
for x in range(1, 1001):
     y = s - x
#    if x <= y and x * y == p:
     if x  <= 1000 and y <= 1000 and x * (s - x ) == p:    
            print (f'{x}, {y}')

print('__Вариант № 4 c сименара правельное решение_______________')

s = 12
p = 27

num_1 = 0
num_2 =0

for x in range(s):
    for y in range(s):
        if x + y == s and x * y ==p:
            num_1 = x
            num_2 = y
print(min(num_1, num_2), max (num_1, num_2)) 


print('__Вариант № 5 c сименара правельное решение_______________')

s = 12
p = 27

for virst in range(s // 2 + 1):
    second = s - virst
    if virst * second == p:
        break
print(virst, second)    

print('__Вариант № 6 c сименара правельное решение  но не работает_______________')

s = 12
p = 27

for virst_1 in range(int(p ** 0.5) +1):
    second_1 = p / virst_1
    if virst_1 + second_1 == s:
        break
print(virst_1, second_1)




x = int(input('Введите число x : '))
y =  int(input('Введите число y : '))
s = x + y
p = x * y
print('сумма чисел X и Y = ',s)
print('Произведение чисел X и Y = ',p)
print(s,p)

print('__Вариант с интернета_есть ошибка_______________')

x = abs(int(input('Введите первое натуральное число X ')))
y = abs(int(input('Введите второе натуральное число Y ')))
S = x + y
P = x * y
y1 = int((S + ((-S) ** 2 - 4 * P) ** 0.5) / 2)
x1 = int((S - ((-S) ** 2 - 4 * P) ** 0.5) / 2)
print(x1, y1)

print('__Вариант с интернета_есть ошибка_______________')


x = abs(int(input('Введите первое натуральное число X от 1 до 1000 ')))
y = abs(int(input('Введите второе натуральное число Y от 1 до 1000 ')))
if x < 1 or x > 1000 or y < 1 or y > 1000:
    print('Вы ввели число не из заданного диапазона!')
else:
    S = x + y
    P = x * y
    stop = 0
    for i in range(1001):
        if stop != 1:
            for j in range(1001):
                if stop != 1:
                    if i * j == P and i + j == S:
                        print(i, j)
                        stop = 1
            else:
                j = 1001
        else:
            i = 1001