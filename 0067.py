class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""

        i = len(a) - 1
        j = len(b) - 1

        carry = 0

        while i >= 0 or j >= 0 or carry:
            num1 = num2 = 0
            if i >= 0:
                num1 = int(a[i])
            if j >= 0:
                num2 = int(b[j])

            total = num1 + num2 + carry
            val = total % 2
            carry = total // 2

            result = str(val) + result
            i -= 1
            j -= 1
        return result
