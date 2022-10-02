#5. Реализуйте алгоритм перемешивания списка.

from random import randint

def mix_list(list_one):
     list = list_one[:]
     list_length = len(list)
     for i in range(list_length):
         index_any = randint(0, list_length - 1)
         temp = list[i]
         list[i] = list[index_any]
         list[index_any] = temp
     return list
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed_list = mix_list(list)
print("Исходный список: ")
print(list)
print("Перемешанный список: ")
print(mixed_list)






