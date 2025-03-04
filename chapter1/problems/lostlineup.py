N = int(input())
pos = list(map(int, input().split()))
friends = [1] + [-1] * (N-1)
for i in range(N-1):
    friends[pos[i]+1] = 2 + i
print(*friends)