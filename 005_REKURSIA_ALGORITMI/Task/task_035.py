# Задача №35. Решение в группах
# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes

def simpi_num(numbers):
    if numbers % 2 == 0 and numbers != 2:
        return False
    for dev in range(3, int(numbers ** 0,5) + 1, 2):# умножили на 1/2 отсекли половину , 
                                                 #renge работает только с int поэтому numbers приводим к int, 
                                                 #а + 1 чтобы взять последнee число
    #for dev in range(2, numbers): вариант с сименара
        if numbers % dev == 0 :
            return False
    return True

def check_num(numbers):
    if numbers.isdigit() and int(numbers) > 1:
        return True
    return False


num = input('Введите число: ')

while not  check_num(num):
    print("не корр4ектный ввод")
    num = input('Введите число: ')

num = int(num)   
print(simpi_num(num))
print("Yes" if simpi_num(num) else "No")