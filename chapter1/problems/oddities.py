import sys
a = list(map(int,sys.stdin.read().splitlines()))[1:]
print(a)
for i in a:
    if i % 2 == 0:
        print(i,"is even")
    else:
        print(i,"is odd")