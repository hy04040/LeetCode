from typing import List
import math

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        node = head
        check = head
        if check.next == None:
            return None
        for i in range (0,n):
            check = check.next
        if check == None:
            node = head.next
            return node
        while check:
            if check.next == None:
                node.next = node.next.next
                break
            node = node.next
            check = check.next
        print(head.val)
        return head

        


sol = Solution()

fifth = ListNode(val = 5, next = None)
fourth = ListNode(val = 4, next = fifth)
third = ListNode(val = 3, next = fourth)
#second = ListNode(val = 2, next = None)
head = ListNode(val = 1, next = None)

answer = sol.removeNthFromEnd(head,1)
print(answer)
