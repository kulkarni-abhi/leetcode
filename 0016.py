"""
16. 3Sum Closest

Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0
Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).


Constraints:

3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104


"""

class Solution(object):
    def threeSumClosest(self, nums, target):
        tripplets = list()
        length = len(nums)
        last_index = length - 1
        closest = None
        closest_sum = None
        for i in range(last_index - 1):
            j = i + 1
            k = j + 1
            while True:
                sum = nums[i] + nums[j] + nums[k]
                diff = abs(sum - target)
                if closest is None:
                  closest = diff
                  closest_sum = sum
                else:
                  if diff < closest:
                    closest = diff
                    closest_sum = sum
                k += 1
                if k == length:
                    j += 1
                    k = j + 1
                if j == last_index:
                    break
        return closest_sum

solution = Solution()
integers = [4,0,5,-5,3,3,0,-4,-5]
print(solution.threeSumClosest(integers, -2))
