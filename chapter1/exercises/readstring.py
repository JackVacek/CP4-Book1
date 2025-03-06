import sys
a = sys.stdin.read().splitlines()
ans = []
for i in a:
    if i[0:7] == '.......':
        break
    ans.append(i)
print(' '.join(ans))