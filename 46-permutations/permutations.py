class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res=[]
        def backtrack(path):
            if len(path)==len(nums):
                res.append(path[:])
                return 
            for n in nums:
                if n not in path:
                    path.append(n)
                    backtrack(path)
                    path.pop()
        backtrack([])
        return res