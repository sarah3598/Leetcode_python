#######solution1###########
def longestCommonPrefix(strs):
    l=len(strs)
    flag=0
    res=[]
    k=0
    if l>=2:
        minl=len(strs[0])
    elif l==1:
         return strs[0]
    else:
        return ""
    for i in range(l):
        if len(strs[i])<minl:
            minl=len(strs[i])
    while k<minl:
        for j in range(1,l):
            if list(strs[j]).pop(k)!=list(strs[j-1]).pop(k):
               flag=1
               if len(res)==0:
                    return  ""
               else:
                   return ''.join(res)
        if flag==0:
            res.append(list(strs[j]).pop(k))
            k=k+1
    return ''.join(res)
######solution2#######


if __name__=='__main__':
    t=["flower","flow","flight"]
    t2=["dog","racecar","car"]
    t3=[]
    t4=["a"]
    t5=["c","c"]
    print(longestCommonPrefix(t5))
