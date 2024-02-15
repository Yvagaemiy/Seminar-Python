# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите 
# программу, которая подсчитает количество 
# элементов массива, больших предыдущего (элемента 
# с предыдущим номером) 
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения 
# списка или список задан изначально.
array = [0, -1, 5, 2, 3]
count = 0
for i in range(len(array)-1):
      
        if array[i] < array[i+1]:
            count = count + 1
           
print(count)   

nuw_array = [1 for i in range(len(array)-1)  if array[i] < array[i+1]]
print(sum(nuw_array))

nuw_array = [1 if array[i] < array[i+1] else 0 for i in range(len(array)-1)  ]
print(sum(nuw_array))