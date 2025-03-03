import sys
X = int(input())
a=list(map(int,sys.stdin.read().splitlines()))[1:]
total = X * (len(a)+1)
print(total - sum(a))