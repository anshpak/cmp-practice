import random, time

def findsum(arr):
	s = 0
	for elem in arr:
		s += elem
	return s

def findavg(arr):
	s = 0
	n = 0 
	for elem in arr:
		s += elem
		n += 1
	return s / n

lst1 = list(range(1000000))
lst2 = list(range(2000000))
lst3 = list(range(5000000))
lst4 = list(range(10000000))

print('elements\tfindsum:\tfindavg:\tratio:')
start1 = time.time()
findsum(lst1)
end1 = time.time()
start2 = time.time()
findavg(lst1)
end2 = time.time()
a = round(end1 - start1, 6)
b = round(end2 - start2, 6)
res = "%s\t\t%s\t%s\t%s" % (1000000, a, b, round(a / b, 2))
print(res)

start1 = time.time()
findsum(lst2)
end1 = time.time()
start2 = time.time()
findavg(lst2)
end2 = time.time()
a = round(end1 - start1, 6)
b = round(end2 - start2, 6)
res = "%s\t\t%s\t%s\t%s" % (2000000, a, b, round(a / b, 2))
print(res)

start1 = time.time()
findsum(lst3)
end1 = time.time()
start2 = time.time()
findavg(lst3)
end2 = time.time()
a = round(end1 - start1, 6)
b = round(end2 - start2, 6)
res = "%s\t\t%s\t%s\t%s" % (5000000, a, b, round(a / b, 2))
print(res)

start1 = time.time()
findsum(lst4)
end1 = time.time()
start2 = time.time()
findavg(lst4)
end2 = time.time()
a = round(end1 - start1, 6)
b = round(end2 - start2, 6)
res = "%s\t%s\t%s\t%s" % (10000000, a, b, round(a / b, 2))
print(res)