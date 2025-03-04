from collections import Counter
c=input().split()
c=[i[0] for i in c]
b=Counter(c)
print(max(b.values()))