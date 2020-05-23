from Dp import CoinDenomination as coin
n=int(input("Enter required Amount :"))
arr=list(map(int,input().split()))
print(coin.Coin().findDenomination(arr,n))