def quicksort(L,start,end):
    if start<end:
        i,j,p=start,end,L[start]
        while i<j:
            while i<j and L[j]>p:
                j=j-1
            if i<j:
                L[i]=L[j]
                i=i+1
            while i<j and L[i]<p:
                i=i+1
            if i<j:
                L[j]=L[i]
                j=j-1
        L[i]=p
        quicksort(L,start,i-1)
        quicksort(L,j+1,end)
    return L
if __name__=='__main__':
    L=[4,2,5,1,56,12,44,0]
    print(quicksort(L,0,len(L)-1))
