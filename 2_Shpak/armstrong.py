# Упражнение: Напишите программу armstrong.py, которая для заданного целого числа n находит все числа Армстронга <= n. 
# Число из k цифр называется числом Армстронга, если сумма его цифр, возведенных в k-ую степень, равна самому числу.

import sys

n = int(sys.argv[1])

def isArmstrong(num):
	lst = [int(i) for i in list(str(num))]
	deg = len(lst)
	if sum([dig ** deg for dig in lst]) == num:
		return True
	else:
		return False

print([i for i in range(1, n + 1) if isArmstrong(i)])