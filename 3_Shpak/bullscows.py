# Упражнение: Напишите программу bullscows.py, которая интерактивно играет с пользователем в игру “Быки и коровы”. 
# Компьютер загадывает случайное 4-значное целое число (от 1000 до 9999), 
# в котором все цифры разные. Пользователь пытается отгадать это число, а компьютер дает ему подсказки говоря 
# сколько в числе пользователя “быков” и “коров”:
# “быки” -- цифры, которые есть в обоих числах, причем на тех же местах
# “коровы” -- цифры, которые есть в обоих числах, но на разных местах

import random as rnd
num = ''
n = str(rnd.randrange(1, 10))
num += n
while len(num) != 4:
	n = str(rnd.randrange(10))
	if n in num:
		continue
	else:
		num += n
print('I\'ve thought of a number between 1000 and 9999. Try to guess it.')
print(num)
guess = input('Enter your guess: ')
trials = 1
while guess != num:
	cows = 0
	bulls = 0
	for i in range(4):
		if guess[i] == num[i]:
			bulls += 1
	for i in range(4):
		if guess[i] in num and guess[i] != num[i]:
			cows += 1
	print(f'Bulls: {bulls}')
	print(f'Cows: {cows}')
	guess = input('Enter your guess: ')
	trials += 1
print(f'You won! It took {trials} trials.')