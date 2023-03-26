''' Cpaвнить вpeмя вычиcлeния пepeмнoжeния 1-, 2- и 3-мepныx мaccивoв пoпapнo чepeз cтaндapтнyю
библиoтeкy Python и чepeз библeoтeкy NumPy. Haчepтить гpaфик зaвиcимocти вpeмeни oт кoличecтвa 
элeмeнтoв мaccивa и интерполировать/aппpoкcимиpoвaть eгo. '''

from random import randint
import numpy as np
import time
import matplotlib.pyplot as plt
# from scipy.interpolate import interp1d

n = 100 # int(input('Введите n: ')) # длина массива
l = 50 # число-ограничение значений внутри массива

# определение массивов
one_dim_matrix_A = [randint(0, l) for i in range(n)]
# print(len(one_dim_matrix_A))
one_dim_matrix_B = [randint(0, l) for i in range(n)]

two_dim_matrix_A = [[randint(0, l) for i in range(n)] for j in range(n)]
two_dim_matrix_B = [[randint(0, l) for i in range(n)] for j in range(n)]

three_dim_matrix_A = [[[randint(0, l) for i in range(n)] for j in range(n)] for k in range(n)]
three_dim_matrix_B = [[[randint(0, l) for i in range(n)] for j in range(n)] for k in range(n)]
#
one_dim_array_A, one_dim_array_B = np.array(one_dim_matrix_A), np.array(one_dim_matrix_B)
two_dim_array_A, two_dim_array_B = np.array(two_dim_matrix_A), np.array(two_dim_matrix_B)
three_dim_array_A, three_dim_array_B = np.array(three_dim_matrix_A), np.array(three_dim_matrix_B)

# определим функцию поэлементного умножения
def multiply(A, B, t, order):
    if order == 1:
        C = []
        for i in range(t):
            C.append(A[i] * B[i])
        return C
    elif order == 2:
        C = [[None for i in range(n)] for j in range(n)]
        for i in range(t):
            for j in range(t):
                C[i][j] = A[i][j] * B[i][j]
        return C
    elif order == 3:
        C = [[[None for i in range(n)] for j in range(n)] for k in range(n)]
        for i in range(t):
            for j in range(t):
                for k in range(t):
                    C[i][j][k] = A[i][j][k] * B[i][j][k]
        return C
    else:
        return 1

# ВЫЧИСЛЯЕМ ТОЧКИ ДЛЯ ОСИ ВРЕМЕНИ
# без использования модуля numpy
period_1 = [None for i in range(n)]
for t in range(n):
    go_off = time.time()
    one_dim_matrix_C = multiply(one_dim_matrix_A, one_dim_matrix_B,t, 1)
    period_1[t] = time.time() - go_off
# print(period_1)
period_2 = [None for i in range(n)]
for t in range(n):
    go_off = time.time()
    two_dim_matrix_C = multiply(two_dim_matrix_A, two_dim_matrix_B,t, 2)
    period_2[t] = time.time() - go_off
# print(period_2)

period_3 = [None for i in range(n)]
for t in range(n):
    go_off = time.time()
    three_dim_matrix_C = multiply(three_dim_matrix_A, three_dim_matrix_B,t, 3)
    period_3[t] = time.time() - go_off
# print(period_3)

# подключим операцию '*' из numpy
period_1_np = [None for i in range(n)]
for t in range(n):
    go_off = time.time()
    one_dim_array_C = one_dim_array_A * one_dim_array_B
    period_1_np[t] = time.time() - go_off
# print(period_1_np)

period_2_np = [None for i in range(n)]
for t in range(n):
    go_off = time.time()
    two_dim_array_C = two_dim_array_A * two_dim_array_B
    period_2_np[t] = time.time() - go_off
# # print(period_2_np)

period_3_np = [None for i in range(n)]
for t in range(n):
    go_off = time.time()
    three_dim_array_C = three_dim_array_A * three_dim_array_B
    period_3_np[t] = time.time() - go_off
# print(period_3_np)

# Построение графиков зависимостей period(n)
# dim = 1
plt.title('Зависимость времени от количества элементов массива\n')
plt.xlabel('$n$')
plt.ylabel('time, s')
fp = np.polyfit(range(n), period_1, 2) # linear
f = np.poly1d(fp)
plt.plot(range(n), period_1, 'mv', range(n), f(range(n)), 'k--', linewidth=1, markersize=6)
fp = np.polyfit(range(n), period_1_np, 1) # linear
f = np.poly1d(fp)
plt.plot(range(n), period_1_np, 'c>', range(n), f(range(n)), 'k-', linewidth=1, markersize=5)
plt.legend(['1-dim', 'linear', '1-dim-np', 'linear'], loc='best')
plt.show()

# dim = 2
plt.title('Зависимость времени от количества элементов массива')
plt.xlabel('$n$')
plt.ylabel('time, s')
fp = np.polyfit(range(n), period_2, 2) # quadratic
f = np.poly1d(fp)
plt.plot(range(n), period_2, 'mv', range(n), f(range(n)), 'k--', linewidth=1, markersize=6)
fp = np.polyfit(range(n), period_2_np, 1) # linear
f = np.poly1d(fp)
plt.plot(range(n), period_2_np, 'c>', range(n), f(range(n)), 'k-', linewidth=1, markersize=5)
plt.legend(['2-dim', 'quadratic', '2-dim-np', 'linear'], loc='best')
plt.show()

# dim = 3
plt.title('Зависимость времени от количества элементов массива')
plt.xlabel('$n$')
plt.ylabel('time, s')
fp = np.polyfit(range(n), period_3, 3) # cubic
f = np.poly1d(fp)
plt.plot(range(n), period_3, 'mv', range(n), f(range(n)), 'k--', linewidth=1, markersize=6)
fp = np.polyfit(range(n), period_3_np, 1) # linear
f = np.poly1d(fp)
plt.plot(range(n), period_3_np, 'c>', range(n), f(range(n)), 'k-', linewidth=1, markersize=5)
plt.legend(['3-dim', 'cubic', '3-dim-np', 'linear'], loc='best')
plt.show()


