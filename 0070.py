class Solution(object):
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
