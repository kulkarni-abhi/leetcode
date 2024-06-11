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

    def strStr1(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack) - n + 1):
            matched = True
            ## If array slicing not allowed.
            ## Match each character of needle with haystack
            for j in range(n):
                if needle[j] != haystack[i+j]:
                    matched = False
                    break
            if matched:
                return i
        return -1
solution = Solution()
print(solution.strStr("hello", "ll"))
