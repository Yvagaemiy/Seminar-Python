import os


def names():
    name = input('Введите имя: ')
    return name

def namber_phon():
    phon = int(input('Введите номер телефона: '))
    return phon

#функция  создает контакт для записи
def creet_contact():
    name = names().title()
    phon_naber = namber_phon()
    return f'{name} - {phon_naber}\n\n'
# Функция 1 записывает контакт
def wrait_contact():
    contact = creet_contact()
    with open('phon_books.txt','a', encoding='utf - 8') as fail:
        fail.write(contact)
    print("\n Контакт записан!\n")
#функция читает контакт для  print_contact()   
def read_contact():
    with open('phon_books.txt','r', encoding='utf - 8') as fail:
        read_of_contact =  fail.read().rstrip().split('\n\n')
    return read_of_contact 

#Функция 2 выводит контакт
def print_contact():
    print_of_contact = read_contact()
    for nn , contact in enumerate(print_of_contact, 1):
        print(f"{nn}. {contact}\n")
#Функция 3 копирует контакт и показывает весь список контактов
def copy_contact():
    print_of_contact = read_contact()
    for nn , contact in enumerate(print_of_contact, 1):
        print(f"{nn}. {contact}\n")

    contact_list = read_contact()
    nume_contact = int(input("Введите номер контакта для копирования: "))   
    with open('phon_books.txt','a', encoding='utf - 8') as fail:
        fail.write(contact_list[nume_contact - 1])
    print("\n Контакт копирован!\n")

def search_for_contact(field_name):  
    print(
            "Возможные варианты поиска :\n"
              "1. по Имени\n"
              "2. по номеру телефона\n"
              )
    search_indeks_input = int(input('Введите вариант поиска: '))-1
    search_user = input('Введите данные поиска: ')
    with open('phon_books.txt','r',encoding='utf-8')as fail:
        contat_str = fail.read()
#    print([contat_str])  #  - в [] выводит все в строку
    contats_list = contat_str.rstrip().split('\n\n') #  split     По умолчанию метод разделяет строку по пробелам.
                                                    # rstrip() - убирает пустое место с права так как стоит r(право)
#    print(contat_list)  
    for i in contats_list:
        contact_list = i.replace('\n', ' ').split(' ')
        if search_user in contact_list[search_indeks_input]:
            print(f'\n{i}\n')



def  cheng_contact():
    pass

# Функция 6 удаления контакта из телефонной книги
# def delete_contact():
#     print_of_contact = read_contact()
#     for nn , contact in enumerate(print_of_contact, 1):
#         print(f"{nn}. {contact}\n")

#     delete_of_contact = read_contact()
#     delete_name = input('Введите контакт для удаления: ').lower()

#     for i in  delete_of_contact:
        
#         if i == delete_name :
            #  print("Вы хотите удалить контакт %s (yes/no)?: " %  delete_of_contact )
            #  name_del = input('> ')
            #  if name_del == 'yes':
                # delete_of_contact.remove(i)
                # print("Вы удалили контакт %s " %  delete_name )
# def delit_contact():     
#     print_of_contact = read_contact()
#     for nn , contact in enumerate(print_of_contact, 1):
#         print(f"{nn}. {contact}\n")

#     contact_list = read_contact()
#     nume_contact = int(input("Введите номер контакта который надо удалить: "))   
#     with open('phon_books.txt','w', encoding='utf - 8') as fail:
#          fail.write(contact_list[nume_contact - 1])
#     print("\n Контакт удален!\n") 
#def del_contact():
    # print_of_contact = read_contact()
    # for nn , contact in enumerate(print_of_contact, 1):
    #     print(f"{nn}. {contact}\n")

    # contact_list = read_contact()
    # nume_contact = int(input("Введите номер контакта для удаления: "))   
    # with open('phon_books.txt','w', encoding='utf - 8') as fail:
    #     fail.__del__(contact_list[nume_contact - 1])    
    # print("\n Контакт удален!\n")
    
     
def delete_contact(file_name):
    print_of_contact = read_contact()
    for nn , contact in enumerate(print_of_contact, 1):
        print(f"{nn}. {contact}\n")

    contact_list = read_contact(file_name)
    number_to_change = search_for_contact(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)
    # del_user = input('Введите данные поиска: ')
    # with open('phon_books.txt','w',encoding='utf-8')as fail:
    #     contat_str = fail.read()
    # contats_list = contat_str.rstrip().split('\n\n')
 
    # for i in contats_list:
    #     contact_list = i.replace('\n', ' ').split(' ')
    #     if del_user in contact_list:
    #         contact_list=contact_list.remove()
    #         print(f'\n{ contact_list}\n')
   


#Функция интерфейс
def user_face():
    print('Добро пожаловать в телефонный справочник!')
    with open('phon_books.txt','a'):
        pass
    user_input = None
    while user_input !=7:
        print(
            "Выберите пункт меню: \n"
            "1. Создать контакт\n"
            "2. Просмотр контакта\n"
            "3. Копировать контакт\n"
            "4. Поиск контакта\n"
            "5. Изменение контакта\n"
            "6. Удаление контакта\n"
            "7. Выход\n"
              )
        user_input = input("Выбирите вариант: ")

        while user_input not in ('1','2','3','4','5','6','7'):
            print("не коректный ввод!")
            user_input = input("Выбирите коректный вариант: ")
        
        print()

        match user_input:
            case '1':
                wrait_contact()
            case '2':
                print_contact()
            case '3':
                copy_contact()
            case '4':
                search_for_contact()
            case '5':
                cheng_contact()
            case '6':
               delete_contact()

             


user_face()
read_contact()
delete_contact()
#del_contact()
#print_contact()