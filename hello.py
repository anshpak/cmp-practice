import sys
print('Hi, ' + sys.argv[1] + ' ' + sys.argv[2] + '. How are you?')
print(sys.argv[0])

# ВОПРОС: что хранится в sys.argv[0]?
# ОТВЕТ: забавно было узнать, что имя файла hello.py, то есть текущего файла

# ВОПРОС: как Python реагирует на ошибки в коде, вызвав программу без аргументов?
# ОТВЕТ: IndexError: list index out of range - выбрасывает исключение