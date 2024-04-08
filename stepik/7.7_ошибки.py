
print('-1-' * 30)

# count = 0
# p = 1

# for _ in range(1, 10 + 1):
#     x = int(input())
    
#     if x >= 0:
#         p = p * x
#         count = count + 1
    
# if count > 0:
#     print(count)
#     print(p)
    
# else:
#     print('NO')

print('-2-' * 30)

# mx = -1000000
# s = 0
# for i in range(1, 11):
#     x = int(input())
#     if x < 0:
#         s = s + x
#         if x > mx:
#             mx = x
# if s < 0:
#         print(s)
#         print(mx)
# else:
#         print('NO')

print('-3-' * 30)

# s = 0
# for i in range(1, 7+1):
#     n = int(input())
#     if n % 2 == 0:
#         s = s + n
# print(s)


print('-4-' * 30)

n = int(input())
max_digit = -1

while n !=0:
    digit = n % 10
    if digit % 3 == 0:
        
        if digit > max_digit:
            max_digit = digit
    n = n // 10
if  max_digit  == -1:
    print('NO')
else:
    print(max_digit)
    