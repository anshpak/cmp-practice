# Упражнение: Напишите программу integraltrap.py, которая вычисляет интеграл функции ArcTan(x)/x по методу трапеций. 
# Здесь отрезок также разбивается на равные интервалы, но приближение ведется не прямоугольниками, а трапециями, как показано на рисунке.

import sys, math

def f(x):
	if x == 0:
		return 1
	else:
		return math.atan(x) / x

a = float(sys.argv[1])
b = float(sys.argv[2])
n = int(sys.argv[3])

h = (b - a) / n
el = a
s = 0

while el < b:
	s += (f(el) + f(el + h)) / 2 * h
	el += h

print(s)