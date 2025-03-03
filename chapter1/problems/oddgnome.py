T = int(input())
for i in range(T):
    nums = list(map(int,input().split()[1:]))
    first = 0
    second = 1
    while(nums[first] + 1 == nums[second]):
        first += 1
        second += 1
    print(first + 2)