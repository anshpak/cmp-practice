import sys, math

b = float(sys.argv[1])
c = float(sys.argv[2])

d = math.sqrt(b * b - 4 * c)

print('x^2 + ' + sys.argv[1] + 'x + ' + sys.argv[2])
print('x1 = ' + str((-b + d)/2))
print('x2 = ' + str((-b - d)/2))