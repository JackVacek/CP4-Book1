import sys
nums = sys.stdin.read().splitlines()
for i in range(len(nums)-1):
    prev = nums[i]
    curr = str(len(nums[i]))
    count = 1
    while prev != curr:
        prev, curr = curr, str(len(curr))
        count +=1
    print(count)