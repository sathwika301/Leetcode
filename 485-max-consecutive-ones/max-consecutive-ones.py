
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left=0
        right=0
        maximum=0
        for right in range(len(nums)):
            if nums[right]==1:
                l=right-left+1
                maximum=max(maximum,l)
            else:
                left=right+1



        return maximum