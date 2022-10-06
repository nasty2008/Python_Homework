# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.    
# Пример:    
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] 


def negaFib(k):

    if k == 0 or k == 1:
        return k
    if k == -1:
        return -k
    if k < 0:
        return round(negaFib(abs(k)) * (-1)**(k + 1))
    else:
        return negaFib(k - 1) + negaFib(k - 2)


k = int(input('Введите число: '))
for i in range(-k, k + 1):
    print(negaFib(i), end=' ')