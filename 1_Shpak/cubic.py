# Упражнение: Напишите программу cubic.py, которая принимает три параметра a, b, c и вычисляет корни уравнения 
# x^3 + a * x^2 + b * x + c = 0 используя формулы Виета. 
# Обратите внимание, что в некоторых случаях корни представляют собой комплексные числа, а в самих формулах активно используются (прямые и обратные) гиперболические функции, а также функция sgn(x).


import sys
import math
import cmath

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

print("x^3 + ", a, " * x^2 + ", b, " * x + ", c, " = 0")

Q = (3 * b - a ** 2) / 9
R = (9 * a * b - 2 * a ** 3 - 27 * c) / 54
S = Q ** 3 + R ** 2

if S < 0:
	phi = 1 / 3 * cmath.acos(R / cmath.sqrt(- Q ** 3)) # не знаю, нужен math или cmath для нахождения acos
	print("x1 = ", 2 * cmath.sqrt(-Q) * cmath.cos(phi) - a / 3) # тоже, нужен тут math или cmath для нахождения cos
	print("x2 = ", 2 * cmath.sqrt(-Q) * cmath.cos(phi + 2 / 3 * math.pi) - a / 3) # тоже, нужен тут math или cmath для нахождения cos
	print("x3 = ", 2 * cmath.sqrt(-Q) * cmath.cos(phi - 2 / 3 * math.pi) - a / 3) # тоже, нужен тут math или cmath для нахождения cos
elif S > 0:
	if Q > 0:
		print("HELLO")
		phi = 1 / 3 * cmath.acosh(abs(R) / math.sqrt(Q ** 3))
		print("x1 = ", -2 * math.copysign(1, R) * math.sqrt(Q) * cmath.cosh(phi) - a / 3)
		print("x2 = ", math.copysign(1, R) * math.sqrt(Q) * cmath.cosh(phi) - a / 3 + complex(math.sqrt(3) * math.sqrt(Q) * cmath.sinh(phi)))
		print("x3 = ", math.copysign(1, R) * math.sqrt(Q) * cmath.cosh(phi) - a / 3 - complex(math.sqrt(3) * math.sqrt(Q) * cmath.sinh(phi)))
# 	if Q < 0:
# 		phi = 1 / 3 * math.acosh(abs(R) / math.sqrt(abs(Q) ** 3))
# 		print("x1 = ", -2 * math.copysign(1, R) * math.sqrt(abs(Q)) * math.sinh(phi) - a / 3)
# 		print("x2 = ", math.copysign(1, R) * math.sqrt(abs(Q)) * math.sinh(phi) - a / 3 + complex(math.sqrt(3) * math.sqrt(abs(Q)) * math.cosh(phi)))
# 		print("x3 = ", math.copysign(1, R) * math.sqrt(abs(Q)) * math.sinh(phi) - a / 3 - complex(math.sqrt(3) * math.sqrt(abs(Q)) * math.cosh(phi)))
# 	else:
# 		print("x1 = ", - math.pow(c - a ** 3 / 27, -1 / 3) - a / 3)
# 		print("x2 = ", -(a + x1) / 2 + j / 2 * math.sqrt(abs((a - 3 * x1)(a + x1) - 4 * b)))
# 		print("x3 = ", -(a + x1) / 2 - j / 2 * math.sqrt(abs((a - 3 * x1)(a + x1) - 4 * b)))
# else:
# 	print("x1 = ", -2 * math.copysign(1, R) * math.sqrt(Q) - a / 3)
# 	print("x2 = ", math.copysign(1, R) * math.sqrt(Q) - a / 3)