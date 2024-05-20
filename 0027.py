class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        k = len(nums)
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
                nums.append("#")
                k -= 1
            else:
                i += 1
        return k

solution = Solution()
NUMS = [0,1,2,2,3,0,4,2]
VAL = 2
K = solution.removeElement(NUMS, VAL)
print(NUMS[:K])
