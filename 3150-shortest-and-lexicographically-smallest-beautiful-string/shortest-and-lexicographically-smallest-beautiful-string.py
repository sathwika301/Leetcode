class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []
    
        for i in range(len(s)):
            if s[i] == "1":
                ones.append(i)

        if len(ones) < k:
            return ""

        ans = ""

        for i in range(len(ones) - k + 1):

            start = ones[i]
            end = ones[i + k - 1]

            curr = s[start:end + 1]

            if ans == "":
                ans = curr

            elif len(curr) < len(ans):
                ans = curr

            elif len(curr) == len(ans) and curr < ans:
                ans = curr

        return ans