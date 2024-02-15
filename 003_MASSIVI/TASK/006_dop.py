q, a, *d = (1, 2, 3, 4, 5)  # * создает список внутри картежа
print(q)
print(a)
print(d)

my_list = [(1, 2, 3), (11, 22, 33), (111, 222, 333)]
for key in my_list:
    print(key)


for q,a,*z in my_list: # под * показывает список
    print(q,a,z)
    
    
my_dist = {'Иванов' : 1 , 'Петров' : 2 , 'Сидоров' : 3, 'Куликов' : 4}    
for key, value in my_dist.items():
    print(key, value, sep=' : ' ,end='\t')
print('\n')

my_dist['Никифоров'] = my_dist.pop('Иванов') # рор заменил иванова на некифорова и присвоил ему 1 элемент
print(my_dist)

my_dist['Петров'] = my_dist['Алексеей']
print(my_dist)

my_dist['Петров'] = my_dist['Алексеей']
del my_dist['Петров']
print(my_dist)

