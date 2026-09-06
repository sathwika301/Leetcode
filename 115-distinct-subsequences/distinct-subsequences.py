class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        dp = [[-1] * (len(t) + 1) for _ in range(len(s) + 1)]

        def solve(i, j):
            if j == len(t):
                return 1
            if i == len(s):
                return 0
            if dp[i][j] != -1:
                return dp[i][j]

            if s[i] == t[j]:
                pick = solve(i + 1, j + 1)
                skip = solve(i + 1, j)
                dp[i][j] = pick + skip

            else:
                dp[i][j] = solve(i + 1, j)
            return dp[i][j]
        return solve(0, 0)

        