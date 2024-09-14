#1143. Longest Common Subsequence

class Solution:
    def longestCommonSubsequenceRecursive(self, text1: str, text2: str) -> int:

        #Time limit exeeds with the following input
        # text1 = "pmjghexybyrgzczy"
        # text2 = "hafcdqbgncrcbihkd"
        def lcs(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + lcs(i+1, j+1)
            else:
                return max(lcs(i+1, j), lcs(i, j+1))
        return lcs(0, 0)

    def longestCommonSubsequenceMemo(self, text1: str, text2: str) -> int:
        memo = dict()
        # No time exeeded, but still slower and beats 5% in runtime.
        def lcs(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if (i, j) in memo:
                return memo[(i, j)]

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + lcs(i+1, j+1)
            else:
                memo[(i, j)] = max(lcs(i+1, j), lcs(i, j+1))
            return memo[(i, j)]
        return lcs(0, 0)

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # DP Table
        m = len(text1)
        n = len(text2)

        dp = list()
        for i in range(m+1):
            dp.append([])
            for j in range(n+1):
                dp[i].append(0)

        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
