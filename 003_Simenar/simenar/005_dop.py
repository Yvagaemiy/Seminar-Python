my_dist = {'Иванов' : 1 , 'Петров' : 2 , 'Сидоров' : 3, 'Куликов' : 4} # иванов это ключи , а 1 это значение
print(f'{my_dist=}')

for key in my_dist:  # десь мы получаем ключи проходя по славорю my_distс
    print(key,end='\t ')
print('\n')    

for key in my_dist.keys():  # сдесь мы получаем ключи проходя по славорю my_distс
    print(key,end='\t ')
print('\n')

for val in my_dist.values():  # сдесь мы получаем значения (индексы) проходя по славорю my_distс
    print(val,end='\t ')
print('\n')
 
for it in my_dist.items():  # сдесь мы получаем значения (индексы) и получаем ключи проходя по славорю my_distс (картеж)
    print(it,end='\t ')
print('\n')




print(f'{my_dist["Сидоров"]=}')

print(f'{my_dist.keys()=}') # обект ключей может один раз протись по списку без индексов
print(f'{my_dist.values()=}') #список
print(f'{my_dist.items()=}')  # список с картежами



print(f'{list(my_dist.keys())[3]=}')    # получаем список и можно работать со списком и в них можно оброщатся к индексам
print(f'{list(my_dist.keys())=}')    # получаем список и можно работать со списком и в них можно оброщатся к индексам
print(f'{list(my_dist.values())=}')     # получаем список и можно работать со списком
print(f'{list(my_dist.items())=}')      # получаем список и можно работать со списком