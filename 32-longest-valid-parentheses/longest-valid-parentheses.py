
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if len(s)==0:
            return 0
        st=[-1]
        res=0
        for i in range(len(s)):
            if s[i]=='(':
                st.append(i)
            else:
                st.pop()
                if not st:
                    st.append(i)
                else:
                    l=i-st[-1]
                    res=max(res,l)
        return res
            