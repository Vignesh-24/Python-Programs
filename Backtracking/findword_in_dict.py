def findword(board,visited,row,col,word,dictn):
    if word in dictn:
        result.add(word)
    if len(word)==r*c or (word not in trie):
        return
    for i in range(len(path_row)):
        new_row=row+path_row[i]
        new_col=col+path_col[i]
        if(valid(new_row,new_col,visited)):
            visited[new_row][new_col]=1
            findword(board,visited,new_row,new_col,word+board[new_row][new_col],dictn)
            visited[new_row][new_col]=0
def valid(row,col,visit):
    if row>=0 and row < r and col >= 0 and col < c and visit[row][col]==0:
        return True
    else:
        return False
r,c=map(int,input("Enter no of rows and columns ").split())
board=[[j for j in input().split()] for i in range(r)]
visited=[[0 for j in range(c)] for i in range(r)]
dictn=set(input("Enter words in Dictionary in space seperated single line : ").split())
trie=set()
for w in dictn:
    for j in range(1,len(w)+1):
        trie.add(w[:j])
path_row=[-1,-1,-1,0,1,1,1,0]
path_col=[-1,0,1,1,1,0,-1,-1]
result=set()
for i in range(r):
    for j in range(c):
        visited[i][j]=1
        findword(board,visited,i,j,board[i][j],dictn)
        visited[i][j]=0
print(*result)


