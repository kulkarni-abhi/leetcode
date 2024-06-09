"""
Leetcode 0322: Smallest Coins Change combination

Tabular Solution

"""
class Solution(object):
    def coinChangeTabularRecommended(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        max_value = amount + 1
        dp = [max_value] * (amount + 1)
        dp[0] = 0
       
        for coin in coins:
            for x in range(coin, amount + 1):
               dp[x] = min(dp[x], dp[x - coin] + 1)
    
    
        if dp[amount] != max_value:
            return dp[amount]
        else:
            return -1

    
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
