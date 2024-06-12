class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        def dfs(start, comb):
            if len(comb) == k:
                result.append(comb.copy())
                return
            for i in range(start, n+1):
                comb.append(i)
                dfs(i+1, comb)
                comb.pop()

        # In the leetcode problems, it is clearly asked that element in range 1 to n.
        # so not starting from 0, and upto n+1 so that n is also included.
        dfs(1, [])
        return result
