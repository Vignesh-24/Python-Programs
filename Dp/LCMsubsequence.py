class Lcmsubseq:
    def findsubsequence(self,str1,str2):
        dp_list=[[0 for j in range(len(str1)+1)] for i in range(len(str2)+1)]
        for i in range(len(str2)+1):
            for j in range(len(str1)+1):
                if i==0 or j==0:
                    dp_list[i][j]=0
                    continue
                if str1[j-1]==str2[i-1]:
                    dp_list[i][j]=1+dp_list[i-1][j-1]
                else:
                    dp_list[i][j]=max(dp_list[i-1][j],dp_list[i][j-1])
        str3=''
        i,j=len(str2),len(str1)
        while i>0:
            index = dp_list[i][j]
            if i!=0 and index==dp_list[i-1][j]:
                i-=1
            elif j!=0 and index==dp_list[i][j-1]:
                j-=1
            else:
                str3+=str2[i-1]
                i-=1
                j-=1
        return str3[::-1]
