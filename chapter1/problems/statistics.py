import sys
a=sys.stdin.read().splitlines()
for x,i in enumerate(a):
    nums = list(map(int,i.split()[1:]))
    mini = min(nums)
    maxi = max(nums)
    print("Case",str(x+1) + ':',mini,maxi,maxi-mini)