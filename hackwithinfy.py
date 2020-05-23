n,d=map(int,input().split())
time,cost,speed={},{},{}
for i in range(n):
    t,c,sp=map(int,input().split())
    if t in time:
        if speed[t]<sp:
            speed[t]=sp
            cost[t]=c
            continue
        if speed[t]==sp and cost[t]>c:
            speed[t]=sp
            cost[t]=c
    else:
        time[t]=t
        cost[t]=c
        speed[t]=sp
mincost=0
for k in sorted(time.keys()):
    if mincost==0:
        prev=time[k]
        mincost+=cost[k]
        curspeed=speed[k]
        d-=curspeed
    else:
        if curspeed < speed[k]:
            d-=(time[k]-prev-1)*curspeed
            if d<=0:
                break
            curspeed=speed[k]
            d-=curspeed
            mincost+=cost[k]
            prev=time[k]
    if d<=0:
        break
print(cost,speed)
print(mincost)
