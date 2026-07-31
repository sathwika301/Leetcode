
class Solution:
    def maxArea(self, height: list[int]) -> int:

        max_amt=0
        i=0
        j=len(height)-1
        while i<j:
            area=(j-i) * min(height[i],height[j])
            max_amt=max(max_amt,area)
            if height[i]<=height[j]:
                i+=1
            else:
                j-=1

        return max_amt

sol=Solution()
res=sol.maxArea(height = [1,8,6,2,5,4,8,3,7])
print(res)

        