# 3. Задайте список из n чисел последовательности (1+ 1/n)^n и выведите на экран их сумму (округляйте до 3 знаков после запятой).    
# Пример:    
# - Для n = 6: [2, 2.25, 2.37, 2.441, 2.488, 2.522]
#Вывод: 14.031 (2 + 2.25 + 2.37 + 2.441 + 2.448 + 2.522)


t = int(input('Введите число: ')) 

def sequence(t):

    return[round((1 + 1 / a)**a, 3) for a in range (1, t + 1)]   
        
        
print(sequence(t))
print(round(sum(sequence(t)),3))







