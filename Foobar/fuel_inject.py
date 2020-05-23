import math
n=int(input("Enter a num : "))
count=0
while n>0:
    print(n,end="\t")
    if (n&n-1)==0:
        print("\n")
        print(int(count+math.log2(n)))
        break
    else:
        if n&1==0:
            n=n//2
        elif n+1 & n == 0:
            n=n+1
        else:
            n=n-1
    count+=1









