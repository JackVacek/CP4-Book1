import sys
names = sys.stdin.read().splitlines()
names = names[1:]
nb = sorted(names, reverse=True)
ns = sorted(names)
if names == nb:
    print("DECREASING")
elif names == ns:
    print("INCREASING")
else:
    print("NEITHER")