N = int(input())
for i in range(N):
    nums = input()
    if nums[1] == "=":
        print("skipped")
    else:
        nums = list(map(int,nums.split("+")))
        print(sum(nums))