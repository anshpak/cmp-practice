# Упражнение: Напишите программу integralmc.py, в которой при помощи метода Монте-Карло вычисляется интеграл функции sin(x)/x 
# на заданном отрезке [a, b]. Количество точек также является входным параметром. 
# Замечание: Задайте функцию так, чтобы интеграл считался на любом отрезке, даже если он включает точку 0.

import sys
import random as rnd
import math

a = int(sys.argv[1])
b = int(sys.argv[2])
N = int(sys.argv[3])
K = 0
lst_y = []

for i in range(N):
	pt_x = rnd.uniform(a, b)
	pt_y = rnd.uniform(0, 1)
	if pt_x == 0:
		pt_x = 1
	if abs(math.sin(pt_x) / pt_x) >= abs(pt_y):
		lst_y += [pt_y]
		K += 1

S_rec = abs(b - a) * max(lst_y)
print(S_rec * K / N)