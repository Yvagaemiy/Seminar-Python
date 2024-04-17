print('-1-'*30)

# data = input()
# dollar = input()
# yan = input()

# print(f'На {data}: 1$ = {dollar}₽, 1¥ = {yan}₽')

print('-1-'*30)

data = int(input())

massa = float(input())

nuw_mass = 100 - 0.2 * data



if massa <= nuw_mass:
    print('Все идет по плану')

else:
    print('Что-то пошло не так')


print(f'#{data} ДЕНЬ: ТЕКУЩИЙ ВЕС = {massa} кг, ЦЕЛЬ по ВЕСУ = {nuw_mass} кг')




