from itertools import combinations
n = int(input())
m = range(1, n+1)
print(*(list(combinations(m,i)) for i in m))