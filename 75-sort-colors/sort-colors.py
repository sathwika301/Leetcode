class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        c1=0
        c2=0
        c3=0
        for i in nums:
            if i==0:
                c1+=1
            
            elif i==1:
                c2+=1
            
            elif i==2:
                c3+=1
            
        for j in range(c1):
            nums[j]=0
        
        for k in range(c1,(c1+c2)):
            nums[k]=1
            
        for l in range((c1+c2),(c1+c2+c3)):
            nums[l]=2
    
sol=Solution()
sol.sortColors(nums = [2,0,2,1,1,0])
        