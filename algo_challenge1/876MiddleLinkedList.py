from typing import List
import math

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def middleNode(self, head):
        slow = head
        fast = head
        while fast:
            if not fast.next:
                break
            slow = slow.next
            fast = fast.next.next
        return slow


sol = Solution()

fifth = ListNode(val = 4, next = None)
fourth = ListNode(val = 52, next = fifth)
third = ListNode(val = 40, next = fourth)
second = ListNode(val = 82, next = third)
head = ListNode(val = 12, next = second)

answer = sol.middleNode(head)
print(answer)
