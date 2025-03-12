def shuffle(N,type):
    deck = [i for i in range(N)]
    OG = deck[:]
    c = 0
    while True:
        c += 1
        newDeck = []
        if type=="out":
            mid = (N+1)//2
            left = deck[:mid]
            right = deck[mid:]
            for i in range(len(right)):
                newDeck.append(left[i])
                newDeck.append(right[i])
            if len(left) > len(right):
                newDeck.append(left[-1])
        else:
            mid = N//2
            left = deck[:mid]
            right = deck[mid:]
            for i in range(len(left)):
                newDeck.append(right[i])
                newDeck.append(left[i])
            if len(right) > len(left):
                newDeck.append(right[-1])
        if newDeck == OG:
            return c
        else:
            deck = newDeck
N, type = input().split()
N = int(N)
print(shuffle(N,type))