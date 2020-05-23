class Coin:
    def __init__(self):
        pass
    def findDenomination(self,arr,r_amount):
        if r_amount==0:
            return []
        req_list=[]
        list_dp=[[0 for j in range(r_amount+1) ] for i in range(len(arr))]
        for i in range(len(arr)):
            for j in range(1,r_amount+1):
                if j < arr[i]:
                    list_dp[i][j]=list_dp[i-1][j]
                elif j-arr[i] >= 0:
                    if i==0:
                        list_dp[i][j] =  1 + list_dp[i][j - arr[i]]
                    else:
                        list_dp[i][j] = min(list_dp[i - 1][j], 1 + list_dp[i][j - arr[i]])
        i=len(arr)-1
        j=r_amount
        while list_dp[i][j] != 0:
            if i!=0 and list_dp[i][j]==list_dp[i-1][j]:
                i-=1
            else:
                req_list.append(arr[i])
                j-=arr[i]
        if sum(req_list)==r_amount:
            return req_list
        else:
            return  []