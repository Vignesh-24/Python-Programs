import time
def computePattern():
    j,i=0,1
    while(i<n):
        if pat[i]==pat[j]:
            patlist.append(j+1)
            j+=1
            i+=1
        elif j!=0:
            j=patlist[j-1]
        else:
            patlist.append(0)
            i+=1
start=time.time()
text,pat=input().split()
m,n=len(text),len(pat)
patlist=[0]
computePattern()
j=i=0
print(patlist)
while(i<m and j<n):
    if pat[j]==text[i]:
        j+=1
        i+=1
    elif j!=0:
        j=patlist[j-1]
    else:
        i+=1
if j==n:
    print("Present",time.time()-start)
else:
    print("Not Present",time.time()-start)








