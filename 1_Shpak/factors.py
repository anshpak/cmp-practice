# Упражнение: Оптимизируйте программу factors.py уменьшив количество итераций. 
# Действительно, если мы ищем множители числа 100, то достаточно проверить делители 2..10, 
# т.е. все такие делители что factor * factor <= n.

import sys
import time
import math

# start = time.time()
# factor n, e.g. 36 = 2 * 2 * 3 * 3

n = int(sys.argv[1])

factor = 2
s = ''

bdr = math.floor(math.sqrt(n))

while (n > 1 and factor <= bdr):
	while (n % factor == 0):
		s += str(factor) + ' '
		n //= factor
	factor += 1

if n != 1:
	s += str(n)

# end = time.time()
print(s)
# print(end - start))