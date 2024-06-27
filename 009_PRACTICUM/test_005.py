def totl_cart_cost(cart_items):

    #cart_items ={'аяблоко : 23', 'дыня : 45', 'картошка : 10'}
    new_cart_items = {}
    for i in cart_items:
        i = i.strip(':')
        produkt, totl = i.split(':')
        totl = int(totl)

        if produkt in new_cart_items:
            new_cart_items[produkt] += totl
        else:
            new_cart_items[produkt] = totl
    sum_j = 0
    for i,j in new_cart_items.items():
        print(i, j)
        
        sum_j +=j
    print(f'сумма всех продуктов = {sum_j}')
    

cart_items_1 ={'яблоко : 23', 'дыня : 45', 'картошка : 10', 'дыня : 32 ','картошка : 40', 'яблоко : 90'}   

totl_cart_cost(cart_items_1)

#вариант с виде через рекурсию

cart_items_2 =[{'наименование' : 'яблоко' , 'цена' : 23},
              {'наименование' :'дыня' ,'цена'  : 45},
              {'наименование':'картошка ','цена' : 10},
              {'наименование':'сливы ','цена' : 32 },
              {'наименование':'помидоры', 'цена' : 40},
              {'наименование':'хлеб' ,'цена' : 90}
              ] 

def totl_cart(cart_items_2):
#вспомогательная функция для рекурсии
    def add_prace(total, prace):
        if prace == 0:
            return total
        else:
            return add_prace(total +1  , prace -1)
 # проверка пустых списков       
    if not cart_items_2:
        return 0
    
#вычесляем стоимосьть первого товара из списка
    firs_itams_cost = add_prace(0, cart_items_2[0]['цена'])
    return firs_itams_cost + totl_cart(cart_items_2[1:] )

print(f'сумма всех продуктов = {totl_cart(cart_items_2)}')