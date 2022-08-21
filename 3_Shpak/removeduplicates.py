# Упражнение: Напишите программу removeduplicates.py, которая принимает на вход файл с построчно заданными 
# данными и удаляет из него все дубликаты (без изменения порядка строк в столбце). 
# На выходе программа выводит количество удаленных строк (дубликатов).

import sys

f = open(sys.argv[1], 'r')
res = []
data = f.read().split('\n')
# data = [line[:len(line) - 1] for line in f]
count = 0
for i in data:
	if i in res:
		continue
	else:
		res += [i]
print(len(data) - len(res))
f.close()
f = open('removeduplicates.txt', 'w')
for i in res:
	f.write(i + '\n')
f.close