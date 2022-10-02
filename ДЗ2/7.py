# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.    
# Пример:    
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def multiply_number(k):
          if k==1:
              answer =  1
          else:
              answer = k*multiply_number(k-1)
          return answer
  
num = int(input("Введите число: "))
list = []
while num !=0:
      list.append(multiply_number(num))
      num-=1
print(list[::-1])



