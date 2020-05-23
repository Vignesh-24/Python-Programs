from collections import deque
def bfs(src_i,src_j,dest_i,dest_j):
    print(src_i,src_j,dest_i,dest_j)
    queue=deque()
    #assuming i am already strted in frst level
    count=1
    flag=1
    queue.append(src_i)
    queue.append(src_j)
    while queue:
        cur_i=queue.popleft()
        if cur_i=='*':
            queue.append('*')
            #marking the end of one level so as to count moves
            count+=1
            cur_i=queue.popleft()
        cur_j=queue.popleft()
        #looping through all possible nodes for current node
        for i,j in zip((1,1,2,2,-1,-1,-2,-2),(2,-2,1,-1,-2,2,1,-1)):
            if cur_i+i>=0 and cur_i+i<8 and cur_j+j>=0 and  cur_j+j<8 and arr[cur_i+i][cur_j+j]!=1:
                arr[cur_i+i][cur_j+j]=1
                queue.append(cur_i+i)
                queue.append(cur_j+j)
                if cur_i+i==dest_i and cur_j+j==dest_j:
                    #if found in frst traversal return count as it is already included else add 1 to current level
                    return str(count) if flag==1 else str(count+1)
        if flag==1:
            queue.append("*")
            flag=0
        print(queue)
    return "Not Possible"
s,d=map(int,input("Source and destination : ").split())
arr=[[0 for j in range(8)] for i in range(8)]
print(bfs(s//8,s%8,d//8,d%8))

