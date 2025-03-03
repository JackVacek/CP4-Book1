def calcScore(high, low):
    if high == 2 and low == 1:
        return 1000
    if high == low:
        return high * 100
    return high * 10 + low
import sys
lines = sys.stdin.read().splitlines()
for line in lines:
    player1 = list(map(int,line.split()[:2]))
    player2 = list(map(int, line.split()[2:]))
    if player1 == [0,0] and player2 == [0,0]:
        break
    player1[0],player1[1] = max(player1[0],player1[1]), min(player1[0],player1[1])
    player2[0],player2[1] = max(player2[0],player2[1]), min(player2[0],player2[1])
    p1s = calcScore(player1[0], player1[1])
    p2s = calcScore(player2[0], player2[1])
    if p1s == p2s:
        print("Tie.")
    elif p1s > p2s:
        print("Player 1 wins.")
    else:
        print("Player 2 wins.")
    
    