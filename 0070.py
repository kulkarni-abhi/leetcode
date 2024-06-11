class Solution(object):
    def climbStairsRecursive(self, n: int) -> int:
        # Not Recommended
        if n <= 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)
        
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1

        for i in range(n-1):
            temp = a
            a = a + b
            b = temp
        return a
