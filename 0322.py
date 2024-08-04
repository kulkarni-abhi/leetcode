"""
Leetcode 0322: Smallest Coins Change combination

Tabular Solution

"""
class Solution(object):

class Solution(object):
    #This is 2D Table Array
    #https://www.youtube.com/watch?v=J2eoCvk59Rc
    def coinChangeRealTabular(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        result = list()

        # Initialize Matrix
        for row in range(len(coins)):
            result.insert(row, [])
            for col in range(amount + 1):
                result[row].insert(col, amount + 1)

        for row in range(len(coins)):
            for col in range(amount + 1):
                if col == 0:
                    result[row][col] = 0
                    continue
                if coins[row] > col:
                    result[row][col] = result[row-1][col]
                else:
                    exclude_coin = result[row-1][col]
                    include_coin = 1 + result[row][col - coins[row]]
                    result[row][col] = min(exclude_coin, include_coin)
        if result[-1][-1] > amount:
            return -1
        return result[-1][-1]

    def coinChangeTabularSmall(self, coins, amount):
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
