# ВОПРОС: как Python обрабатывает деление на 0?
# print(4 / 0)
# ОТВЕТ: выбрасывает исключение ZeroDivisionError: division by zero

# ВОПРОС: как Python обрабатывает выражения с несколькими операторами типа 2 ** 3 ** 4 или 2 + 3 * 4 или 1 / 2 + 3?
# print(2 ** 3 ** 4) # сначала в степень возводится тройка
# print(2 + 3 * 4) # 12
# print(1 / 2 + 3) # 3.5
# print(0 ** 0) # 1
# print(5 % 2 % 1 % 2) # 0
# print(5 // 2 // 2 // 10 // 12) # 0
# print(5 % 10) # 5
# ОТВЕТ: Python обрабатывает выражения с несколькими операторами в соотствии с приоритетом операторов

# Сравните результаты вычислений 123**45 и 123.0**45.0
print(123 ** 45 == 123.0 ** 45.0)
# Результат: False из-за потери точности

# Импортируйте модуль math, после чего вычислите math.sqrt(10) и math.sqrt(-1)
import math
print(math.sqrt(10))
# math.sqrt(-1) # ValueError: math domain error

# Проверьте применимость основных операций к комплексному числу
a = complex(1, 2)
b = 3 + 4j
print(a + b)
print(a * b)
print(a / b)
# print(a % b) # TypeError: unsupported operand type(s) for %: 'complex' and 'complex'
# print(a // b) # TypeError: unsupported operand type(s) for //: 'complex' and 'complex'
print(a ** 5)
print(a ** b)

# ВОПРОС: что будет, если извлечь корень из отрицательного числа используя math.sqrt(-1)? 
# Теперь загрузите другой пакет cmath (ответственный за работу с комплексными числами) и повторите попытку.
# math.sqrt(-1) # ValueError: math domain error
import cmath
print(cmath.sqrt(-1)) # 1j

# Создайте строковое выражение вида
# 1
# 2 3
# 4 5 6
# и выведите его при помощи функции print()
print("1\n2 3\n4 5 6")

# Постройте таблицу истинности для выражения a and not b 
# поочередно вычисляя его для разных значений a и b, например, True and not True, True and not False, ...
print("a        b        a and not b")
print(True, "   ", True, "   ", True and not True) # False
print(True, "   ", False, "  ", True and not False) # True
print(False, "  ", True, "   ", False and not True) # False
print(False, "  ", False, "  ", False and not False) # False

# Упражнение: Проверьте, что выражения a and b и not (not a or not b) эквивалентны, 
# построив таблицу истинности сначала для одного, а потом для второго выражения
print("a        b        a and b   not (not a or not b)")
print(True, "   ", True, "   ", True and True, "    ", not (not True or not True)) # False
print(True, "   ", False, "  ", True and False, "   " , not (not True or not False)) # True
print(False, "  ", True, "   ", False and True, "   ", not (not False or not True)) # False
print(False, "  ", False, "  ", False and False, "   ", not (not False or not False)) # False