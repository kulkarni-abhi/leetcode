class Solution:
    def subsets(self, nums):
        """
        Faster Solution using backtracking.
        """
        result = []
        subset = []

        def dfs(idx):
            if idx >= len(nums):
                result.append(subset.copy())
                return

            #Right Tree... Include element
            subset.append(nums[idx])
            dfs(idx + 1)

            #Left Tree.. Do not include element
            subset.pop()
            dfs(idx + 1)
        dfs(0)
        return result
