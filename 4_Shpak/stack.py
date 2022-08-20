# УПРАЖНЕНИЕ: Напишите программу stack.py, в которой реализуйте следующий набор стековых операций используя list или collections.deque:
# def create_stack() – создает пустой стек и возвращает его
# def is_empty(stack) – проверяет, пуст ли стек (возвращает true – пуст и false – нет)
# def push(stack, item) – добавляет элемент в стек
# def pop(stack) – возвращает верхний элемент и удаляет его из стека (если стек не пуст, иначе сообщение об ошибке)
# def peek(stack) – возвращает верхний элемент стека (без удаления)
# Далее создайте стек, добавьте туда 100 тыс. случайных чисел, потом достаньте их всех пока стек не станет пустым. Выведите время выполнения и финальный размер стека.

# РЕШЕНИЕ:

from collections import deque
import random as rnd
import time

# с помощью collections.deque, перечисление функций
# def create_stack():
# 	return deque()

# def is_empty(stack):
# 	if len(stack):
# 		return False
# 	else:
# 		return True

# def push(stack, item):
# 	stack.append(item)
# # ВОПРОС: как это работает? Почему изменения влияют на stack?

# def pop(stack):
# 	if is_empty(stack):
# 		print("Error. Stack is empty")
# 	else:
# 		return stack.pop()

# def peek(stack):
# 	return stack[len(stack) - 1]

# с помощью collections.deque, класс

class Stack():
	def __init__(self):
		self.items = deque()

	def is_empty(self):
		if len(self.items):
			return False
		else:
			return True

	def push(self, item):
		self.items.append(item)

	def pop(self):
		if self.is_empty():
			print("Error. Stack is empty")
			return None
		else:
			return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

start = time.time()
stack = Stack()
for i in range(100000):
	stack.push(rnd.randrange(1000) - 500)

while not stack.is_empty():
	stack.pop()
end = time.time()
print(end - start, len(stack.items))