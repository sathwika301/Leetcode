class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n,101):
            digits=[int(d) for d in str(i)]
            l=len(digits)
            product=1
            for j in range(l):
                if digits[j]==0:
                    product=0
                product=product*digits[j]
            if product%t==0:
                return i
            else:
                continue
                 

        