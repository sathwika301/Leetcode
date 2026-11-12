class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        n=len(nums)
        if n<k:
            return 0
        curr=sum(nums[:k])
        max_sum=curr
        max_avg=max_sum/k
        for i in range(k,len(nums)):
            curr+=nums[i]-nums[i-k]
            max_sum=max(max_sum,curr)
            new_avg=max_sum/k
            max_avg=max(max_avg,new_avg)
        return max_avg
            
        
        