class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n=len(nums)
        prefix=[1]*n
        suffix=[1]*n
        res=[0]*n
        for i in range(1,n):
            prefix[i]=prefix[i-1]*nums[i-1]
        
        for j in range(n-2,-1,-1):
            suffix[j]=suffix[j+1]*nums[j+1]

        
        for k in range(n):
            res[k]=prefix[k]*suffix[k]
        return res
        