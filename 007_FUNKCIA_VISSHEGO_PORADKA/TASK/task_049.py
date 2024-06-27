# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам. 
# Назовем самой далекой планетой ту, орбита которой имеет 
# самую большую площадь. Напишите функцию 
# find_farthest_orbit(list_of_orbits), которая среди списка орбит 
# планет найдет ту, по которой вращается самая далекая 
# планета. Круговые орбиты не учитывайте: вы знаете, что у 
# вашей звезды таких планет нет, зато искусственные спутники 
# были были запущены на круговые орбиты. Результатом 
# функции должен быть кортеж, содержащий длины полуосей 
# эллипса орбиты самой далекой планеты. Каждая орбита 
# представляет из себя кортеж из пары чисел - полуосей ее 
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b, 
# где a и b - длины полуосей эллипса. При решении задачи 
# используйте списочные выражения. Подсказка: проще всего 
# будет найти эллипс в два шага: сначала вычислить самую 
# большую площадь эллипса, а затем найти и сам эллипс, 
# имеющий такую площадь. Гарантируется, что самая далекая 
# планета ровно одна
# Пример ввода и вывода данных представлены на
# следующем слайде
# 20 минут
# Семинар 7. Функции высшего порядка
# Задача №49. Решение в группах
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

from math import pi

print('_____вариант с сименарам 1______________________________________________-')

def find_farthest_orbit(list_of_orbits):
    max_s = 0
    for a, b in list_of_orbits:
#        print(a , b, end=' ')
        s = pi * a * b
        if a != b and s > max_s:
           max_s = s
           res = a ,b
    return res

orbits_1 = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits_1))

print('_____вариант с сименарам 2______________________________________________-')

def find_farthest_orbit(list_of_orbits):
    list_of_orbits = list(filter(lambda sazes: sazes[0] != sazes[1] ,list_of_orbits))# фильтруем круг
    list_max_orbits = [pi * a * b for a, b in list_of_orbits]# зи списка картежей считаем площади
    max_orbits = max(list_max_orbits) # переменная определяет мах площадь
    i_max_orbits = list_max_orbits.index(max_orbits) # переменная находит из списка list_max_orbits индексы мах площади
    return list_of_orbits[i_max_orbits] # возврощаем список с мах площадью индекс переведенную вскартеж
#    return [list_of_orbits[i] for i in range(len(list_of_orbits)) if list_max_orbits[i] == max_orbits][0] #  [0] - что бы распокавать 
                                                                                                           # картеж от скобок!!!!                      

orbits_2 = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits_2))


print('_____вариант с лекции с видео______________________________________________-')



def find_farthest_orbit(list_of_orbits):
    list1 = [i for i in list_of_orbits if i[0] != i[1]]# функция котороя избовляется от круга
    print(list1)
    list_s = [(pi * i[0] *i[1])for i in list1] # функция которая ищит площадь
    print(list_s)
    max_s = list_s.index(max(list_s)) # переменная которая через функцию мах ищит максимальную площадь и индекс из списка list_s
    #                                                                                     и возврощает индек максимального числа
    print(max_s)
    return list1[max_s]
   
orbits_3 = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits_3))