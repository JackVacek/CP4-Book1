N = int(input())
for i in range(1,N+1):
    s=list(input())
    t=list(input())
    overallDiff = 0
    oneDiff = 0
    oneToZero = 0
    zeroToOne = 0
    for j in range(len(s)):
        if s[j] != t[j]:
            overallDiff+=1
        if s[j] == '?' and t[j] == '1':
            oneDiff -= 1
        elif s[j] == '0' and t[j] == '1':
            oneDiff -= 1
            zeroToOne += 1
        elif s[j] == '1' and t[j] == '0':
            oneToZero += 1
            oneDiff += 1
    if oneDiff > 0:
        print('Case', str(i) + ":",'-1')
        continue
    print('Case', str(i) + ':',overallDiff - min(oneToZero, zeroToOne))