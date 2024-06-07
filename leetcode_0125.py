import re
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = 0
        right = len(s) - 1
        palindrome = True

        def is_alpha_numeric(char):
            if re.match("[a-zA-Z0-9]", char):
                return True
            '''
            if  (ord(char) >= ord("a") and ord(char) <= ord("z")) or \
                (ord(char) >= ord("A") and ord(char) <= ord("Z")) or \
                (ord(char) >= ord("0") and ord(char) <= ord("9")):
                return True
            '''
            return False

        while left < right:
            if not is_alpha_numeric(s[left]):
                left += 1
                continue
            if not is_alpha_numeric(s[right]):
                right -= 1
                continue
    
            if s[left].lower() != s[right].lower():
                palindrome = False
                break
            left += 1
            right -= 1
        return palindrome
