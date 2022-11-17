
# f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

import sympy as sym
from scipy.optimize import fsolve as sci_fsolve
import matplotlib.pyplot as plt
import numpy

# описание глобальных переменных
funcrange = [-10, 10]
leftnum = min(funcrange)
rightnum = max(funcrange)

# Можно определить корни только на заданном интервале.
def f(x):
    return -12 * x ** 4 * numpy.sin(
        numpy.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30

# нахождение корней на интервале
def solution():
    global leftnum, rightnum
    temp = leftnum
    rightnum = rightnum
    roots = []
    interval = []

    while temp < rightnum:
        # определяются интервалы, где функция переходит через 0
        if f(temp) >= 0 and f(temp + 1) <= 0:
            w = sci_fsolve(f, temp)
            roots.append(*w)
        # определяются интервалы, где функция переходит через 0
        if f(temp) <= 0 and f(temp + 1) >= 0:
            w = sci_fsolve(f, temp)
            roots.append(*w)
        # если функция возрастает, добавляется список интервалов
        if f(temp) > f(temp + 1) < f(temp + 2):
            interval.append(temp + 1)
        temp += 1
    # список корней с округлением
    roots = [round(i, 2) for i in roots]
    print(f'Корни уравнения для интервала от {leftnum} до {rightnum}: {roots}')

    return roots


# Определить промежутки, на которых f>0 и f<0:
def func_interval(left, right):
    array = []
    temp = left
    while left < right:
        array.append([f(left), left])
        left += 0.1
    if array[0][0] > 0:
        print(f'f > 0 в промежутке {temp, right}')
        return max(array)
    else:
        print(f'f < 0 в промежутке {temp, right}')
        return min(array)


# Вычисляем координаты вершины функции на заданном интервале:
def maxima_and_minima():
    # корни уравнения (точки, в которых значение функции равно нулю)
    roots = solution()
    if len(roots) < 2:
        print('На заданном интервале нет вершин')
    else:
        top = []
        for i in range(len(roots) - 1):
            top.append(func_interval(roots[i], roots[i + 1]))
        for j in top:
            j = [round(i, 2) for i in j]
            print(f'Координаты вершин функции: [{j[1]}, {j[0]}]')
        if len(top) < 2:
            print('error')
        else:
            for i in range(len(top) - 1):
                if top[i][0] > top[i + 1][0]:
                    print(f'На участке {round(top[i][0], 1)}...{round(top[i + 1][0], 1)} функция убывает')
                else:
                    print(f'На участке {round(top[i][0], 1)}...{round(top[i + 1][0], 1)} функция возрастает')


# График функции при помощи библиотеки matplotlib:
start = -100
finish = 100

x = [x for x in range(start, finish + 1)]
y = [(-12 * x ** 4 * sym.sin(sym.cos(x)) - 18 * x ** 3 + 5 * x ** 2 + 10 * x - 30) for
     x in range(start, finish + 1)]
plt.plot(x, y)
plt.grid()
plt.hlines(0, start, finish)
plt.title('graph using matplotlib')
plt.show()

maxima_and_minima()