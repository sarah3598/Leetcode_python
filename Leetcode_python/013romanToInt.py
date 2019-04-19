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
if __name__=='__main__':
    m="MCMXCIV"
    print(romanToInt(m))




