class Solution:
    def maxDepth(self, s: str) -> int:
        left_p=0
        right_p=0
        max_d=0
        for char in s:
            if char=='(':
                left_p+=1
            if char==")":
                right_p+=1
                
            depth=left_p-right_p
            max_d=max(max_d,depth)
        return max_d

            
        