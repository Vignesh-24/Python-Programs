from math import ceil, log2

def build(node,strt,end):
    if strt==end:
        s_arr[node]=arr[strt]
    else:
        mid=(strt+end)//2
        build(2*node,strt,mid)
        build(2*node+1,mid+1,end)
        s_arr[node]=s_arr[2*node]+s_arr[2*node+1]

def update(node,strt,end,index,val):
    if strt==end:
        arr[index]=val
        s_arr[node]=val
    else:
        mid=(strt+end)//2
        if strt<=index and index <= mid:
            update(node*2,strt,mid,index,val)
        else:
            update(node*2+1,mid+1,end,index,val)
        s_arr[node]=s_arr[node*2]+s_arr[node*2+1]

arr=[2,5,6,1,4,7,8,10,17]
n=len(arr)
maxsize=2*(2**int(ceil(log2(n))))-1
s_arr=[0]*(maxsize+1)
build(1,0,n-1)
print(arr)
print(s_arr)
update(1,0,n-1,7,23)
print(arr)
print(s_arr)

