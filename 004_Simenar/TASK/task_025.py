# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

inp_1 = ' a a a b c a a d c d d '
inp_2 = inp_1.split()

output = ''
coint_dict = {}

for letter in inp_2:
    output = output + letter
    
    if letter in coint_dict:
        coint_dict[letter] = coint_dict[letter] + 1
        output = output + f'_{coint_dict[letter]}'
    else:
          coint_dict[letter] = 0 
          output = output + ' '
print(output)

print('__вариант 2 с get_____________________________________________')
 
  
input_data = ' a a a b c a a d c d d '.split() 
res = {}
for letter in input_data:
     if letter in res:
        print(f'{letter}_{res[letter]}', end='')
     else:
         print(letter, end='')
     res[letter] = res.get(letter, 0) + 1  
     
print()     
print('__вариант 3 с get_____________________________________________')


input_data = ' a a a b c a a d c d d ' .split()
res = {}
for letter in input_data:
    
    print(f'{letter}_{res.get(letter, " ")}', end='')
    res[letter] = res.get(letter, 0) + 1    
                  
     