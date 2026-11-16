class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        min_size=float('inf')
        curr_sum=0
        i=0
        for j in range(len(nums)):
            curr_sum+=nums[j]
            while curr_sum>=target:
                min_size=min(min_size,j-i+1)
                curr_sum-=nums[i]
                i+=1
        if min_size==float('inf'):
            return 0 
        else:
            return min_size

        