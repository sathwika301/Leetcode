class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        arr_sum = sum(nums)
        actual_sum=0
        for i in range(n+1):
            actual_sum += i
        res= actual_sum - arr_sum
        return res

        