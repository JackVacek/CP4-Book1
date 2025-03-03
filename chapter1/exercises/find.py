import bisect
into = list(map(int,input().split()))
value = int(input())
idx = bisect.bisect_left(into, value)
if idx != len(into) and into[idx] == value:
    print('is there')
print('not there')