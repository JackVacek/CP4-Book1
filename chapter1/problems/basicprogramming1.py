N,t=list(map(int,input().split()))
A=list(map(int,input().split()))
if t==1:
    print(7)
elif t==2:
    if A[0] > A[1]:
        print('Bigger')
    elif A[0] == A[1]:
        print("Equal")
    else:
        print("Smaller")
elif t==3:
    asub=sorted(A[0:3])
    print(asub[1])
elif t==4:
    print(sum(A))
elif t==5:
    print(sum(list([x for x in A if x % 2 == 0])))
elif t==6:
    for i in A:
        print(chr((i%26)+97),end='')
    print()
elif t==7:
    i = 0
    seen = set()
    while i != len(A)-1:
        seen.add(i)
        i = A[i]
        if i in seen:
            print("Cyclic")
            break
        if i >= len(A):
            print("Out")
            break
    if i == len(A)-1:
        print('Done')            
    