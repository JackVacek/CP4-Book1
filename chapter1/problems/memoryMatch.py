N = int(input())
K = int(input())
cards = ["Unknown"] * N
for i in range(K):
    parts = input().split()
    c1,c2=int(parts[0])-1, int(parts[1])-1
    p1,p2=parts[2],parts[3]
    cards[c1]=p1
    cards[c2]=p2
    if p1 == p2:
        cards[c1] = 'Matched'
        cards[c2] = 'Matched'
faceDown = [card for card in cards if card != 'Matched']
picCounts = {}
for card in faceDown:
    if card != 'Unknown':
        picCounts[card] = picCounts.get(card,0) + 1
pairs = 0
singles = 0
for pic, count in picCounts.items():
    pairs += count // 2
    singles += count % 2
unknown = faceDown.count("Unknown")
score = pairs
if singles >= unknown:
    score += unknown
elif unknown == 2:
    score += 1
print(score)