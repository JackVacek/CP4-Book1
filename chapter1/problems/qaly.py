N = int(input())
total = 0
for i in range(N):
    a=list(map(float,input().split()))
    total+=a[0]*a[1]
print(total)