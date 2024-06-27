# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая 
# проверяет, все ли объекты имеют одинаковое значение 
# некоторой характеристики, и возвращают True, если это так. 
# Если значение характеристики для разных объектов 
# отличается - то False. Для пустого набора объектов, функция 
# должна возвращать True. Аргумент characteristic - это 
# функция, которая принимает объект и вычисляет его 
# характеристику.
# Ввод: Вывод:
# def same_by(val):
#     if filter(lambda x: x % 2 == 0, val):
#         print('same')
#     else:
#         print('different') 
# values = [1, 21, 11, 7]
# same_by(values)
print('_____Вариант с сименара 1_________________________________________________________-')


def same_by_1(characteristic, objects):
    check = characteristic(objects[0]) # находим первое значение с 0 индексом
    for num in objects[1:]:    # проходм начиная с 1 индекса
        if  check != characteristic(num): 
            return False
    return True 
values = [0, 2, 10, 6]
if same_by_1(lambda x: x % 2 == 0,values):
     print('same')
else:
    print('different') 

print('_____Вариант с сименара 2_________________________________________________________-')


def same_by_2(characteristic, objects):
    res_set = {characteristic(num) for num in objects}
    if  len(res_set) <= 1:
            return True
    return False
values = [0, 2, 10, 6]
if same_by_2(lambda x: x % 2 == 0,values):
     print('same')
else:
    print('different')


print('_____Вариант с сименара 3_________________________________________________________-')


def same_by_3(characteristic, objects):
    result = list(filter(characteristic, objects))
    if  objects == result or not result:
            return True
    return False
values = [0, 2, 11, 6]
if same_by_3(lambda x: x % 2 == 0,values):
     print('same')
else:
    print('different')

print('_____Вариант с сименара 4_________________________________________________________-')

def same_by_4(characteristic, objects):
    result = list(map(characteristic, objects))
    if  all(result) == any(result):
            return True
    return False
values = [5, 21, 1, 3]
if same_by_4(lambda x: x % 2 == 0,values):
     print('same')
else:
    print('different')

 
print('_____Вариант с видео лекции_________________________________________________________-')   


def same_by(cfsgrthrt, sdvzdfgt):
    result = True
    list1 = [cfsgrthrt(x) for  x in sdvzdfgt]
    for i in range(len(list1) - 1):
        if list1[i] != list1[i + 1]:
            return False
    return result

v = [2,4,6,9]
if same_by(lambda x : x % 2 == 0 , v):
    print('same')
else:
    print('different')