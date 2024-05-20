class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        position = -1
        length = len(needle)
        for i in range(len(haystack) - length + 1):
            substr = haystack[i:i+length]
            if substr == needle:
                position = i
                break
        return position

solution = Solution()
print(solution.strStr("hello", "ll"))
