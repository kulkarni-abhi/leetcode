"""
1296. Divide Array in Sets of K Consecutive Numbers

Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

Return true if it is possible. Otherwise, return false.

 

Example 1:

Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
Example 2:

Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
Example 3:

Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each array should be divided in subarrays of size 3.
"""

class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        
        hashmap = dict()

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        while hashmap:
            x = min(hashmap)
            for i in range(x, x+k):
                if not i in hashmap:
                    return False
                hashmap[i] -= 1
                if hashmap[i] == 0:
                    del hashmap[i]
        return True
