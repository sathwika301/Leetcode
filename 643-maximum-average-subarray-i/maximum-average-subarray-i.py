class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n=len(nums)
        curr=sum(nums[:k])
        max_sum=curr
        for i in range(k,n):
            curr+=nums[i]-nums[i-k]
            max_sum=max(max_sum,curr)
        return max_sum/k
            
        
        