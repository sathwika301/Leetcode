class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n=len(nums)
      
        minimum=nums.index(min(nums))
        maximum=nums.index(max(nums))
        
        l=min(minimum,maximum)
        r=max(minimum,maximum)
        return min(r+1,n-l,l+1+n-r)
        