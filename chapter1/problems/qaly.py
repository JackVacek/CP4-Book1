N=int(input())
t=0.0
for i in range(N):
    a,b=map(float,input().split())
    t += a*b
print(f"{t:.3f}")