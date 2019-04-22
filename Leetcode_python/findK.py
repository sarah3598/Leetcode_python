#coding=utf-8
def findK(l1,l2,k):
    #l=len(l1)
    l3=[]
    i=0
    j=0
    while i+j<=k-1:
        if l1[i]<l2[j]:
            l3.append(l1[i])
            i=i+1
        elif l1[i]>l2[j]:
            l3.append(l2[j])
            j=j+1
        else:
            l3.append(l1[i])
            l3.append(l2[j])
            i=i+1
            j=j+1
    return l3,l3[k-1]
if __name__=='__main__':
    a=[3,7,9]
    b=[0,3,11]
    k=3
    print(findK(a,b,k))