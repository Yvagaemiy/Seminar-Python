# Задача 26: Напишите программу, которая на вход принимает 
# два числа A и B, и возводит число А в целую степень B с 
# помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8


# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.
# Функция не должна ничего выводить, только возвращать значение.

# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8 
print('_____ВАРИАНТ С АВТОТЕСТОВ___________________________________________-')
a = 3
b = 5


def f(a, b):
  if b == 0:
    return 1
  return f(a, b - 1) * a

print(f(a,b))# в атотестах не используется принт

print('______мой вариант_______________________________________')
def degree(a, b):
    if a == 0 or b== 0:
        return 1
    else:
        return a * degree(a, b - 1)
    
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

print(degree(a, b))
