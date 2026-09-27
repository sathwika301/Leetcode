class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        curr=""
        for char in s:
            if char.islower():
                curr+=char
            if char=="(":
                stack.append(curr)
                curr=""
            if char==")":
                r=curr[::-1]
                t=stack.pop()
                curr=t+r
        return curr
            

        