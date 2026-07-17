class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        strs.sort()
        s1=strs[0]
        s2=strs[len(strs)-1]
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                res+=s1[i]
            else:
                break
        return res 
                
        