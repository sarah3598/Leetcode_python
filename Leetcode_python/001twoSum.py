def twoSum(nums, target):
    res=[]
    for i in range(0,len(nums)-1):
        p1 = nums[i]
        for j in range(i+1,len(nums)):
            if nums[j]==target-p1:
                res.append(i)
                res.append(j)
                return  res
            continue
if __name__=='__main__':
    list=[2,7,11,15]
    t=9
    print(twoSum(list,t))
