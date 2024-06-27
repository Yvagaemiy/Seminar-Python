contacts = [
    {
        "name": "John",
        "phone": "123456"
    },
    {
        "name": "Jane",
        "phone": "564321"
    },
    {
        "name": "Bob",
        "phone": "+1234"
    },
]
 
FORMAT_STR = '{:<15} {:>12}'
 
 
def list(contacts):
    print(FORMAT_STR.format('Name', 'Phone'))
    for contact in contacts:
        print(FORMAT_STR.format(
            contact['name'],
            contact['phone']
        ))
 
 
 
def find(contacts):
    print("Введите имя контакта:")
    name = input("> ")
 
    for contact in contacts:
        if contact['name'] == name:
            print(FORMAT_STR.format(
                contact['name'],
                contact['phone']
            ))
            break
    else: 
        print("Контакт не найден")
 
def delete(contacts):
    print("Введите контакт: ")
    name = input('> ')
    for contact in contacts:
        if contact['name'] == name:
            print("Вы хотите удалить контакт %s (yes/no)?: " % name )
            name_del = input('> ')
            if name_del == 'yes':
               contacts.remove(contact)
               print("Вы удалили контакт %s " % name)
 
 
 
def add(contacts):
    print("Введите имя контакта:")
    name = input("> ")
    print("Введите телефон контакта:")
    phone = input("> ")
    new_contact = {
        'name': name,
        'phone': phone
    }
    contacts.append(new_contact)
    
    print('Контакт сохранён')
 
print("Добро пожаловать в телефонную книгу.")
print("""Введите команду:
* 1 - чтобы посмотреть список контактов.
* 2 - найти контакт по имени
* 3  - добавить контакт
* 4  - удаление контакта
* 5 - изменение контакта 
* 6 - выход""")
 
while True:
    print("\nВведите команду: ")
    command = input('> ')
    if command == '1':
        list(contacts)
    elif command == '2':
        find(contacts)
    elif command == '3':
        add(contacts)
    elif command == '4':
        delete(contacts)
    elif command == '5': 
        edit(contacts)       
    elif command == '6':
        break
    else:
        print("Неизвестная команда")