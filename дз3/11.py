# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.    
# Пример:    
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12




def sum_index(spisok):
    a = 0
    for i in range(len(spisok)):
        if i % 2 != 0:
            a += spisok[i]
    print(f"Сумма равна: {a}")

spisok = [2, 3, 5, 9, 3]
sum_index(spisok)
spisok = list(map(int, input("Введите числа через пробел:\n").split()))
sum_index(spisok)