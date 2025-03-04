n=int(input())
p=False
for i in range(n):
    items=int(input())
    name = input()
    hasPea=False
    hasPancake=False
    for j in range(items):
        b=input()
        if b == 'pea soup':
            hasPea=True
        elif b == 'pancakes':
            hasPancake=True
    if hasPea and hasPancake:
        print(name)
        p=True
        break
if not p:
    print("Anywhere is fine I guess")