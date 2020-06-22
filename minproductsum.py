n,k=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
pro=0
minn=0
diff=2*k
for i in range(len(a)):
    pro+=(a[i]*b[i])
for i in range(len(a)):
    temp=pro-(a[i]*b[i])
    minn=min(minn,temp+((a[i]+diff)*b[i]),temp+((a[i]-diff)*b[i]))
print(minn)
