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

def data_surname():
    return input('Введите Фамилию:')

def data_name():
   return input('Введите Имя:')

def data_phon():
    return input('Введите номер телефона:')

def data_address():
    return input('Введите Адрес:')


def create_contact():# функция создоет контакт   
    surname = data_surname()
    name    = data_name()
    phon    = data_phon()
    address = data_address()
    
    return f'{surname} {name} {phon}\n {address}\n\n'

def wrait_contakt(): #  функция записывает контакт
    contact = create_contact()
    with open('phonebooks.txt','a', encoding= 'utf - 8') as file:
        file.write(contact)
    print('\nКонтакт записан!\n')


def print_contact():# распечатать_контакт
   with open('phonebooks.txt','r',encoding='utf-8')as fail:
       print('__________________')
       #print(fail.read())
       print('__________________')

def search_contact():# поиск_контакта аргумет облась/поле/пространство //='' - 'значение по умолчанию что бы функция работала
    search = input('Введите данные поиска: ')
    with open('phonebooks.txt','r',encoding='utf-8')as fail:
        contat_str = fail.read()
#    print([contat_str])  # [data_str] - в [] выводит все в строку
    contat_list = contat_str.rstrip().split('\n\n') #  split     По умолчанию метод разделяет строку по пробелам.
                                                    # rstrip() - убирает пустое место с права так как r
#    print(contat_list)
       
    for contact in contat_list:
       
        if search in contact:
            print(contact)
        #     print()
           
       


def intrface():# пользовательское меню
    with open('phonebooks.txt','a'):# with - это с/вместе с
        pass
    user_input = None
    while user_input != '4':
        print(
            "Возможные варианты действия :\n"
              "1. Добавить контакт\n"
              "2. Вывод списка контактов\n"
              "3. Поиск контактов\n"
              "4. Выход из программы"
              )
        user_input = input('Введите вариант: ')
        while user_input not in ('1','2','3','4'):
            print('Некорректный ввод!')
            user_input = input('Введите коректный вариант: ')

        print()    

        match user_input:   # функция кейсов
            case '1': # если ввели '1' то проваливаемся в create_contact()
                wrait_contakt()
            case '2':
                print_contact()
            case '3':
                search_contact()
        


if __name__ == '__main__':
    intrface()