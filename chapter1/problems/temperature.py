nums = list(map(int,input().split()))
if nums[0] == 0 and nums[1] == 1:
    print("ALL GOOD")
elif nums[1] == 1:
    print("IMPOSSIBLE")
else:
    print(round(nums[0]/(1-nums[1]), 6))