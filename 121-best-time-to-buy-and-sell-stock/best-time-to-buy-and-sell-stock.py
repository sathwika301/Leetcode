class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        
        max_p=0
        for i in range(n-1):
            for j in range(i+1,n):
                if prices[i]<prices[j]:
                    profit=prices[j]-prices[i]
                    max_p=max(max_p,profit)
                else:
                    break
        return max_p
                
            
sol=Solution()
res=sol.maxProfit(prices = [7,1,5,3,6,4])
print(res)
        