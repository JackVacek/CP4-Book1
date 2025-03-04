word = input()
ds = False
for c in range(len(word)-1):
    if word[c] == word[c+1] and word[c] == 's':
        ds = True
        break
if ds:
    print("hiss")
else:
    print('no hiss')