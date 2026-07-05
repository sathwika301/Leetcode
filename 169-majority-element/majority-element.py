           
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        hashmap={}
        for n in nums:
            hashmap[n]=hashmap.get(n,0)+1
      
        for key, value in hashmap.items():
            if value>len(nums)//2:
                return key
sol=Solution()
res=sol.majorityElement(nums = [3,3,4])
print(res)   