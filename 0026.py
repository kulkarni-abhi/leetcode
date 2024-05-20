class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 0
        for i, num in enumerate(nums):
            if num in nums[:i]:
                nums[i] = max(nums) + 1
                k += 1
        nums.sort()
        return len(nums) - k

solution = Solution()
mlist = [1,1,2]
K = solution.removeDuplicates(mlist)
print(mlist[:K])
