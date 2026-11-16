class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        s=set(nums)
        longest=0
        for n in s:
            if n-1 not in s:
                count=1
                x=n
                while x+1 in s:
                    x+=1
                    count+=1
                longest=max(longest,count)
        return longest
        