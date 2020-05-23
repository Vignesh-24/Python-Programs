def maxsubset(val,wt,total):
    dp_list=[[0 for j in range(total+1)]  for i in range(len(val))]
    for i in range(len(val)):
        for j in range(total+1):
            if j==0:
                dp_list[i][j]=0
                continue
            if i==0 and j-wt[i]>=0:
                dp_list[i][j]=val[i]
                continue
            if j-wt[i]>=0:
                dp_list[i][j]=max(val[i]+dp_list[i-1][j-wt[i]],dp_list[i-1][j])
            else:
                dp_list[i][j]=dp_list[i-1][j]
    i,j=len(val)-1,total
    req=list()
    while dp_list[i][j] != 0 and i >= 0 :
        if i!=0 and dp_list[i-1][j]==dp_list[i][j]:
            i-=1
        else:
            req.append(val[i])
            j-=wt[i]
            i -= 1
    return req

