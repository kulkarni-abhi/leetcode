"""
Leetcode 0322: Smallest Coins Change combination

Tabular Solution

"""
class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0 for _ in range(amount + 1)]
        for amt in range(1, amount + 1):
            res = float('inf')
            for denom in coins:
                if denom <= amt:
                    res = min(res, dp[amt - denom])
            dp[amt] = res + 1
        if dp[-1] == float('inf'):
            return -1
        return dp[-1] 
