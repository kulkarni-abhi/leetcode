class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Start pointer in reverse
        # because we want to find the last word
        # so lets not start from beginning to traverse to the last word
        #
        # then, ignore if there are whitespaces at the end,
        # counting of the last word is not yet started
        # once we receive the last character of the last word start counting
        # move pointer to left until we get whitespace at the beginning of last word.
        # 
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
