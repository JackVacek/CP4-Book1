import math
p,a,b,c,d,N = list(map(int,input().split()))
maxPrice = float('-inf')
minPrice = float('inf')
maxDecline = 0
for i in range(1,N+1):
    curr = p * (math.sin(a*i + b) + math.cos(c * i + d) + 2)
    if curr > maxPrice:
        maxPrice = curr
    elif curr < maxPrice:
        maxDecline = max(maxDecline, maxPrice-curr)
print(round(maxDecline,10))