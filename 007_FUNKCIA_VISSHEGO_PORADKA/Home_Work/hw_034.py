# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
# разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
# стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
# гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
# слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
# от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
# напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
# в порядке
# Ввод: Вывод:
# пара-ра-рам рам-пам-папам па-ра-па-дам Парам пам-пам
print('__ВАРИАНТ С АВТОТЕСТОВ_______________________________________')

stroka_1 = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

glasnii = ['а', 'е', 'ё', 'и', 'й', 'о', 'у', 'ы', 'э', 'ю', 'я']
spisok = stroka_1.split()
if len(spisok) < 2:
 print('Количество фраз должно быть больше одной!')
else:
 countVowels = []

for i in spisok:
    countVowels.append(len([x for x in i if x.lower() in glasnii]))

if  len(countVowels) == countVowels.count(countVowels[0]):
    print('Парам пам-пам')
else:
    print('Пам парам')




print('___мой вариант______________________________________')


def vini_pyx(spisok):
    spisok = spisok.split()# из vini_pyx(spisok) взяли spisok и присвоили функцию
    list_1 = []
    for word in spisok:
        sum_word = 0
        for i in word:
            if i in 'йуеыаоэюяи':
                sum_word+=1
        list_1.append(sum_word)
    return len( list_1) ==  list_1.count( list_1[0])


stroka_1 = ' пара-ра-рам рам-пам-папам па-ра-па-дам '
if  vini_pyx(stroka_1):
    print('Парам пам-пам')
else:
    print('Пам парам')


print('____еще вариант_1_____'*2)

def sum_vowletes(fraza):
    vow_let = 'йуеыаоэюяи'
    count_0=0
    for i in fraza:
        if i in vow_let:
           count_0+=1
    return count_0     
   
def chekund_count(fraza_list):
    vowel_0 = sum_vowletes(fraza_list[0])
    for fraza in fraza_list[:1]:
        if sum_vowletes(fraza) != vowel_0 :
            return 'Пам парам'
        
    return 'Парам пам-пам'
   

stroka_1 =  ' пара-ра-рам рам-пам-папам па-ра-па-дам '.split()

print(chekund_count(stroka_1))

print('____еще вариант_2_____'*2)

def rifma(poem):
    phraza_list = poem.lower().split()
    sum_vowelse = lambda phraza: sum(1  for i in phraza if i in 'йуеыаоэюяи')
    tmp = sum_vowelse(phraza_list[0])
    if all([sum_vowelse(phraza) == tmp for phraza in phraza_list[1:]]):
        return 'Парам пам-пам'
    return 'Пам парам'
print(rifma('пара-ра-рам рам-пам-папам па-ра-па-дам '))
      

      