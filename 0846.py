"""
846. Hand of Straights

Example 1:

Input: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3
Output: true
Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8]
Example 2:

Input: hand = [1,2,3,4,5], groupSize = 4
Output: false
Explanation: Alice's hand can not be rearranged into groups of 4.
"""

class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        length = len(hand)
        if length % groupSize > 0:
            return False

        hand.sort()

        #result = list()
        while hand:
            #sequence = list()
            small = hand[0]
            for i in range(small, small+groupSize):
                if not i in hand:
                    return False
                #sequence.append(hand.pop(hand.index(i)))
            #result.append(sequence)
        #print(result)
        return True

    def isNStraightHand_dict(self, hand, groupSize):
        hashmap = dict()
        for num in hand:
            hashmap[num] = hashmap.get(num, 0) + 1

        #result = list()
        while hashmap:
            small = min(hashmap)
            #sequence = list()
            for num in range(small, small+groupSize):
                if hashmap.get(num, None) is None:
                    return False
                hashmap[num] -= 1
                #sequence.append(num)
                if hashmap[num] == 0:
                    del hashmap[num]
            #result.append(sequence)
        #print(result)
        return True

solution = Solution()
mylist = [1,2,3,6,2,3,4,7,8]
size = 3

print(solution.isNStraightHand(mylist, size))
print(solution.isNStraightHand_dict(mylist, size))
