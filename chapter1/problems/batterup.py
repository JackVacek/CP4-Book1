N=int(input())
nums = list(map(int,input().split()))
nums=[i for i in nums if i != -1]
print(sum(nums)/len(nums))