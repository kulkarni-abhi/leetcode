class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lower, upper = 0, len(nums)
        while lower < upper:
            mid = int((lower+upper)/2)
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                lower = mid +1
            else:
                upper = mid
        return lower
