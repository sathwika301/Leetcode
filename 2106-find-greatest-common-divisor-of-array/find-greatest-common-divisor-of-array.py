class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a=min(nums)
        b=max(nums)
        return gcd(a,b)
    def gcd(a,b):
        while b!=0:
            a=b
            b=a%b
        return a
sol=Solution()
res=sol.findGCD(nums = [2,5,6,9,10])
print(res)
        