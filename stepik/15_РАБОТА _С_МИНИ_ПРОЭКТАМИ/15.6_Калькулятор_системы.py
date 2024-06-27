print('--Функция bin()=='*2)
# # двоичная система
# print(bin(10))        
# print(bin(128))
# print(bin(150))
# print(bin(18765))

# # 0b1010
# # 0b10000000
# # 0b10010110
# # 0b100100101001101

print('--Функция oct())=='*2)
# #восьмиричная система

# print(oct(10))
# print(oct(128))
# print(oct(150))
# print(oct(18765))

# # 0o12
# # 0o200
# # 0o226
# # 0o44515

print('--Функция hex()=='*2)
# #шестнатцатиричная система

# print(hex(10))
# print(hex(128))
# print(hex(150))
# print(hex(18765))

# # 0xa
# # 0x80
# # 0x96
# # 0x494d

# #Примечания Если нам требуется избавиться от приставок 0b, 0o, 0x, то мы можем воспользоваться строковым срезом

# num = 127

# bin_num = bin(num)  # 0b1111111
# oct_num = oct(num)  # 0o177
# hex_num = hex(num)  # 0x7f

# print(bin_num[2:])  # 1111111
# print(oct_num[2:])  # 177
# print(hex_num[2:])  # 7f

# num = 127432

# hex_num = hex(num)          # 0x1f1c8
# print(hex_num[2:].upper())  # 1F1C8