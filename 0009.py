"""
9. Palindrome Number
Given an integer x, return true if x is a
palindrome
, and false otherwise.



Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-2^31 <= x <= 2^31 - 1

"""

class Solution:
  def isPalindrome(self, x):
    # Without String Conversion
    if x < 0:
      return False
    mylist = []
    while x > 0:
      x, remainder = divmod(x, 10)
      mylist.insert(0,remainder)
    status = True
    for i in range(len(mylist)):
      if mylist[i] != mylist[len(mylist) - i - 1]:
        status = False
        break
    return status

  def isPalindromeStr(self, x):
    x = str(x)
    status = True
    for i in range(len(x)):
      if i >= len(x)/2:
        break
      if x[i] != x[len(x) - i - 1]:
        status = False
        break
    return status

solution = Solution()
print(solution.isPalindrome(121))
print(solution.isPalindrome(-121))
print(solution.isPalindromeStr(121))
print(solution.isPalindromeStr(-121))
