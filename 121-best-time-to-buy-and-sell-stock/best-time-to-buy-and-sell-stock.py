class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_p=float("inf")
        max_p=0
        for curr in prices:
            min_p=min(min_p,curr)
            profit=curr-min_p
            max_p=max(profit,max_p)
        return max_p
                
            
sol=Solution()
res=sol.maxProfit(prices = [7,1,5,3,6,4])
print(res)
        