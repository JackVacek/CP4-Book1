points=list(map(int,input().split()))
if points[0] != 0 and points[0] == points[1]:
    print("Even",points[0]+points[1])
elif points[0] != points[1]:
    print("Odd",max(points[0],points[1])*2)
else:
    print("Not a moose")
