"""
Leetcode 0263: An ugly number 
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

"""
class Solution(object):
    def isUgly(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n<=0: return False
        for factor in (2, 3, 5):
            while n % factor == 0:
                n = n // factor
        if n == 1:
            return True
        return False
