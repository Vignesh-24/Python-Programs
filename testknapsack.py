from Dp import Knapsack
n=int(input("Enter Total Weight "))
print('Enter Values of items')
val=list(map(int,input().split()))
print("Enter weights of items")
wt=list(map(int,input().split()))
print("Max Values can be included :",Knapsack.maxsubset(val,wt,n))