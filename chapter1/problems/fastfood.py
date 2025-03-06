T = int(input())
for i in range(T):
    N,M = list(map(int,input().split()))
    requirements=[]
    prizes = []
    total=0
    for j in range(N):
        p=list(map(int,input().split()))
        requirements.append(p[1:len(p)-1])
        prizes.append(p[-1])
    stickers=list(map(int,input().split()))
    for j in range(len(requirements)):
        mini = float('inf')
        for k in range(len(requirements[j])):
            mini=min(mini,stickers[requirements[j][k]-1])
        total += mini * prizes[j]
    print(total)