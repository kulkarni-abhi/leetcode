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
def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = strs[0]
    while prefix:
        matched = True
        for word in strs:
            if not word.startswith(prefix):
                matched = False
                break
        if matched:
            break
        prefix = prefix[:-1]
    return prefix

mlist = ["flower","flow","flight"]
mlist = ["reflower","flow","flight"]
print(longestCommonPrefix(mlist))
