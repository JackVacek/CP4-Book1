N=int(input())
teas = list(map(int,input().split()))
M=int(input())
toppings=list(map(int,input().split()))
minCost = float('inf')
for i in range(N):
    pairings = list(map(int,input().split()))
    pairings = pairings[1:]
    for j in pairings:
        minCost = min(minCost, teas[i]+toppings[j-1])
money=int(input()) - minCost
c=0
while money > 0:
    money -= minCost
    c+=1
print(c)