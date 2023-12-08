# Задача №27.
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов. Определите, сколько различных слов 
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13


text_data = "She sells sea shells on the sea shore The shellsthat she sells are sea shells I'm sure.So if she sells seashells on the sea shore I'm sure that the shells are seashore shells"

print(text_data.split()) # split() разделяет строку, пробелы и переделывает строку в список
print(type(text_data.split()))
text_1 = text_data.lower().split() # lower() переводит список в нижний регистор
print(len(set(text_1)))



print('_________________________________________')


str_1 = 'a a a b c a b c'
list_1 = str_1.split()
print(type(list_1))

coint = ''
res = {}
for i in list_1:
    coint = coint + i
    if i in res:
        res[i] = res[i] + 1
        coint = coint + f'_{res[i]}'
    else:
        res[i] = 0
        coint = coint + ''
print(coint)   