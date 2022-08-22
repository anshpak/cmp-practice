# Упражнение: Напишите программу checkbrackets.py, которая для текстовой строки, состоящей из круглых скобок, 
# проверяет правильность этого скобочного выражения используя стек. Скобочное выражение правильное если:
# скобки сбалансированы, т.е. в каждой паре скобка сначала открывается, а потом закрывается
# скобка закрывается после того, как закрыты все скобки, открытые внутри нее
# Вход: строка вида “(()()(()()))”
# Выход: True/False

from collections import deque
import sys

class Stack:
	def __init__(self):
		self.items = deque()

	def is_empty(self):
		return True if len(self.items) == 0 else False

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if self.is_empty():
			# print('Error. Stack is empty')
			return None
		else:
			return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

def is_correct(brackets):
	stack = Stack()
	for i in brackets:
		if i == '(':
			stack.push('(')
		else:
			if stack.pop() == None:
				return False
	return stack.is_empty()

brackets = sys.argv[1]
print(is_correct(brackets))