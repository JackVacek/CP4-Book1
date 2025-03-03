import sys
a=sys.stdin.read().splitlines()
for line in a:
    line=list(map(int,line.split()))
    print(abs(line[0]-line[1]))