#1. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.


a = [int(s) for s in input().split()]
res = [x for x in a if a.count(x)==1]
print(res)        
