"""Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
4. Использование функций. Ваша программа не должна быть линейной """


def user_interfac():
    user_choice = None
    while user_choice !=8:
        print('Что вы хотите сделать?: ')
        user_choice = input(
            '1 - Импортировать данные\n'
            '2 - Добавить контакт\n'
            '3 - Найти контакт\n'
            '4 - Изменить контакт\n'
            '5 - Удалить контакт\n'
            '6 - Просмотреть все контакты\n'
            '7 - Копировать контакт\n'
            '8 - Выйти из приложения\n'
            )
        if user_choice == '1':
            file_to_add = input('Введите название импортируемого файла: ')
            import_data(file_to_add)
        elif user_choice == '2':
            add_phone_number()
        elif user_choice == '3':
            contact_list = read_file_to_dict()
            find_number(contact_list)
        elif user_choice == '4':
            change_phone_number()
        elif user_choice == '5':
            delete_contact()
        elif user_choice == '6':
            print_contact()
        elif user_choice == '7':
            copy_contact()
        elif user_choice == '8':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue


def import_data():
    try:
        with open('Phon_book1!.txt', 'r', encoding='utf-8') as new_contacts, open('Phon_book1!.txt', 'a', encoding='utf-8') as file:
            contacts_to_add = new_contacts.readlines()
            file.writelines(contacts_to_add)
    except FileNotFoundError:
        print(f'{'Phon_book1!.txt'} не найден')

#функция читает контакт для  print_contact()   
def read_contact():
    with open('Phon_book1!.txt','r', encoding='utf - 8') as fail:
        read_of_contact =  fail.read().rstrip().split('\n\n')
    return read_of_contact 

#Функция 2 выводит контакт
def print_contact():
    print_of_contact = read_contact()
    for nn , contact in enumerate(print_of_contact, 1):
        print(f"{nn}. {contact}\n")
#Функция 3 копирует контакт и показывает весь список контактов
def copy_contact(f):
    print_of_contact = read_contact()
    for nn , contact in enumerate(print_of_contact, 1):
        print(f"{nn}. {contact}\n")

    contact_list = read_contact()
    nume_contact = int(input("Введите номер контакта для копирования: "))   
    with open('Phon_book1!.txt','a', encoding='utf - 8') as fail:
        fail.write(contact_list[nume_contact - 1])
    print("\n Контакт копирован!\n")

# def show_phonebook(file_name):
#     list_of_contacts = sorted(read_file_to_dict(file_name), key=lambda x: x['Фамилия'])
#     print_contacts(list_of_contacts)
#     print()
#     return list_of_contacts

def read_file_to_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        lines = file.readlines()
    headers = ['Фамилия', 'Имя', 'Ном тел']
    contact_list = []
    for line in lines:
        line = line.strip().split()
        contact_list.append(dict(zip(headers, line)))
    return contact_list


def read_file_to_list(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        contact_list = []
        for line in file.readlines():
            contact_list.append(line.split())
    return contact_list

# Функция поиска данных от пользователя9 для удаления,поиска итд)
def search_parameters():
    print('По какому полю выполнить поиск?')
    search_field = input(
                         '1 - по фамилии\n'
                         '2 - по имени\n'
                         '3 - по номеру телефона\n'
                         )
    search_value = None
    match search_field:
        case '1':
            search_value = input('Введите ФАМИЛИЮ для поиска: ')
        case '2':
            search_value = input('Введите ИМЯ для поиска: ')
        case '3':
            search_value = input('Введите НОМЕР ТЕЛЕФОНА для поиска: ')
    return search_field, search_value
            
    # print()
    # search_value = None
    # if search_field == '1':
    #     search_value = input('Введите фамилию для поиска: ')
    #     print()
    # elif search_field == '2':
    #     search_value = input('Введите имя для поиска: ')
    #     print()
    # elif search_field == '3':
    #     search_value = input('Введите номер для поиска: ')
    #     print()
    # return search_field, search_value


def find_number(contact_list):
    search_field, search_value = search_parameters()
    search_value_dict = {'1': 'Фамилия', '2': 'Имя', '3': 'Номер телефона'}
    found_contacts = []
    for contact in contact_list:
        if contact[search_value_dict[search_field]] == search_value:
            found_contacts.append(contact)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        print_contacts(found_contacts)
    print()


def get_new_number():
    last_name = input('Введите фамилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    return last_name, first_name, phone_number


def add_phone_number(file_name):
    info = ' '.join(get_new_number())
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'{info}\n')





def search_to_modify(contact_list: list):
    search_field, search_value = search_parameters()
    search_result = []
    for contact in contact_list:
        if contact[int(search_field) - 1] == search_value:
            search_result.append(contact)
    if len(search_result) == 1:
        return search_result[0]
    elif len(search_result) > 1:
        print('Найдено несколько контактов')
        for i in range(len(search_result)):
            print(f'{i + 1} - {search_result[i]}')
        num_count = int(input('Выберите номер контакта, который нужно изменить/удалить: '))
        return search_result[num_count - 1]
    else:
        print('Контакт не найден')
    print()


def change_phone_number(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    print('Какое поле вы хотите изменить?')
    field = input('1 - Фамилия\n2 - Имя\n3 - Номер телефона\n')
    if field == '1':
        number_to_change[0] = input('Введите фамилию: ')
    elif field == '2':
        number_to_change[1] = input('Введите имя: ')
    elif field == '3':
        number_to_change[2] = input('Введите номер телефона: ')
    contact_list.append(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def delete_contact(file_name):
    contact_list = read_file_to_list(file_name)
    number_to_change = search_to_modify(contact_list)
    contact_list.remove(number_to_change)
    with open(file_name, 'w', encoding='utf-8') as file:
        for contact in contact_list:
            line = ' '.join(contact) + '\n'
            file.write(line)


def print_contacts(contact_list: list):
    for contact in contact_list:
        for key, value in contact.items():
            print(f'{key}: {value:12}', end='')
        print()



    
user_interfac()  
