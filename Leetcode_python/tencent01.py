input_l=input().strip()
n=int(input_l)
res=[]
for i in range(n):
    t=input()
    res.append(int(t))
res.sort()
res2=res
minl=res[0]
maxl=res[n-1]
j=0
temp=0
while j<n-1:
    a=res.pop()
    b=res.pop()
    res.append(a*b+1)
    j=j+1
minl=res[0]
k=0
while k<n-1:
    a=res2.pop(0)
    b=res2.pop(0)
    res2.append(a*b+1)
    k=k+1
maxl=res2[0]
print(maxl-minl)