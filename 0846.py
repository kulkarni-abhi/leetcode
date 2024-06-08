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
    def __init__(self):
        self.start = 0

    def isNStraightHand(self, hand, groupSize):
        # Recursive
        # Add constructor __init__ for start variable
        length = len(hand)
        if length % groupSize > 0:
            return False

        if self.start == 0:
            hand.sort()
            self.start = 1

        if not hand:
            return True

        small = hand[0]
        for i in range(small, small + groupSize):
            if not i in hand:
                return False
            hand.pop(hand.index(i))
        return self.isNStraightHand(hand, groupSize)

    def isNStraightHand2(self, hand, groupSize):
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
                print(i)
                if not i in hand:
                    return False
                hand.pop(hand.index(i))
                #sequence.append(i)
            #result.append(sequence)
        #print(result)
        return True

    def isNStraightHand3(self, hand, groupSize):
        # without sort, using hashmap
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
