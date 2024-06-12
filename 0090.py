class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = list()
        nums.sort()

        def dfs(pos, subset):
            if pos == len(nums):
                result.append(subset.copy())
                return

            subset.append(nums[pos])
            dfs(pos+1, subset)
            subset.pop()

            while pos+1 < len(nums) and nums[pos] == nums[pos+1]:
                pos += 1
            dfs(pos+1, subset)
        dfs(0, [])
        return result
