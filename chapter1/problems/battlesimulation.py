from collections import deque
mappings = {'R':'S','B':'K','L':'H'}
counts={}
moves=list(input())
curr=deque([])
ans=[]
for move in moves:
    counts[move] = counts.get(move,0) + 1
    curr.append(move)
    if counts.get('R',0) > 1 or counts.get('B',0) > 1 or counts.get('L',0) > 1:
        whatToTake=curr.popleft()
        counts[whatToTake] -= 1
        ans.append(mappings[whatToTake])
    elif counts.get('R',0) == 1 and counts.get('B',0) == 1 and counts.get('L',0) == 1:
        ans.append('C')
        counts.clear()
        curr.clear()
for i in curr:
    ans.append(mappings[i])
print(*ans,sep='')