n = 'Hello, my friend! How are you? =)'
s = n
for i in s:
    if i in '!@".,)=?':
        s = s.replace(i,' ')

x = [len(i) for i in s.split()] 
print(x)

new_text = ''
count=0
for j in n:
    num = ord(j)
 
    if j == ' ':
        count +=1
        new_text+=j
    elif 65<= num <=90:
        if num + x[count] > 90:
            new_text+= chr((num + x[count]) -26 ) 
        else:
            new_text+= chr(num + x[count]) 
    elif 97<= num <=122:
        if num + x[count] > 122:
            new_text+= chr((num + x[count]) - 26) 
        else:
            new_text+= chr(num + x[count]) 
    else:
        new_text+=j

print(new_text)
#Day, mice. "Year" is a mistake!
#Gdb, qmgi. "Ciev" ku b tpzahrl!
#Mjqqt, oa lxoktj! Krz duh brx? =)
print('--степик 9.6--' *3)
# степик 9.6
# n = 1

# st = 'bwfusvfupdbftbs'

# for i in st:
#      st_1 = ord(i)
    
#      if st_1 - n < 97:
#         st_1 = 122 - (96 - st_1 + n)

#         print(chr(st_1), end='')

#      else:
         
#          print(chr(st_1 - n), end='')

print('РУССКАЯ  функции цезерь' *2)

# рабочие функции шифровки дешефровки цезарь

# def fn_cezer_rus(text: str, shift: int):
#     alphobet_lower = 'абвгдежзийклмнопрстуфхчшщьъэюя'
#     alphobet_upper = alphobet_lower.upper()
#     ord_first_letter_lower = ord('а')
#     ord_first_letter_upper = ord('А')
#     new_text = ''

#     for i in text:
#         if i in alphobet_lower:
#             new_text += chr(((ord(i) - ord_first_letter_lower + shift ) % 32) + ord_first_letter_lower)
#         elif i in  alphobet_upper:
#             new_text += chr(((ord(i) -  ord_first_letter_upper + shift) % 32) + ord_first_letter_upper)
#         else:
#             new_text += i

#     return new_text
# user_text = input('введите текст на русском: ')
# user_number = int(input('введите сдвиг: '))
# res = fn_cezer_rus(user_text,user_number)
# print(res)

# def decoder_fn_cezer_rus(text: str, shift: int):
#     return fn_cezer_rus(text, -shift)

# decoder_res = (decoder_fn_cezer_rus('Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.', 7))
# print(decoder_res)

print('АНГЛ  функции  цезарь ' *2)
# def fn_cezer_in(text: str, shift: int):
#     alphobet_lower = 'abcdefghijklmnopqrstuvwxyz'
#     alphobet_upper = alphobet_lower.upper()
#     ord_first_letter_lower = ord('a')
#     ord_first_letter_upper = ord('A')
#     new_text_1 = ''

#     for i in text:
#         if i in alphobet_lower:
#             new_text_1 += chr(((ord(i) - ord_first_letter_lower + shift ) % 26) + ord_first_letter_lower)
#         elif i in  alphobet_upper:
#             new_text_1 += chr(((ord(i) -  ord_first_letter_upper + shift) % 26) + ord_first_letter_upper)
#         else:
#             new_text_1 += i

#     return new_text_1
# user_text_1 = input('введите текст на английском: ')
# user_number_1 = int(input('введите сдвиг: '))
# res_1 = fn_cezer_in(user_text_1,user_number_1)
# print(res_1)



# def decoder_fn_cezer_in(text: str, shift: int):
#     return fn_cezer_in(text, -shift)



# num = int(input('введите сдвиг: '))
# decoder_res_1 = (decoder_fn_cezer_in( "Hawnj pk swhg xabkna ukq nqj.", num ))
# print(decoder_res_1)




