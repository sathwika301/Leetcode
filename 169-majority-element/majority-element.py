           
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count=0
        ele=0
        for n in nums:
            if count==0:
                ele=n
                count=1
            elif ele==n:
                count+=1
            else:
                count-=1
        return ele
sol=Solution()
res=sol.majorityElement(nums = [3,3,4])
print(res)   