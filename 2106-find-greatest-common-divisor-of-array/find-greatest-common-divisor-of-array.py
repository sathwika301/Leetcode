class Solution:
    def findGCD(self, nums: List[int]) -> int:
        small=min(nums)
        large=max(nums)
        mul=[]
        res=[]
        for i in range(1,large+1):
            if small%i==0:
                mul.append(i)
            if large%i==0:
                if i in mul:
                    res.append(i)
        return max(res)
        