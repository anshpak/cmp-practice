# Упражнение: Напишите программу queue.py, в которой реализуйте следующий набор операций над очередью используя collections.deque:
# def create_queue() – создает пустую очередь и возвращает ее
# def is_empty(queue) – проверяет, пуста ли очередь (возвращает true – пуст и false – нет)
# def enqueue(queue, item) – добавляет элемент в очередь
# def dequeue(queue) – возвращает первый элемент и удаляет его из очереди (если очередь не пустая, иначе сообщение об ошибке)
# def peek(queue) – возвращает первый элемент (без удаления)
# Далее создайте очередь, добавьте туда 100 тыс. случайных чисел, потом достаньте их всех пока очередь не станет пустой. 
# Выведите время выполнения и финальный размер очереди.

from collections import deque
import random as rnd
import time

class Queue:
	def __init__(self):
		self.items = deque()

	def is_empty(self):
		if self.is_empty:
			print("Queue is empty")
			return None
		else:
			if len(self.items) == 0:
				return True
			else:
				return False

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		return self.items.popleft()

	def peek(self):
		return self.items[0]

start = time.time()
queue = Queue()
for i in range(100000):
	queue.enqueue(rnd.randrange(1000) - 500)

for i in range(100000):
	queue.dequeue()

end = time.time()
print(end - start, len(queue.items))