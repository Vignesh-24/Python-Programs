from collections import defaultdict
def sum_digit(i):
    sum=0
    while(i>0):
        sum+=i%10
        i=i//10
    return sum

sums=defaultdict(lambda : 0)
for i in range(300,400):
    sums[sum_digit(i)]+=1
for i in sums:
    print(i,sums[i])