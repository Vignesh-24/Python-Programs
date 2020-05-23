def findnextLargest(n):
    if int(n) > num2:
        return n
    temp=[i for i in n[::-1]]
    l=len(temp)
    point = -1
    for i in range(l - 1):
        if temp[i] > temp[i + 1]:
            point = i + 1
            break
    if point == -1:
       return "-1"
    for i in range(l):
        if temp[i] > temp[point]:
            temp[i], temp[point] = temp[point], temp[i]
            break
    temp=temp[l - 1:point - 1:-1]+temp[0:point]
    return findnextLargest("".join(temp))
num1,num2=map(int,input("enter two numbers : ").split())
print(findnextLargest(str(num1)))
