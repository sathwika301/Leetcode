class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        n=len(s)
        ans=i=0
        pre=float('-inf')
        mx=0
        while i<n:
            j=i+1
            while j<n and s[j]==s[i]:
                j+=1
            curr=j-i
            if s[i]=="1":
                ans+=curr
            else:
                mx=max(mx,pre+curr)
                pre=curr
            i=j
        ans+=mx
        return ans


        