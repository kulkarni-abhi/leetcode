class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def digit_square_sum(num):
            result = 0
            while num > 0:
                last_digit = num % 10
                result += last_digit * last_digit
                num = num // 10
            return result

        #square_sum = 0
        #if n > 0:
        #    for digit in str(n):
        #        square_sum += int(digit) ** 2

        square_sum = digit_square_sum(n)
        if square_sum == 1:
            return True
        elif square_sum == 4:
            return False
        
        return self.isHappy(square_sum)
