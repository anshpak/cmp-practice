# Упражнение: Выясните, какие еще функции есть в пакете random и с какими еще параметрами можно вызывать random.randrange()?
import random
print(dir(random))
print(random.getrandbits(100))

# Упражнение: Вычислите значение функции sgn(x) для предварительно заданного x используя конструкцию if … elif … else.

import sys

num = int(sys.argv[1])

if num > 0:
	print(1)
elif num < 0:
	print(-1)
else:
	print(0)