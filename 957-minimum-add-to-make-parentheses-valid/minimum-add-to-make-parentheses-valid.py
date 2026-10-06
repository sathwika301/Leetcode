class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        need_open=0
        stack=[]
        for ch in s:
            if ch=='(':
                stack.append(ch)
            elif ch==')':
                if stack:
                    stack.pop()
                else:
                    need_open+=1
        return len(stack)+need_open
