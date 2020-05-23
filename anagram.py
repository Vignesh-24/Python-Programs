from collections import  defaultdict
dict1=defaultdict(lambda :0)
flag=1
text1,text2=input().split()
if len(text1)!=len(text2):
    print("Not Anagrams")
for i in range(len(text1)):
    dict1[text1[i]]+=1
    dict1[text2[i]]-=1
print(dict1)
for v in dict1.values():
    if v!=0:
        print("Not Anagrams")
        flag=0
        break
if flag!=0:
    print("Anagrams")


