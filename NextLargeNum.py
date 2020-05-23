n=int(input())
temp=[]
while n!=0:
    temp.append(n%10)
    n//=10
l= len(temp)
point=-1
for i in range(l-1):
    if temp[i] > temp[i+1]:
       point=i+1
       break
if point==-1:
    print("Not Possible")
    exit(1)
for i in range(l):
    if temp[i] > temp[point]:
        temp[i],temp[point]=temp[point],temp[i]
        break
print(temp[::-1])
int(temp)
print(*temp[l-1:point-1:-1],*temp[0:point],sep='')




