"""
Leetcode 0371: Sum of two integers without using + or - operators

Author: Abhishek Kulkarni
email : kulkarni.abhishek12@gmail.com

ex1.
1 + 2 = 3

   0 1
 + 1 0
 -----
   1 1

ex2.
3 + 2 = 5


 carry 1
         1 1
     +   1 0
       ------
       1 0 1

  XOR to sum
  AND and leftshift by 1 digit to find carry

a + b = ?

  a = a XOR b
  carry = (a AND b) << 1     (i.e. AND and left shift by 1 digit)


for large binary digits
e.g.
9 + 11 = 20

            a =  1 0 0 1
            b =  1 0 1 1

     xor_op = (a ^ b) = 0 0 1 0
     and_op = (a & b) = 1 0 0 1
     carry  = 1 0 0 1 0 (left shift and_op i.e. add 0 to right)

 again,
     a = xop_op, b = carry

         0 0 1 0
       1 0 0 1 0

#https://www.youtube.com/watch?v=gVUrDV4tZfY&t=212s


"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # Python integer is large (32 bits)
        # Hence the binary operations will be slow
        # and execution may get timedout.
        # Use masking(AND) of bit_shortner to shorten
        # the binary digits.
        # Refer to the commented method getSumEfficient().
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        return a

    '''
    def getSumEfficient(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        bit_shortner = 0xffffffff

        while (b & bit_shortner) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry

        return (a & bit_shortner) if b > 0 else a
    '''

solution = Solution()
print(solution.getSum(1, 2))
