"""
97. Interleaving String

https://leetcode.com/problems/interleaving-string/description/

"""

import pprint
pp = pprint.PrettyPrinter(indent=4)

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m = len(s1)
        n = len(s2)
        x = len(s3)

        if m + n != x:
            return False

        dp = [ [False] * (n+1) for row in range(m+1) ]
        #pp.pprint(dp)

        dp[0][0] = True
        for i in range(m+1):
            for j in range(n+1):
                if i > 0 and s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                    dp[i][j] = True
                if j > 0 and s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                    dp[i][j] = True
        return dp[-1][-1]

sol = Solution()
print(sol.isInterleave("aabc", "abn", "aabnabc"))
print(sol.isInterleave("", "a", "c"))
print(sol.isInterleave("", "", ""))
print(sol.isInterleave("", "a", "a"))
print(sol.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
print(sol.isInterleave("aabcc", "dbbca", "aadbbbaccc"))
