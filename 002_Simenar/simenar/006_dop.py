а = "хахаха"
print(а)




text = 'weesgsae rgrtthrrth frge'
# print(*range(len(text)))  #len пото му что это строка и чтобы пройтись по всей строке используется len, * условия распоковки индекса (0, 24)
# print(list(range(len(text))))
# for i in range(len(text)) :
#     print(i, text[i], sep='-',end='-')
    
# print()

# for letter in text :   # в этом решении мы берем не индекс а букву. И проходить будем не по range  ,а по text
#     print(letter, end=' - ')
    
# print()
n = 1
while True:
    print('Безконечный цикл')
    n = n + 1
    if n % 5 == 0:
        break

print()
    
n = 1
while n % 5 != 0:
    print('Безконечный цикл')
    n = n + 1
   
print()
for i in range(len(text)) :
    if i % 3 == 0:
        continue # пропускаем каждую 3 букву
    if text[i] == 't':
        break # как только находим букву g код останавливается
    print(i, text[i], sep='-',end=' - ')
else: # else относится к циклу for
    print()
    print('мыпрошлись по всей строке')