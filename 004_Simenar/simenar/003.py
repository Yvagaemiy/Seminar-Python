# Задача №27. 
# Пользователь вводит текст(строка). Словом считается 
# последовательность непробельных символов идущих 
# подряд, слова разделены одним или большим числом 
# пробелов или символами конца строки.Определите, 
# сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore;The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore,I'm sure that the shells are sea
# shore shells.
# Output: 19

texs1 = "She sells sea shells on the sea shore;The shellsthat she sells are sea shells I'm sure.So if she sells seashells on the sea shore,I'm sure that the shells are seashore shells "
print(texs1.split())

texs2 = texs1.lower().split()
print(len(texs2))
print(len(set(texs2)))
      
print(len(texs2) - len(set(texs2)))