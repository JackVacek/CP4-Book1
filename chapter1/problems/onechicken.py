nums = list(map(int,input().split()))
pieces = "pieces"
if abs(nums[1] - nums[0]) == 1:
    pieces = "piece"
if nums[1] > nums[0]:
    print("Dr. Chaz will have",nums[1]-nums[0], pieces, "of chicken left over!")
else:
    print("Dr. Chaz needs", nums[0]-nums[1], "more",pieces, "of chicken!")