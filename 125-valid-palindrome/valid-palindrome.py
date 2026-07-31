class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=""
        for c in s:
            if c.islower():
                res+=c
            elif c.isdigit():
                res+=c
            elif c.isupper():
                res+=c.lower()
            else:
                continue
        i=0
        j=len(res)-1
        while i<=j:
            if res[i]==res[j]:
                i+=1
                j-=1
            else:
                return False
        return True
            

        