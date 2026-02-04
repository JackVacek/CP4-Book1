import sys
lines = sys.stdin.readlines()
for line in lines:
    n,m = map(int,line.split())
    print(abs(n-m))