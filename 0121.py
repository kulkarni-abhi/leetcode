class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int


        1. min = prices[0]
        2. max = 0
        3. 
        """
        maximum = 0
        minimum = prices[0]

        for price in prices:
            if price < minimum:
                minimum = price
            elif price - minimum > maximum:
                maximum = max(price, maximum)
        return maximum

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int


        1. min = prices[0]
        2. max = 0
        3. 
        """
        maximum = 0
        minimum = prices[0]

        for price in prices:
            minimum = min(price, minimum)
            maximum = max(price - minimum, maximum)
        return maximum

