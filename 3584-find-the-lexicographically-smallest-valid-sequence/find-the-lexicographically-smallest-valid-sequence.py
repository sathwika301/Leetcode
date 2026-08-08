class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n=len(word1)
        m=len(word2)
        last=[-1]*m
        i=n-1
        j=m-1
        while i>=0 and j>=0:
            if word2[j]==word1[i]:
                last[j]=i
                j-=1
            i-=1

        can_skip=True
        res=[]
        j=0
        for i in range(n):
            if j==m:
                break
            if word1[i]==word2[j]:
                res.append(i)
                j+=1
            elif can_skip and (j==m-1 or i<last[j+1]):
                can_skip=False
                res.append(i)
                j+=1
                
         
        return res if len(res)==m else []
    
sol=Solution()
res=sol.validSequence(word1 = "vbcca", word2 = "abc")
print(res)
        
        