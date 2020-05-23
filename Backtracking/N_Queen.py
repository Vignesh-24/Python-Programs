def find_place(col,board):
    if n<4:
        return False
    if col>=n:
        return True
    for i in range(n):
        if safe(i,col,board):
            board[i][col]=1
            if find_place(col+1,board):
                return True
            board[i][col]=0
    return False

def safe(row,col,board):
    if any(board[row][place] for place in range(n)):
        return False
    for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    for i,j in zip(range(row,n),range(col,-1,-1)):
        if board[i][j]==1:
            return False
    return True

n=int(input("Enter no of Queens : "))
board=[[0 for j in range(n)] for i in range(n)]
if find_place(0,board):
    print("Queen can be placed")
    print(*board,sep='\n')
else:
    print("Queen Cannot be placed")
