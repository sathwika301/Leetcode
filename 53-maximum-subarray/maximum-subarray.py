class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr=0
        max_sum=nums[0]
        for n in nums:
            if curr<0:
                curr=0
            curr=curr+n
            max_sum=max(curr,max_sum)
        return max_sum
            
        