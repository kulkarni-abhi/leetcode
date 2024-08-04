"""
Leetcode 0518: Coin change - II
https://www.youtube.com/watch?v=L27_JpN6Z1Q
DP Table
"""

import pprint
pp = pprint.PrettyPrinter(indent=4)
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount+1) for _ in range(len(coins))]
        for i in range(len(coins)):
            for j in range(amount + 1):
                if j == 0:
                    dp[i][j] = 1
                    continue
                if coins[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]
        #pp.pprint(dp)
        return dp[-1][-1]
