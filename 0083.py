# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head

        while current:
            if not prev:
                prev = current
                current = current.next
                continue
            if current.val == prev.val:
                prev.next = current.next
                current = current.next
            else:
                prev = current
                current = current.next
        return head
