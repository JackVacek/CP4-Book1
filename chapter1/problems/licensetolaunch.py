minDay = float('inf')
minIndex = -1
N = int(input())
nums = list(map(int,input().split()))
for i in range(N):
    if nums[i] < minDay:
        minDay = nums[i]
        minIndex = i
print(minIndex)