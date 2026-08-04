class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res=[]
        small=min(nums)
        large=max(nums)
        for i in range(small+1,large):
            if i in nums:
                continue
            else:
                res.append(i)
        return res
        