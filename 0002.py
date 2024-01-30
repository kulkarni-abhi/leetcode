""""
Leetcode 2: Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.

https://leetcode.com/problems/add-two-numbers/description/

Author: Abhishek Kulkarni
email : kulkarni.abhishek12@gmail.com

"""
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode()
        current = result
        carry = 0

        while True:
            val1 = 0
            val2 = 0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next

            val = (val1 + val2 + carry) % 10
            carry = (val1 + val2 + carry) // 10
            current.val = val
            if l1 or l2 or carry:
                current.next = ListNode()
                current = current.next
            else:
                break
        return result

# pre-reqs for standalone script start
import random

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def array_to_linked_list(xlist):
  """
  This is a mimic function of list insert/push
  (no need to implement in leetcode)

  """
  head = None
  for index, num in enumerate(xlist):
    temp = ListNode(num)
    if index == 0:
      head = temp
    else:
      ptr = head
      while ptr.next:
        ptr = ptr.next
      ptr.next = temp
  return head

def display_list(xlist):
  ptr = xlist
  while ptr:
    print(ptr.val),
    ptr = ptr.next
  print("")

list1 = [ random.randint(0, 9) for i in range(random.randint(1,5)) ]
list2 = [ random.randint(0, 9) for i in range(random.randint(1,5)) ]

l1 = array_to_linked_list(list1)
l2 = array_to_linked_list(list2)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

display_list(l1)
display_list(l2)
display_list(result)
# pre-reqs for standalone script end
