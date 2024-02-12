# Задача №45. Решение в группах
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105
# . Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод: 300    
# Вывод:   220 284
# пример из сименара возьмем два числа 220 и 284. найдем их делитель.
# Делитель 220(1,2,4,5,10,11,20,22,44,55,110)
# сумма их = 1+2+4,5,10,11,20,22,44,55,110 = 284
# Делитель 284(1,2,4,71,142)
# сумма их = 1+2+4+71+142 = 220
# print('______вариант с сименара 1_______________________________________')
# def get_summ_dev(n):
#     sum_dev = 0
#     for div in range( 1, n ):
#         if n % div == 0:
#            sum_dev += div
#     return sum_dev

# def check_frend_num(m):
#     for first_num in range(2 , m):
#         secont_num = get_summ_dev(first_num)
#         if first_num < secont_num and get_summ_dev(secont_num) ==  first_num :
#             print(first_num , secont_num )


# k = int(input('Введите число: '))
# check_frend_num(k)



print('______вариант с сименара 2_код быстрее______________________________________')

def get_summ_dev(n):
    sum_dev = 0
    swrt_num = int(n ** 0.5)
    for div in range(2, swrt_num ):
        if n % div == 0:
           sum_dev += div + n // div
    if swrt_num == n ** 0.5:
        sum_dev += swrt_num
    
    return sum_dev

def check_frend_num(m):
    for first_num in range(2 , m):
        secont_num = get_summ_dev(first_num)
        if first_num < secont_num and get_summ_dev(secont_num) ==  first_num :
            print(first_num , secont_num )


k = int(input('Введите число: '))
check_frend_num(k)

print('______вариант лекции видео______________________________________')

k = int(input())

list1 = list()

for i in range(k):
    summa = 0
    for j in range(1 , i // 2 + 1):
        if i % j == 0:
           summa += j
    list1.append(tuple([i , summa]))
#print(list1)

for i in range(len(list1)):
    for j in range(i , len(list1)):
        if i != j and list1[i][0] == list1[j][1] and list1[i][1] == list1[j][0]:
            print(*list1[i])
