"""
Author: Abhishek Kulkarni
email : kulkarni.abhishek12@gmail.com

Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

You can return the answer in any order.

Example 1:
----------
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
----------
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
----------
Input: nums = [3,3], target = 6
Output: [0,1]

"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = dict()

        for index, value in enumerate(nums):
            diff = target - value
            if diff in hash_map:
                return [hash_map[diff], index]
            hash_map[value] = index
        return


mylist = [2,7,11,15]
target = 9
solution = Solution()
print(solution.twoSum(mylist, target))
