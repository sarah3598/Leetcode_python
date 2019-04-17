###solution1####small data
# def reverse(x):
#     res=[]
#     t=0
#     p=1 #记录位数
#     y=x
#     if x<0:
#         x=-x
#     while x//10!=0:
#         p=p+1
#         res.append(x%10)
#         x=x//10
#     res.append(x)
#     l=p
#     p=p-1
#     for i in range(l):
#         t=t+res[i]*(10**p)
#         p=p-1
#     if y>0:
#         return  t
#     else:
#         return  -t

def reverse(x):
    res = 0
    if x > 0 and x <= 2 ** 31 - 1:
        l = list(str(x))
        newl = l[::-1]
        res = int(''.join(newl))
        if res > 2 ** 31:
            return 0
        else:
            return res
    elif x < 0 and x >= - 2 ** 31:
        l2 = list(str(abs(x)))
        newl2 = l2[::-1]
        res = int(''.join(newl2)) * (-1)
        if res < -2 ** 31:
            return 0
        else:
            return res
    else:
        res = 0
if __name__=='__main__':
    a=123
    print(reverse(a))



