class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []
       
        def dfs(num, subset, target):
            if len(subset) == k:
                if target == 0:
                    result.append(subset.copy())
                return
                
            for x in range(num + 1, 10):
                if x <= target:
                    dfs(x, subset + [x], target - x)
                else:
                    return
            
        dfs(0, [], n)
        return result
