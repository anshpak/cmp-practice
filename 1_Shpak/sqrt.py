# Упражнение: Дополните программу sqrt.py еще одним вычислением корня, но теперь при помощи метода Ньютона, 
# описанного выше, т.е. уточняя оценку пересечением касательной к графику x^2-c. 
# Сначала проведите необходимые вычисления на бумаге, а затем перенесите формулу в код. 
# Выведите конечный результат и количество шагов для каждого метода.

# import sys, math

# c = float(sys.argv[1])
# t = c
# eps = 1e-2
# i = 0

# while abs(t - c / t) > eps:
# 	t = (t + c / t) / 2.0
# 	i += 1

# print(t, i)

# t = c
# i = 0

# def f(x):
# 	return x ** 2 - c

# def g(x):
# 	return 2 * x

# while abs(t - c / t) > eps:
# 	t = t - f(t) / g(t)
# 	i += 1

# print(t, i)

import sys, math
c = float(sys.argv[1])
t = c
eps = 1e-15
i = 0
while abs(t - c/t) > eps:

        t = (t + c/t) / 2.0
        i += 1
        print(i)

print(t)