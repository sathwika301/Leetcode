class Solution:
    def minimumPushes(self, word: str) -> int:
        freq={}
        for c in word:
            freq[c]=freq.get(c,0)+1
        res=list(freq.values())
        res.sort(reverse=True)
        m=len(res)
        sum=0
        for j in range(0,m):
            print("j=",j)
            if j<8:
                sum+=1*res[j]
            elif j>=8 and j<16:
                sum+=2*res[j]
            elif j>=16 and j<24:
                sum+=3*res[j]
            else:
                sum+=4*res[j]
        return sum
sol=Solution()
res=sol.minimumPushes(word="xyzxyzxyzxyz")
print(res)
        