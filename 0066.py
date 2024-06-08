"""
Leetcode 0066: Plus One to List

"""
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        result = list()
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            num = 0
            if i == len(digits) - 1:
                num = 1
            total = digits[i] + num + carry
            val = total % 10
            carry = total / 10
            result.insert(0, val)
        if carry:
            result.insert(0, carry)
        return result
