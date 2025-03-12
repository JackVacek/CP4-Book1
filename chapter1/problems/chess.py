T = int(input())
board = [["Black" if (i+j)%2==0 else "White" for j in range(8)] for i in range(8)]
for i in range(T):
    moves = input().split()
    r1,c1,r2,c2 = int(ord(moves[0])-ord('A')),int(moves[1])-1,int(ord(moves[2])-ord('A')), int(moves[3])-1
    if r1 == r2 and c1 == c2:
        print('0 '+chr(r1+ord('A'))+" "+str(c1+1))
        continue
    if board[r1][c1] != board[r2][c2]:
        print("Impossible")
        continue
    elif abs(r1-r2) == abs(c1-c2):
        print('1 ' + chr(r1 + ord('A')) + " " + str(c1+1) + " " + chr(r2 + ord('A')) + " " + str(c2+1))
    else:
        intermediate = False
        for r in range(8):
            for c in range(8):
                if (r == r1 and c == c1) or (r == r2 and c == c2):
                    continue
                if abs(r - r1) == abs(c - c1) and abs(r - r2) == abs(c - c2):
                    print('2 ' + chr(r1 + ord('A')) + " " + str(c1+1) + " " + 
                          chr(r + ord('A')) + " " + str(c+1) + " " + 
                          chr(r2 + ord('A')) + " " + str(c2+1))
                    intermediate = True
                    break
            if intermediate:
                break