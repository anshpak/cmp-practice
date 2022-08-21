# Напишите программу oracle.py, которая использует описанные выше бинарный поиск для отгадывания заданного 
# пользователем числа. На входе подается число n, после чего программа сначала предлагает 
# задать целое число не превышающее n, а затем последовательно выводит свою догадку, а пользователь 
# отвечает либо 0 (меньше), либо 1 (больше), либо 2 (угадано). Замечание: Пользователь может запутаться, 
# что приведет к логическому противоречию – отследите это.

import sys, random

b = int(sys.argv[1])
a = 1
trials = 0
print(f'Please think of a number between {a} and {b}.')

try:
	while a <= b:
		trials += 1
		guess = (a + b) // 2 
		print(f'My guess is {guess}.')
		print(f'[0 = number < {guess}, 1 = number > {guess}, 2 = I guessed it]')
		res = int(input())
		if res == 1:
			a = guess + 1
		elif res == 0:
			b = guess - 1
		elif res == 2:
			raise
except:
	print(f'Your number is {guess}. It took {trials} trials.')
else:
	print('You made a mistake')