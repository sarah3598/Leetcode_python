#######solution1#######
# def isPalindrome(x):
#     if x<0:
#         return False
#     else:
#         l=str(x)
#        #newl=reversed(l)
#         newl=l[::-1]
#         i=0
#         while l[i] is newl[i]:
#             if i<len(l)-1:
#                 i=i+1
#             else:
#                 return True
#         return False
######solution2########
# def isPalindrome(x):
#     if x<0:
#         return False
#     else:
#         l = str(x)
#         for i in range(len(l)//2):
#             j=len(l)-i-1
#             if l[i] is not l[j]:
#                 return False
#                 break
#         return True
#####solution 3########
def isPalindrome(x):
    if x<0:
        return False
    y=x
    b=0
    while x!=0:
        b=x%10+10*b
        x//=10
    if b==y:
        return True
    return False

if __name__=='__main__':
    a=121
    print(isPalindrome(a))




