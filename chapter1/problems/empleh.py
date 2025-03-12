def place(person, moves, board):
    for move in moves:
        if len(move) == 2:
            col = 2 + (ord(move[0])-ord('a'))*4
            row = 16 - int(move[1]) - (int(move[1])-1)
            if person == "White":
                piece = "P"
            else:
                piece = 'p'
            board[row][col] = piece
        else:
            col = 2 + (ord(move[1])-ord('a'))*4
            row = 16 - int(move[2]) - (int(move[2])-1)
            if person == "White":
                piece = move[0].upper()
            else:
                piece = move[0].lower()
            board[row][col] = piece
board = []
border = list('+---+---+---+---+---+---+---+---+')
first = '|:::|...|:::|...|:::|...|:::|...|'
second = '|...|:::|...|:::|...|:::|...|:::|'
board.append(border)
for i in range(8):
    if i % 2 == 1:
        board.append(list(first))
    elif i % 2 == 0:
        board.append(list(second))
    board.append(border)
for i in range(2):
    player = input().split()
    if len(player) > 1:
        moves = player[1].split(',')
        if i % 2 == 0:
            place('White',moves,board)
        else:
            place('Black',moves,board)
for i,row in enumerate(board):
    row = ''.join(row)
    board[i] = row
    print(board[i])
