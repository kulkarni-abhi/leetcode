class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count = 0
        for i in range(len(s)-1, -1, -1):
            if count == 0 and s[i] == " ":
                continue
            if s[i] == " ":
                break
            count += 1
        return count

## Test Cases
## "Hello World"
## "   fly me   to   the moon  "
## "luffy is still joyboy"
