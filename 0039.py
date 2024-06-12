class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def dfs(current, position, target):
            if target == 0:
                result.append(current.copy())
                return
            if position >= len(candidates):
                return
            if target < 0:
                return

            current.append(candidates[position])
            dfs(current, position, target-candidates[position])

            current.pop()
            dfs(current, position+1, target)

        dfs([], 0, target)
        return result


