# Упражнение: Напишите программу dictsearch.py, которая реализует линейный и бинарный поиск слов в отсортированном словаре dict.txt. Программа должна находить все слова из словаря, которые начинаются с заданной строки.
# Линейный поиск означает, что вы последовательно просматриваете слова пока не найдете первое похожее, после чего добираете все остальные. Время выполнения такого поиска O(n).
# Бинарный (двоичный) поиск заключается в том, что на каждом шаге диапазон слов делится на две части и в работе остается та половина, где находится искомое слово. Упрощает ситуацию то, что операторы сравнения “<” и “>” в Python выполняют сравнение лексикографически (“b” > “a”, “bb” > “ba”, etc). Время выполнения O(logn). Бинарный поиск иногда относят к методу “разделяй и властвуй”, хотя здесь происходит большая задача на каждом шаге сводится к более простой.
# Входные параметры: название файла (словарь) и строка поиска.
# На выходе: список найденных слов и затраченное время для 1) линейного и 2) бинарного поисков.

import sys, time

def linear_search(data, word):
	res = []
	i = 0
	while (i < len(data)) and (not data[i].startswith(word)):
		i += 1
	while (i < len(data)) and data[i].startswith(word):
		res += [data[i]]
		i += 1
	return res 

# def binary_search(data, word):
# 	# print(data, len(data) - 1, mid)
# 	if len(data) == 0:
# 		return 0
# 	mid = (len(data) - 1) // 2
# 	if word < data[mid]:
# 		return binary_search(data[:mid], word)
# 	elif word > data[mid]:
# 		return binary_search(data[mid + 1:], word) + mid + 1
# 	else:
# 		return mid

def binary_search(data, word):
	# print(data, len(data) - 1, mid)
	a = 0
	b = len(data) - 1
	while a <= b:
		mid = (a + b) // 2
		if word < data[mid]:
			b = mid - 1
		elif word > data[mid]:
			a = mid + 1
		else:
			return mid
	return None

f = open(sys.argv[1])
word = sys.argv[2]
data = f.read().split('\n')
f.close()
start = time.time()
print(linear_search(data, word))
end = time.time()
print(end - start)
# 
start = time.time()
res = []
index = binary_search(data, word)
if index:
	while (index < len(data)) and (data[index].startswith(word)):
		res += [data[index]]
		index += 1
print(res)
end = time.time()
print(end - start)
# 
# print('############################')
# print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], -100))
# 