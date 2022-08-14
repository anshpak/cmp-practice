# Упражнение: Напишите программу tally.py, которая для заданного на входе массива выводит матрицу 
# [[элемент 1, кол-во в списке], [элемент 2, кол-во в списке], ...] (прямо как функция Tally в Mathematica). 
# Элементы упорядочивать не нужно. Массив, как обычно, задается строкой.

import sys

lst = sys.argv[1].split(',')
ln = len(lst)

for i in range(ln):
	lst[i] = int(lst[i])

new_lst = [[el, lst.count(el)] for el in lst]

res = []
for el in new_lst:
	if not el in res:
		res.append(el)
	else:
		continue

print(res)