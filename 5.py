#5.Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.    
#Пример:    
#A (3,6); B (2,1) -> 5,09
#A (7,-5); B (1,-1) -> 7,21


print('Введите координаты точки А:')
X_A = float(input('X: '))
Y_A = float(input('Y: '))
print('Введите координаты точки B:')
X_B = float(input('X: '))
Y_B = float(input('Y: '))

distance = (((X_B - X_A) ** 2) + ((Y_B - Y_A) ** 2)) ** 0.5
print(distance)
