N, D = input().split()
total = 0
myDict = {'A':11, 'K':4,'Q':3,'JD':20,'JND':2,'T':10,'9D':14, '9ND':0}
for i in range(int(N)*4):
    num,suit = list(input())
    if num == 'J' or num == '9':
        if suit == D:
            suit = 'D'
        else:
            suit = 'ND'
        total += myDict[num+suit]
    elif num in myDict:
        total += myDict[num]
print(total)