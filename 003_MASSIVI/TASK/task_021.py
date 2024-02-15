# Задача №21. 
# Напишите программу для печати всех уникальных 
# значений в словаре. 
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII 
# ":" S007 "}] 
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. 
# Пользователь его не вводит
s = 'python'
print(*s)

list_dicts = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "},{" v ":" S999 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
nuw_list = set()
for curr_dict in list_dicts:
    nuw_list.update(curr_dict.values())
print(nuw_list)     
   # nuw_list.add(*curr_dict.values())
#print(nuw_list)    
 #   print(*curr_dict.values(),end=' ') # * распечатывает только значение
    
    
 #   for val in curr_dict.values(): # Метод values() в Python возвращает объект представления,
                                   #который выводит список всех значений в словаре. Он не принимает никаких аргументов.
                                                   
 #       nuw_list.add(val.strip()) # add добовляет все уникальные множества в единичном экземпляре
        #trip убирает лишние элементы со всех сторон
 #       nuw_list.update(val.strip()) # update добовляет все уникальные множества в любом количестве
        
#print(nuw_list)