# Упражнение: Напишите программу postfixcalc.py, в которой реализуйте вычисление арифметического выражения, 
# заданного постфиксной (польской) нотацией, при помощи стека. Алгоритм вычисления приведен там же. 
# Выражение задается на входе строкой вида “4 3 2 * +”. Поддерживаются целые числа и арифметические операции +, -, *, /. 
# Если выражение содержит другие символы или не является корректным, то выводится “invalid input”.

import sys

class Stack:
	def __init__(self):
		self.items = []

	def is_empty(self):
		if len(self.items) == 0:
			return True
		else:
			return False

	def pop(self):
		if self.is_empty():
			print("Stack is empty")
			return None
		else:
			return self.items.pop()

	def push(self, item):
		self.items.append(item)

	def peek(self):
		return self.items[len(self.items) - 1]

def is_correct(lst_expr):
	signs = ('+', '-', '*', '/')
	count = 0
	try:
		for i in lst_expr:
			if i not in signs:
				int(i)
			else:
				count += 1
	except ValueError:
		return False
	return True if (len(lst_expr) - count) == (count + 1) else False

def calc_expr(lst_expr):
	stack = Stack()
	signs = ('+', '-', '*', '/')
	i = 0
	while i <= len(lst_expr) - 1:
		if lst_expr[i] in signs:
			a = stack.pop()
			b = stack.pop()
			if abs(b) > abs(a):
				a, b = b, a
			if lst_expr[i] == '+':
				stack.push(a + b)
			elif lst_expr[i] == '-':
				stack.push(a - b)
			elif lst_expr[i] == '*':
				stack.push(a * b)
			elif lst_expr[i] == '/':
				stack.push(a / b)
		else:
			stack.push(int(lst_expr[i]))
		#
		# print(i, stack.items)
		#
		i += 1
	return stack.pop()

# в условии есть пример '3 9 + 2 / 5 * 15 10 - 5 / -'

expr = sys.argv[1]
lst_expr = expr.split(' ')
if is_correct(lst_expr):
	print(calc_expr(lst_expr))
else:
	print("invalid input")