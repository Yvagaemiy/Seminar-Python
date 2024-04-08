

print('-1-'*30)


for i in range(3):
    for j in range(3):
 #       if i == j:
 #           break
          print(i, j)

print()

for i in range(3):
    for j in range(3):
        if i == j:
            continue
        print(i, j)


for i in range(6):
    for j in range(6):
        print('*',end='')
    print()


for i in range(6):
    for j in range(i+1):
        print('*',end='')
    print()


for i in range(1, 4):
    for j in range(3, 6):
        print(i, j)
    print()

print('-2-'*30)

# n = 4

# for i in range(n):
#     for j in range(n):
#         print(n,sep='',end=' ')
#     print()

print('-3-'*30)

# n = 4

# for i in range(n):
#     for j in range(n):
#         print(i,end=' ')
#     print()


print('-4-'*30)

# n = int(input())
# for i in range(1,n+1):
#     for j in range(5):
#         print(i,end=' ')
#     print()



print('-5-'*30)


# n = 4

# for i in range(1,n+1):
#     for j in range(1,9+1):
#         print(i,'+',j,'=',i+j)
#     print()

print('-6-'*30)

# n = 5

# for i in range(1,n //2 + 2):
#     for j in range(i):
#         print('*', end='')
#     print()
    
# for i in range(n//2 + 1,0,-1):
#     for j in range(i -1):
#         print('*', end='')
#     print()


print('-7-'*30)

# n = 5

# for i in range(n+1):
#     for j in range(i):
#         print(i, end='')
#     print()


print('-8-'*30)


# 12x+13y=777

# total = 0

# for x in range(1, 65):
#     for y in range(1,60):
#         if x * 12 + y * 13 ==777:
#             total +=1
#             print('x =', x, 'y =', y)
# print('Общее количество натуральных решений =', total)


# #2022 по корнем = 45

# total = 0 

# for x in range(1,45):
#     for y in range(1,45):
#         for z in range(1, 45):
#             if x **2 + y ** 2 + z ** 2 == 2020:
#                 total+=1
#                 print('x =', x, 'y =', y,'z =',z)
# print('Общее количество натуральных решений =', total)

 
# 28n+30k+31m=365.

# total = 0 

# for n in range(1,13):
#     for k in range(1,12):
#         for m in range(1, 11):
#             if n * 28 + k * 30 + m * 31 == 365:
#                 total+=1
#                 print('n =', n, 'k =', k,'m =',m)
# print('Общее количество натуральных решений =', total)

#бык корова теленок

#10*b + 5*k + 0.5*t = 100

# total = 0

# for b in range(1,10):
#     for k in range(1,20):
#         for t in range(1,200):
#             if b * 10 + k * 5 + t * 0.5 == 100 and b + k + t == 100:
#                 total +=1
#                 print('b =', b, 'k =', k,'t =',t)
# print('Общее количество натуральных решений =', total)  


# total = 0 

# for a in range(1,150):
#     for b in range(a,150):
#         for c in range(b, 150):
#              for d in range(c, 150):
#                 for e in range(d, 150):
#                     if (a **5 + b ** 5 + c ** 5 + d ** 5  < e **5):
#                         break
#                     if (a **5 + b ** 5 + c ** 5 + d ** 5  == e ** 5):
#                         total+=1
#                         print('a =', a, 'b =', b,'c =',c, 'd =',d,'e=',e)
#                         print(a+b+c+d+e)
# print('Общее количество натуральных решений =', total)



# total = 0 

# for a in range(1,151):
#     for b in range(a,151):
#         for c in range(b, 151):
#              for d in range(c, 151):
                    
#                     e = int((a **5) + (b ** 5) + (c ** 5) + (d ** 5))

#                     if e **5 <  int(a **5) + (b ** 5) + (c ** 5) + (d ** 5):
#                         break  

#                     if e **5 ==int(a **5) + (b ** 5) + (c ** 5) + (d ** 5):
#                         total+=1

#                         print('a =', a, 'b =', b,'c =',c, 'd =',d,'e=',e)
#                         print(a+b+c+d+e)
# print('Общее количество натуральных решений =', total)
