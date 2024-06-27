list_1 = "rd*gdj fhgffbgfg#g *mhjb*kyu rtt*hth#"

firs_list = list_1.replace('*', 'WWW')
print(firs_list)

list_2 =''
for i in firs_list:
    list_2+=i
second_list = list_2.replace('#','ZZZ')
print(second_list)

#вариант с видео 1

list_2 = '''rd*gdj fhgffbgfg#g
            *mhjb*kyu rtt*hth'''
# удаляем все символы кроме букв
clean_list_1 = ''.join(filter(str.isalpha, list_2.lower()))

# посчитаем частоту каждой буквы
from collections import Counter
freqoen = Counter(clean_list_1)

#сортируем буквы по частоте использования
sorted_freqoen = freqoen.most_common()

#самая частая и самая редкая буква
most_common_letter, most_common_count = sorted_freqoen[0]
least_common_letter , least_common_count = sorted_freqoen[-1]

most_common_letter, most_common_count,least_common_letter , least_common_count

for letter, count in sorted_freqoen :
    print(f"{letter}:{count} ",end='')

#вариант с видео 2

list_3 = '''rd*gdj fhgffbgfg#g
            *mhjb*kyu rtt*hth'''
# удаляем все символы кроме букв
clean_list_2 = ''.join(filter(str.isalpha, list_3.lower()))

#инициализация пустого слова для частоты букв
frequency ={} 

# посчитаем частоту каждой буквы
for i in clean_list_2:
    if i in frequency:
        frequency[i] +=1
    else:
        frequency[i] =1

#сортируем буквы по частоте использования
sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

#вывод частоты каждой буквы
for letter, count in sorted_frequency :
    print(f"{letter}:{count} ",end='')