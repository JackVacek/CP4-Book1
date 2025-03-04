a,b,c = sorted(list(map(int,input().split())))
maxDiff = max(abs(a-b), abs(b-c))
minDiff = min(abs(a-b), abs(b-c))
if maxDiff == minDiff:
    print(c+minDiff)
elif abs(a-b) > abs(b-c):
    print(a + minDiff)
elif abs(a-b) < abs(b-c):
    print(b + minDiff)