# Упражнение: На основе программы binary.py напишите программу baseform.py, 
# которая для заданных числа и основания (от 2 до 10) выводит представление числа в этой системе счисления.

import sys

num = int(sys.argv[1])
base = int(sys.argv[2])
i = 0
n = 1

while(base ** n * (i + 1) <= num):
	# print(i, n)
	# print(base ** n * (i + 1))
	if i + 1 == base:
		i = 1
		n += 1
	else:
		i += 1

# возможно, было бы проще сначала посчитать максимальную степень n у выражения base ** n < num,
# а уже потом попробовать пройтись от [1, base) и найти нужный i, но я уже сделал так

s = ''
s += str(i)
num = num - base ** n * i
n -= 1

while n >= 0:
	i = 0
	while(base ** n * (i + 1) <= num):
		i += 1
	s += str(i)
	num = num - base ** n * i
	n -= 1

print(s)