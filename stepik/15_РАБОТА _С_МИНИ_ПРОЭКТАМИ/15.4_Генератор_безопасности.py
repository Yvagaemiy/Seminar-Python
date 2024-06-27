
from random import *


digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation= '!#$%&*+-=?@^_.'

# def nambers():
#     num = input('Введите количество паролей: ')
#     while num.isdigit() == False:
#         print('Нужно ввести число:')
#         num = input('Введите количество паролей: ')
#     return int(num)


def long():
    l = input('Введите длину пароля: ')
    while l.isdigit() == False:
        print('необходимо длина пароля')
        l = input ('Введите длину пароля: ')  
    return int(l)

def digits_num():
    num = input('Если в пароле нужный цыфры 0123456789 напищи да или нет: ')
    while num.lower() not in ['да', 'нет']:
        print('напеши да или нет')
        num = input('Если в пароле нужный цыфры 0123456789 напищи да или нет: ')
    return num



def lowercase():
    low = input('Если в пароле нужный  буквы маленькие напищи да или нет: ')
    while low.lower() not in ['да', 'нет']:
        print('напеши да или нет')
        low = input('Если в пароле нужный буквы маленькие напищи да или нет: ')
    return low


def uppercase():
    upp = input('Если в пароле нужный заглавные  буквы  напищи да или нет: ')
    while upp.lower() not in ['да', 'нет']:
        print('напеши да или нет')
        upp = input('Если в пароле нужный заглавные буквы напищи да или нет: ')
    return upp

def punct():
    pun = input('Если в пароле нужный знаки напищи да или нет: ')
    while pun.lower() not in ['да', 'нет']:
        print('напеши да или нет')
        pun = input('Если в пароле нужный знаки напищи да или нет:')
    return pun



def ambiguous():
    amb = input('Будут ли в пароле неоднозначные символы "il1Lo0O"? Напиши "да" или "нет": ')
    while amb.lower() not in ['да', 'нет']:
        print('напеши да или нет')
        amb= input('Будут ли в пароле неоднозначные символы "il1Lo0O"? Напиши "да" или "нет": ')
    return amb

def gen_chars():
    chars = ''
    if num == 'да':
        chars +=digits
    if low == 'да':
        chars +=lowercase_letters
    if upp == 'да':
        chars += uppercase_letters
    if pun == 'да':
        chars += punctuation

        for i in range(len(chars)):
            if chars[i] in "il1Lo0O":
                del i
        return chars
    
# def password():
# #    for i in range(n):
#     password = []
#     for _ in range(l): 
#             password.append(choice(chars))
#     print(''.join(password))
def generate_password(length, chars):
    password = ''
    for j in range(length):
        password += random.choice(chars)
    return password


print(pasword)
pas = generate_password(l, chars)
print(pas)
#n =  nambers()
l = long()
num = digits_num()
low = lowercase()
upp = uppercase()
pun = punct()
chars = gen_chars()    
#password()