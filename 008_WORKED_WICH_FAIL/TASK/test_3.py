


#функция  создает контакт для записи
def creet_contact():
    name = input('Введите имя: ').title()
    phon_naber = int(input('Введите номер телефона: '))     
    return f'Имя: {name} Телефон:+7 {phon_naber} \n\n'            
#функция  записывает контакт 
def wrait_contact2():
    contact = creet_contact()
    with open('test_3.vsc','a', encoding='utf - 8') as fail:
        fail.write(contact)
    print("\n Контакт записан!\n")
#функция читает контакт для  print_contact()   
def read_contact():
    with open('test_3.vsc','r', encoding='utf - 8') as fail:
        read_of_contact =  fail.read().rstrip().split('\n\n')
    return read_of_contact 

#Функция  выводит список  контактов
def print_contact2():
    print_of_contact = read_contact()
    for nn , contact in enumerate(print_of_contact, 1):
        print(f"{nn}. {contact}\n")

#Функция  копирует контакт и показывает весь список контактов
def copy_contact2():
    print_of_contact = read_contact()
    for nn , contact in enumerate(print_of_contact, 1):
        print(f"{nn}. {contact}\n")
    
    contact_list = read_contact()
    number_contact = int(input("Введите номер контакта для копирования: "))   
    with open('text_3.vsc','a', encoding='utf - 8') as fail:
        fail.write(contact_list[number_contact - 1])
    print("\n Контакт копирован!\n\n")
 

              

               
def search_for_contact2():
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

def find_number(contact_list):
    search_field, search_value = search_for_contact2()
    search_value_dict = { '1': 'Имя', '2': 'Номер телефона'}
    found_contacts = []
    for i in contact_list:
        if i[search_value_dict[search_field]] == search_value:
            found_contacts.append(i)
    if len(found_contacts) == 0:
        print('Контакт не найден!')
    else:
        copy_contact2()(found_contacts)
    print() 
              
def get_new_number():
    first_name = input('Введите ИМЯ: ').title()
    phone_number = input('Введите НОМЕР ТЕЛЕФОНА: ')
    return f'Имя: {first_name} Телефон:+7 {phone_number} \n\n' 


def add_phone_number2():
    print_of_contact = read_contact()
    for nn , contact in enumerate(print_of_contact, 1):
        print(f"{nn}. {contact}\n")
        
    info = ' '.join(get_new_number())
    with open('text_3.vsc', 'a', encoding='utf-8') as file:
        file.write(f'{info}\n\n')
         
def delete_contact2():
    pass


def user_face2():
    print('Добро пожаловать в телефонный справочник!')
    with open('test_3.csv','a'):
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
                wrait_contact2()
            case '2':
                print_contact2()
            case '3':
                copy_contact2()
            case '4':
                search_for_contact2()
            case '5':
                add_phone_number2()
            case '6':
               delete_contact2()





user_face2()
#creet_contact()
#print_contact2()
copy_contact2()