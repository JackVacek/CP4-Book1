problems = list(map(int,input().split()))
print("YES" if problems[0] > 0 and problems[1] > 0 and problems[2] > 0 and sum(problems[0:3]) >= problems[3] and problems[3] >= 3 else "NO")