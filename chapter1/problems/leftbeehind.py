import sys
a=sys.stdin.read().splitlines()
for i in a:
    nums = list(map(int,i.split()))
    if nums[0] == 0 and nums[1] == 0:
        break
    if sum(nums) == 13:
        print("Never speak again.")
    elif nums[1] > nums[0]:
        print("Left beehind.")
    elif nums[1] == nums[0]:
        print("Undecided.")
    else:
        print("To the convention.")