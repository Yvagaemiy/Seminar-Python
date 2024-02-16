# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: Вывод:
# print_operation_table(lambda x, y: x * y) 1 2 3 4 5 6 
#  2 4 6 8 10 12
#  3 6 9 12 15 18
#  4 8 12 16 20 24
#  5 10 15 20 25 30
#  6 12 18 24 30 36

print('____ВАРИАНТ С АВТОТЕСТОВ_________________________________-')


def print_operation_table(operation, num_rows=6, num_columns=6):
    result = []
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1, num_rows + 1):
            for j in range(1, num_columns + 1):
                if j != num_columns :
                    result.append(f'{operation(i, j)} ')
                else:
                    result.append(operation(i, j))
            result.append('\n')
        print(''.join([str(i) for i in result[:len(result) - 1]]))
        
print_operation_table(lambda x, y: x * y, 3, 3)

print('______мой вариант__________________________________')

def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows +1):
        a = []
        for j in range(1, num_columns +1):
            a.append(str(operation(i, j)))# обязательно конвертировать в str иначе Join не получится
        print("   ".join(a)) #join при конвертации списка в строку.
       # vowels = ["a", "e", "i", "o", "u"]
       # vowels_str = ",".join(vowels)
       # print("Строка гласных:", vowels_str)

print_operation_table(lambda x, y: x * y, 3 , 3)

print('_____вариант с интернета_1_________________________________________-')

def print_operation_table(operation, num_rows, num_columns):
   
        
    res = [[operation(row, col) for row in range(1, num_columns + 1)] for col in range(1, num_rows + 1)]

    for i in res:
        #print(*[f"{x} " for x in i])
        print(*i)


print_operation_table(lambda x, y: x * y, 6, 6)


print('_____вариант с интернета_2_не работает________________________________________-')

def print_operation_table(operation, num_rows, num_columns):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"ОШИБКА! Размерности таблицы должны быть больше 2!" for x in i])


print_operation_table(lambda x, y: x * y, 3, 3)

def print_operation_table(operation, num_rows, num_columns):
    if num_rows<2:
        print("ОШИБКА! Размерности таблицы должны быть больше 2!")
        return
    res = [[operation(row, col) for row in range(1, num_columns + 1)] for col in range(1, num_rows + 1)]

    for i in res:
        print(*[f"{x} " for x in i])
