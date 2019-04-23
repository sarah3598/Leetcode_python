#####solution1####faster####
def romanToInt(s):
    d={
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    i = 1
    count = last = d[s[0]]
    while i < len(s):
        current = d[s[i]]
        if current > last:
            count -= last * 2
        count += current
        last = current
        i += 1
    return count
# ########solution2########
# def romanToInt(s):
#     d = {'I': 1,
#          'V': 5,
#          'X': 10,
#          'L': 50,
#          'C': 100,
#          'D': 500,
#          'M': 1000
#          }
#     res = 0
#     if len(s) < 2:
#         return d[s[0]]
#     res = res + d[s[0]]
#     for i in range(1,len(s)):
#         res = res + d[s[i]]
#         if d[s[i]] > d[s[i - 1]]:
#             res = res - 2 * d[s[i-1]]
#     return res
#
#
# if __name__=='__main__':
#     m="MCMXCIV"
#     print(romanToInt(m))




