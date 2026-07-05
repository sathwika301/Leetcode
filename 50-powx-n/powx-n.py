class Solution:
    def myPow(self, x: float, n: int) -> float:
        def powerf(x,n):
            if n==1:
                return x*n
            elif n==0:
                return 1
            else:
                if n%2==0:
                    return powerf(x*x, n//2)
                if n%2!=0:
                    return x*(powerf(x*x, (n-1)//2))

        if n<0:
            temp=-1*n
            return 1/(powerf(x,temp))
        else:
            return powerf(x,n)
                
sol=Solution()
r=sol.myPow(x = 2.00000, n = -2)
print(r)

        