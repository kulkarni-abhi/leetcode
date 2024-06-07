"""
21. Merge Two Sorted Lists

ou are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # without an additional node at beginning
        result = cur = None
        l1=list1
        l2=list2
        while l1 and l2:
            if l1.val < l2.val:
                if not result:
                    result = cur = ListNode(l1.val)
                else:
                    cur.next = ListNode(l1.val)
                    cur = cur.next
                l1 = l1.next
            else:
                if not result:
                    result = cur = ListNode(l2.val)
                else:
                    cur.next = ListNode(l2.val)
                    cur = cur.next
                l2 = l2.next

        if not result:
            '''
            result and cur are None if any of the lists
            list1 or list2 are empty, while loop not traversed
            so result list is not created or it is still None
            '''
            result = l1 or l2
        else:
            '''
            result list is created and cur is the pointer to result
            updated. 
            either list1 or list2 is still not fully traversed.
            append the remaining list to cur.next
            '''
            cur.next = l1 or l2
        return result

    def mergeTwoListsExtra(self, list1, list2):
        # With an additional node at beginning
        result = cur = ListNode(0)
        l1=list1
        l2=list2
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return result.next
