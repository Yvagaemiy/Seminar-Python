def new_fail():
    with open("shop_fail.txt",'a'):
        pass

def spisok_shop():
    nume = input('Введите наименование продукта: ').title()
    count = int(input('Введите количество: '))
    return f"{nume} - {count} \n\n"


def wraet_spisik():
    list_produkt = spisok_shop()
    with open("shop_fail.txt",'a', encoding='utf') as fail:
        fail.write(list_produkt)
        print("запись сделана!")

def raed_spisik():
    with open("shop_fail.txt",'r', encoding='utf') as fail:
        read_spisok_print = fail.read().rstrip().split('\n\n')
    return read_spisok_print

def print_spisok():
    list_print = raed_spisik()
    for nn , product in enumerate(list_print, 1):
        print(f"{nn} {product}")

def analis_spisok():
    sile_list = {}
    with open('shop_fail.txt','r', encoding='utf - 8') as fail:
        read_fail = fail.read().split('\n\n')
        print(read_fail)
        for i in read_fail:
            i = i.strip('-')
            #print(i)
            if not i: #проверка на пустые строки
               continue
            product,qvantyti = i.split('-')
            qvantyti = int(qvantyti)

            if product  in sile_list:
                    sile_list[product] += qvantyti
           
            else:
                    sile_list[product] = qvantyti

        for i, j in sile_list.items():
             print(i , j)
            
      

def user_intefac():
    print("список продукции магазина:")
    user_input = None
    while user_input != 4:
        print(
            "1 - сделать запись:\n "
            "2 - вывести весь список:\n "
            "3 - сумма каждого наименования товара:\n "
            "4 - выход"
             )
        user_input = input("Выберети пункт: ")
        while user_input not in ('1','2','3','4'):
            print('введен не коректный ввод!')
            user_input = input("Выберети пункт: ")

        match  user_input:
            case '1':
              wraet_spisik()
            case '2':
                print_spisok()
            case '3':
                analis_spisok()
            case '4':
                print("Досвидание!")
user_intefac()