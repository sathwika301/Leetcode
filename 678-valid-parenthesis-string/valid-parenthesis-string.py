class Solution:
    def checkValidString(self, s: str) -> bool:
        l=0
        h=0
        for ch in s:
            if ch=='(':
                l+=1
                h+=1
            elif ch==')':
                if l>0:
                    l-=1
                h-=1
            else:
                if l>0:
                    l-=1
                h+=1
            if h<0:
                return False
        return l==0 
            