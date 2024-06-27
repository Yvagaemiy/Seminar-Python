# Задача №55. Решение в группах
# Создать телефонный справочник с
# возможностью импорта и экспорта данных в
# формате .txt. Фамилия, имя, отчество, номер
# телефона - данные, которые должны находиться
# в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в
# текстовом файле
# 3. Пользователь может ввести одну из
# характеристик для поиска определенной
# записи(Например имя или фамилию
# человека)
# 4. Использование функций. Ваша программа
# не должна быть линейной

#1. Зосдание файла +++
#----------------------
#2. Добавление новой записи ++++
#   * input пользователя +++
#   * открыть фаил на дозапись +++
#   * запись в фаил +++++
#----------------------
# 3. Вывод на экран
#   * открыть фаил на чьтенье
#   * считывание данных
#   * вывод на экран
#----------------------
# 4. Поиск контакта
#   * выбрать вариант поиска
#   * input пользователя
#   * открыть фаил на чьтенье
#   * считывание данных
#   * осуществить поиск
#   * вывод на экран
# 5. Пользовательский интерфес  ++++
#  * Вы хотите ввести данные
#  * Вы хотите получить данные
#  * выход


def data_surname():
    return input('Введите Фамилию: ').title()

def data_name():
   return input('Введите Имя: ').title()

def data_phon():
    return input('Введите номер телефона: ')

def data_address():
    return input('Введите Адрес: ').title()

#ФУНКЦИЯ 1   ++++++++
def create_contact():# функция создоет контакт   
    surname = data_surname()
    name    = data_name()
    phon    = data_phon()
    address = data_address()
    return f'{surname} {name} {phon}\n {address}\n\n'# \n\n перенос на новую строку

def wrait_contakt(): #  функция записывает контакт
    contact = create_contact()
    with open('phonebooks.txt','a', encoding= 'utf - 8') as file:
        file.write(contact)
    print('\nКонтакт записан!\n')

def raed_files():
    with open('phonebooks.txt','a', encoding= 'utf - 8') as file:
         contaktr_list = file.read().rstrip().split('\n\n')
    return contaktr_list

#ФУНКЦИЯ 2 -----------
def print_contact():# распечатать_контакт аргумент из  return contaktr_list def raed_files():
    contaktr_list = raed_files()
    for nn, contakt in enumerate(contaktr_list, 1):
        print(f'{nn}. {contakt }\n')


    
#Функция 3 поиск контакта +++++++++++++
def search_contact(field = ''):# поиск_контакта аргумет облась/поле/пространство //='' - 'значение по умолчанию что бы функция работала
    print(
            "Возможные варианты поиска :\n"
              "1. По фамилии\n"
              "2. По Имени\n"
              "3. По номеру телефона\n"
              "4. По городу"
              )
    search_indeks_input = int(input('Введите вариант поиска: '))-1
    search = input('Введите данные поиска: ')
    with open('phonebooks.txt','r',encoding='utf-8')as fail:
        contat_str = fail.read()
    print([contat_str])  #  - в [] выводит все в строку
    contats_list = contat_str.rstrip().split('\n\n') #  split     По умолчанию метод разделяет строку по пробелам.
                                                     #rstrip() - убирает пустое место с права так как стоит r(право)
    #print(contat_list)  
    for contact_str in contats_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if search in contact_list[search_indeks_input]:
            print(f'\n{contact_str}\n')
            print()
           
#функция 4
def copy_files():# пытается скопировать контакт
    contak_list = raed_files()
    print_contact(contak_list)
    num_indeks_input = int(input('Введите номер контакта для копирования: '))
    with open('phonebooks.txt','a', encoding= 'utf - 8') as file:
        file.write( contak_list[num_indeks_input - 1]) # -1 для того чтобы избавится от 0 индекса
    print('\nКонтакт скопирован!\n')

#Функция 5   исправить контакт
def chenge_contact(field = ''):# поиск_контакта аргумет облась/поле/пространство //='' - 'значение по умолчанию что бы функция работала
    print(
            "Возможные варианты поиска :\n"
              "1. По фамилии\n"
              "2. По Имени\n"
              "3. По номеру телефона\n"
              "4. По городу"
              )
    chenge_indeks_input = int(input('Введите вариант поиска: '))-1
    chenge = input('Введите данные поиска: ')
    with open('phonebooks.txt','W',encoding='utf-8')as fail:
        contat_str = fail.read()
    print([contat_str])  #  - в [] выводит все в строку
    contats_list = contat_str.rstrip().split('\n\n') #  split     По умолчанию метод разделяет строку по пробелам.
                                                     #rstrip() - убирает пустое место с права так как стоит r(право)
    #print(contat_list)  
    for contact_str in contats_list:
        contact_list = contact_str.replace('\n', ' ').split(' ')
        if chenge in contact_list[chenge_indeks_input]:
            print(f'\n{contact_str}\n')       

#это первая функция
def intrface():# пользовательское меню
    with open('phonebooks.txt','a'):# with - это с/вместе с
        pass
    user_input = None
    while user_input != '7':# Так как у нас 3 кесса а 4 какбы выход
        print(
            "Возможные варианты действия :\n"
              "1. Добавить контакт\n"
              "2. Вывод списка контактов\n"
              "3. Поиск контактов\n"
              "4. Копировать контакт\n"
              "5. Иcправить контакт\n"
              "6. Удалить контакт\n"
              "7. Выход из программы"
              )
        user_input = input('Введите вариант: ')

        while user_input not in ('1','2','3','4','5','6','7'):
            print('Не корректный ввод!')
            user_input = input('Введите коректный вариант: ')

        print()    

        match user_input:   # функция кейсов
            case '1': # если ввели '1' то проваливаемся в create_contact()
                wrait_contakt()
            case '2':
                print_contact()
            case '3':
                search_contact()
            case '4': 
                copy_files()
            case '5':
                chenge_contact()
            case '6':
                pass
        


if __name__ == '__main__':
    intrface()

raed_files()