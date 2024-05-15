print('-1-'*30)

# Напишите функцию is_valid_triangle(side1, side2, side3), 
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение 
# True если существует невырожденный треугольник со сторонами side1, side2,
# side3 и False в противном случае.

# def is_valid_triangle(side1, side2, side3):
#     if side1 + side2 > side3 and side1 + side2 > side2 and side2 + side3 > side1:
#         return True
#     else:
#         return False

# # считываем данные
# a, b, c = int(input()), int(input()), int(input())

# # вызываем функцию
# print(is_valid_triangle(a, b, c))

print('-2-'*30)
# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число
# и возвращает значение True если число является простым и False в противном случае.

# def is_prime(num):
#     if num == 1:
#         return False
#     for i in range(2, num ):
       
#         if num % i == 0:     
                  
#             return False
#     else:
#         return True

# # считываем данные
# n = int(input())

# # вызываем функцию
# print(is_prime(n))

# n = int(input())

print('-2-'*30)

# Напишите функцию get_next_prime(num), которая принимает в качестве 
# аргумента натуральное число num и возвращает первое простое число большее числа num.


# def get_next_prime(num):
#     num +=1
#     for i in range(2, num ):
       
#         if num % i == 0:     
                  
#             return get_next_prime(num)
#     else:
#         return num 
    
# # считываем данные
# n = int(input())

# # вызываем функцию
# print(get_next_prime(n))

print('-3-'*30)

# Напишите функцию is_password_good(password), которая принимает 
# в качестве аргумента строковое значение пароля password и возвращает значение True,
# если пароль является надежным и False - в противном случае.

# Пароль является надежным если:

# его длина не менее 8 символов; 
# он содержит как минимум одну заглавную букву (верхний регистр); 
# он содержит как минимум одну строчную букву (нижний регистр);
# он содержит хотя бы одну цифру.

# def is_password_good(password):
#     for i in range(len(password)):
#         if len(password) == 8 and password == password.lower() and password == password.upper() and  password[i] in '0123456789':
#             return True
#     else:
#         return False    

# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_password_good(txt))
# # вариант_1
# def is_password_good(password):
#     if len(password) == 8:
#             return True


#     count_1 = 0
#     count_2 = 0
#     count_3 = 0
#     for i in password:
#         if i.isdigit() == True:
#             count_1+=1
#         if i.isupper() == True:
#             count_2 +=1
#         if i.islower() == True:
#             count_3 +=1
#             if count_1* count_2 * count_3 == 1:
#                 return True
#     else:
#         return False
              
# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_password_good(txt))


# вариант_2

# def is_password_good(password):
#     if len(password) < 8:
#           return  False
#     count_1 = False
#     count_2 = False
#     count_3 = False
#     for i in password:
        
#             if i.isupper():
#                 count_1 = True
#             elif i.islower():
#                 count_2 = True
#             elif i.isdigit():
#                 count_3 = True
#     return count_1 and count_2 and count_3       
# # считываем данные
# txt = input()
# # вызываем функцию
# print(is_password_good(txt))


print('-4-'*30)

# Напишите функцию is_one_away(word1, word2), которая принимает 
# в качестве аргументов два слова word1 и word2 и возвращает значение True, 
# если слова имеют одинаковую длину и отличаются ровно в одном символе и False 
# в противном случае

# def is_one_away(word1, word2):
    
#     count = 0
#     if len(word1) == (len(word2)):
#         for i in range(len(word1)):
#             if word1[i] == word2[i]:
#                 count +=1
#         if count + 1 == len(word1):
#                 return True    
   
#     return False
            

# # считываем данные
# txt1 = input()
# txt2 = input()

# # вызываем функцию
# print(is_one_away(txt1, txt2))

print('-5-'*30)



# Напишите функцию is_palindrome(text), которая принимает в 
# качестве аргумента строку text и возвращает значение True
# если указанный текст является палиндромом и False в противном случае.

# def is_palindrome(text):
#     znaki = [',', '.','!', '?' ,'-',' ']
#     for i in znaki:
#         text = text.replace(i, '')
#     text = text.lower()
#     return text == text[::-1]
# # считываем данные
# txt = 'Standart - smallest, sell Amstrad nats'

# # вызываем функцию
# print(is_palindrome(txt))


print('-5-'*30)
# Действительный пароль BEEGEEK банка имеет вид a:b:c,
# где a, b и c – натуральные числа. Поскольку основатель 
# BEEGEEK фанатеет от математики, то он решил:

# число a – должно быть палиндромом;
# число b – должно быть простым;
# число c – должно быть четным.

# def is_valid_password(password):

#     psw1 = psw.split(':')

#     if len(psw1) != 3:
#         return False 

#     a = psw1[0]
#     b = psw1[1]
#     c = psw1[2]

#     flag1 = False
#     flag2 = False
#     flag3 = False

#     if a == a[::-1]:
#         flag1 = True

#     for i in range(2,int(b)):
#         if int(b) % i == 0:
#             return False
#     else:
#         flag2 = True 
    
#     if int(c) % 2 == 0:
#         flag3 = True

#     return flag1 and flag2 and flag3
# # считываем данные
# psw = '1221:101:22'
# # вызываем функцию
# print(is_valid_password(psw))
    
print('-6-'*30)
# Напишите функцию is_correct_bracket(text), которая принимает в 
# качестве аргумента непустую строку text, состоящую из символов 
# ( и ) и возвращает значение True если поступившая на вход строка 
# является правильной скобочной последовательностью и False в противном случае.  


# def is_correct_bracket(text):
#     while '()' in text:
#         text = text.replase('()',' ')
#     if text == ' ':
#         return True
#     else:
#         return False
# # считываем данные
# txt = input()

# # вызываем функцию
# print(is_correct_bracket(txt))


print('-7-'*30)
# Напишите функцию convert_to_python_case(text), которая принимает в качестве
# аргумента строку в «верблюжьем регистре» и преобразует его в «змеиный регистр».

def convert_to_python_case(text):
    for i in text:
        if  i.isupper():
            text = text.replace(i , '_' + i.lower())
    text = text[1:]
    return text

# # считываем данные
txt = 'ThisIsCamelCased'

# вызываем функцию
print(convert_to_python_case(txt))






 


