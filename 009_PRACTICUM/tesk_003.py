def new_fail():
    with open("sum_word_of_spisok.txt",'a'):
        pass

def cret_spisok():
    word_list = input("запешите слово: ")
    return f'{ word_list} {''}'

def wraet_spisok():
    wraet_list = cret_spisok()
    with open("sum_word_of_spisok.txt",'a',encoding="utf -8")as fail:
        fail.write(wraet_list)
    print('слово записано!')
def raet_spisok():
    with open("sum_word_of_spisok.txt",'r',encoding="utf -8")as fail:
        raet_list = fail.read().split()
    return raet_list

def  print_spisok():
    print_list = raet_spisok()
    for i in print_list:
        i = i.split()
        print(i,end='')       
           
def sum_word_of_spisok():
    with open("sum_word_of_spisok.txt",'r',encoding="utf -8")as fail:
        spisok = fail.read().split()
        sum_spisok = 0
        for i in range(len(spisok)):
            i = int(i)
            sum_spisok+=1
        print(f'всего {sum_spisok} слов')


def user_interface():
    print('\nдобрый день!')
    user_input = None
    while user_input != 4:
        print(
              "\n1 - заполнить список\n"
              "2 - посмотреть список\n"
              "3 - посчитать слова в списке\n"
              "4 - выход\n"
              )
        user_input = input("Выберите пункт: ")
        while user_input  not in ('1','2','3','4'):
            print("не коректны ввод!")
            user_input = input("\nВыберите пункт: ")

        match user_input:
            case '1':
                wraet_spisok()
            case '2':
                print_spisok()
            case '3':
                sum_word_of_spisok()
            case '4':
                print("Досвидание!")


user_interface()
