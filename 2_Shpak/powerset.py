import sys, copy

n = int(sys.argv[1])

result = [[]]

for i in range(1, n + 1):
        new = copy.deepcopy(result)
        for j in range(len(new)):

                new[j].append(i)
        result += new

print(result)