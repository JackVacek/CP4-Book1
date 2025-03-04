L,N=list(map(int,input().split()))
c=0
curr=L
for i in range(N):
    a,b=input().split()
    if a=='enter':
        if curr-int(b)<0:
            c+=1
        else:
            curr-=int(b)
    else:
        curr+=int(b)
print(c)