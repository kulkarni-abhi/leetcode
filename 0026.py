class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1  # Initialize the count of unique elements to 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[k] = nums[i]  # Overwrite the next unique element
                k += 1
        return k

    def removeDuplicates_hash(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        hash_map = dict()
        while True:
            if i < len(nums):
                if nums[i] in hash_map:
                    del nums[i]
                    continue
                else:
                    hash_map[nums[i]] = 1
            else:
                break
            i += 1
            
    def removeDuplicates_no_recommended(self, nums):
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
