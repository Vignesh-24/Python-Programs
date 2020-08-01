def quicksort(arr,strt,end):
    if strt<end:
        pivot=partition(arr,strt,end)
        quicksort(arr,strt,pivot-1)
        quicksort(arr,pivot+1,end)

def partition(arr,strt,end):
    pivot=arr[end]
    i=strt
    for j in range(strt,end):
        if arr[j]<=pivot:
            arr[i],arr[j]=arr[j],arr[i]
            i+=1
    arr[i],arr[end]=arr[end],arr[i]
    return i

arr=list(map(int,input().split()))
quicksort(arr,0,len(arr)-1)
print(arr)
