class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
        """
        heapList = list()
        def heapify(num):
            if len(heapList) < k:
                heapList.append(num)
            else:
                if heapList[-1] < num:
                    heapList.pop()
                    heapList.append(num)
            heapList.sort(reverse=True)

        for i in nums:
            heapify(i)
        return heapList[-1]

    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        # heapify the input, in-place
        heapq.heapify(nums)

        # remove the topmost item from the heap
        # until k reached.
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]
