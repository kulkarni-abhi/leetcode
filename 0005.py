"""
5. Longest Palindromic Substring

Given a string s, return the longest
palindromic

substring
 in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""
class Solution(object):
  #Fastest from middle
  def longestPalindromeRecommended(self, s: str) -> str:
    if len(s) <= 1:
      return s

    def expand_from_center(left, right):
      while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
      return s[left + 1:right]

    max_str = s[0]

    for i in range(len(s) - 1):
      odd = expand_from_center(i, i)
      even = expand_from_center(i, i + 1)

      if len(odd) > len(max_str):
        max_str = odd
      if len(even) > len(max_str):
        max_str = even

    return max_str

 
  def is_palindrome(self, s):
    status = True
    for i in range(len(s) - 1):
      if s[i] != s[len(s)-1-i]:
        status = False
        break
    return status

  def longestPalindrome(self, s):
    longest = ""
    if len(s) == 1:
      longest = s
    for i in range(len(s) - 1):
      substr = s[i]
      for j in range(i+1, len(s)):
        substr = substr + s[j]
        if self.is_palindrome(substr):
          if len(longest) < len(substr):
            longest = substr
    return longest

  def longestPalindromeRecursive(self, s):
    if self.is_palindrome(s):
      return s
    left = self.longestPalindrome(s[1:])
    right = self.longestPalindrome(s[:-1])

    if len(left)>len(right):
      return left
    else:
      return right

solution = Solution()
print(solution.longestPalindrome("b"))
print(solution.longestPalindromeRecursive("babad"))
