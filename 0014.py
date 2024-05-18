"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    base_str = strs.pop()
    size = len(base_str)
    matched = False
    prefix = ""
    for i in range(size, -1, -1):
      prefix = base_str[:i]
      matched = True
      for word in strs:
        if not word.startswith(prefix):
          matched = False
          break
      if matched:
        break
    return prefix

mlist = ["flower","flow","flight"]
mlist = ["reflower","flow","flight"]
print(longestCommonPrefix(mlist))
