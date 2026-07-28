
class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)

        first=s[0:n//2]
        first="".join(sorted(first))

        middle=""
        if n%2==1:
            middle=s[n//2]

        second=first[::-1]

        return first + middle + second
