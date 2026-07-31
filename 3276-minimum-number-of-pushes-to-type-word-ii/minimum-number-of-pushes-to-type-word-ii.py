class Solution:
    def minimumPushes(self, word: str) -> int:
        freq={}
        for c in word:
            freq[c]=freq.get(c,0)+1

        res=list(freq.values())
        res.sort(reverse=True)

        m=len(res)
        ans=0
        for i in range(m):
            ans += (i // 8 + 1) * res[i]
        return ans
sol=Solution()
res=sol.minimumPushes(word="xyzxyzxyzxyz")
print(res)
        