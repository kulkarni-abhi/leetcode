class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        answer = ""
        carry = 0
        length_a = len(a)
        length_b = len(b)
        i = 0
        # traverse both list in reverse order
        # length_a - 1, length_a - 2, length_a - 3
        # i = 1, 2, 3, ....

        while i < length_a or i < length_b or carry != 0:
            num1 = 0
            # set num1 if list1 is not exausted
            if i < len(a):
                num1 = int(a[length_a - i - 1])
            
            num2 = 0
            # set num2 if list2 is not exausted
            if i < len(b):
                num2 = int(b[length_b - i - 1])

            total = num1 + num2 + carry
            val = total % 2
            carry = total / 2
            answer = "%d%s" % (val, answer)

            i += 1
        return answer
