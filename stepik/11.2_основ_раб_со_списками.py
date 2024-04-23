# list.append(x)Добавляет элемент в конец списка

# list.extend(L)Расширяет список list, добавляя в конец все элементы списка L

# list.insert(i, x)Вставляет на i-ый элемент значение x

# list.remove(x)Удаляет первый элемент в списке, имеющий значение x. ValueError, если такого элемента не существует

# list.pop([i])Удаляет i-ый элемент и возвращает его. Если индекс не указан, удаляется последний элемент

# list.index(x, [start [, end]])Возвращает положение первого элемента со значением x (при этом поиск ведется от start до end)

# list.count(x)Возвращает количество элементов со значением x

# list.sort([key=функция])Сортирует список на основе функции

# list.reverse()Разворачивает список

# list.copy()Поверхностная копия списка

# list.clear()Очищает список



# primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

# print(primes[17])


# numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]
# a = max(numbers)
# print(a)
# b =  min(numbers)
# print(b)

# print(a +b)

print('-1-'*30)


# чтобы элемент списка имеющий значение Green заменился 
# на значение Зеленый, а элемент Violet на Фиолетовый

# rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

# #rainbow[3:-1]= ['Зеленый', 'Фиолетовый'] 
# for i in range(len(rainbow)):
#     if rainbow[i] =='Green':
#         rainbow[i] = 'Зеленый'
    
#     if rainbow[i] =='Violet':
#         rainbow[i] = 'Фиолетовый'

# print(rainbow)

print('-2-'*30)

# languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 'Japanese', 'Lahnda']

# print(languages[::-1])


print('-3-'*30)

numbers1 = [1, 2, 3]
numbers2 = [6]
numbers3 = [7, 8, 9, 10, 11, 12, 13]

print(numbers1 * 2 + numbers2 *9 + numbers3 )