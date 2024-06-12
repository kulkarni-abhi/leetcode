class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        signed = False
        if x < 0:
            x = x * -1
            signed = True
        while x > 0:
            remainder = x % 10
            result = result * 10 + remainder
            x = x // 10
        if result > 2 ** 31 - 1:
            result = 0
        if signed:
            result = result * -1
        return result
