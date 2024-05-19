"""
18. 4Sum

Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

 

Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]
 

Constraints:

1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109

"""
class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        if len(nums) < 4:
            return res

        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                k = j + 1
                l = len(nums) - 1
                while k < l:
                    sum = nums[i] + nums[j] + nums[k] + nums[l]
                    if sum == target:
                        quad = [nums[i], nums[j], nums[k], nums[l]]
                        quad.sort()
                        if not quad in res:
                            res.append(quad)
                        k += 1
                        l -= 1
                    elif sum < target:
                        k += 1
                    else:
                        l -= 1
        return res

    # Find all combinations and then filter
    def fourSum2(self, nums, target):
        def combinations(mylist, r):
            if r == 0:
                return [[]]

            quads = []
            for i in range(len(mylist)):
                first  = [ mylist[i] ]
                others = mylist[i+1:]
                combos = combinations(others, r-1)
                for combination in combos:
                    quads.append(first + combination)
            return quads

        result = list()
        nums.sort()
        sets = combinations(nums, 4)
        for comb in sets:
            if sum(comb) == target:
                if not comb in result:
                    result.append(comb)
        return result

solution = Solution()
mlist = [1,0,-1,0,-2,2]
goal = 0
print(solution.fourSum(mlist, goal))
