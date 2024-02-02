class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window = dict()
        start  = 0
        size   = 0
        for cursor, char in enumerate(s):
            if char in window:
                if window[char] + 1 > start:
                    start = window[char] + 1
            window[char] = cursor
            size = max(size, cursor - start + 1)
        return size

solution = Solution()
inputs = [
  "pwwkew",
  "abcabcbb",
  "bbbbb",
  "tmmzusxt"
]

for input in inputs:
  print(solution.lengthOfLongestSubstring(input))
