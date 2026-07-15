class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n=len(nums)
        hashmap=[0]*n
        for i in range(n):
            if hashmap[nums[i]]==0:
                hashmap[nums[i]]=1
            else:
                return nums[i]
        
        