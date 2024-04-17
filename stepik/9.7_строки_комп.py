print('-------Функция ord --------'*2)

# Функция ord позволяет определить код некоторого символа в таблице символов Unicode.
# Аргументом данной функции является одиночный символ.

# Результатом выполнения следующего кода:

# num1 = ord('A')
# num2 = ord('B')
# num3 = ord('a') 

# print(num1, num2, num3)

# #будет: 65 66 97

# print('-------Функция chr  --------'*2)

# # Функция chr позволяет определить по коду символа сам символ.
# # Аргументом данной функции является численный код.

# # Результатом выполнения следующего кода:

# chr1 = chr(65)
# chr2 = chr(75)
# chr3 = chr(110) 
# print(chr1, chr2, chr3)
# #будет: A K n

# for i in range(26):
#     print(chr(ord('A') + i))

# print(ord('f'))
# print(ord('o'))

# print('-1-'*30)

# a = 65
# b = 70

# for i in range(a , b +1):
#     print(chr(i),end=' ')

# print()
# print('-2-'*30)

# st = input()

# for i in st:
    
#     print(ord(i), end=' ')

print()
print('-3-'*30)
# 97, 122

n = 1

st = 'bwfusvfupdbftbs'

for i in st:
     st_1 = ord(i)
    
     if st_1 - n < 97:
        st_1 = 122 - (96 - st_1 + n)

        print(chr(st_1), end='')

     else:
         
         print(chr(st_1 - n), end='')