X=int(input())
N=int(input())
t=0
for i in range(N):
    t += X
    t -= int(input())
print(t+X)