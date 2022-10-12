#1. Вычислить число c заданной точностью d    
#Пример: при d = 0.001, π = 3.141    10^(-1) ≤ d ≤10^(-10)



def nikalant_row(d: int) -> float:
    pi, sign, m = 3, 1, 2
    while abs(pi - (pi + sign*4/(m**3+3*m**2+2*m))) > 10**(-d-1):
        pi = pi + sign*4/(m**3+3*m**2+2*m)
        sign = -1*sign
        m = m+2
    return round((pi + (pi + sign*4/(m**3+3*m**2+2*m)))/2, d)

d = int(input('Введите заданную точность определения числа ПИ: '))
pi = nikalant_row(d)
print(f'С точностью {d=}, число {pi=}; ')