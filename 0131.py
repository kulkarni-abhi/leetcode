class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = list()
        part = list()

        def is_palindrome(x, l, r):
            while l < r:
                if x[l] != x[r]:
                    return False
                l += 1
                r -= 1
            return True

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return

            for j in range(i, len(s)):
                if is_palindrome(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()

        dfs(0)
        return res
